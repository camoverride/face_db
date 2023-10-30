import os
import sys
import sqlite3
import face_recognition



# Path to all the face pics.
FACE_PIC_BASE_PATH = sys.argv[1]


def create_face_embedding(image: str) -> list:
    """
    Accepts a path to an image file and returns an embedding as a numpy array.

    Parameters
    ----------
    image : str
        The path to an image file.

    Returns
    -------
    list
        The image embedded as a 128-dimension vector.
    """
    image_file = face_recognition.load_image_file(image)
    try:
        embedding = face_recognition.face_encodings(image_file)[0]
    except IndexError:
        return None

    return embedding


# Connect to a database.
con = sqlite3.connect("face_embeddings.db")
cur = con.cursor()

# Create faces table if it doesn't already exist.
try:
    cur.execute("CREATE TABLE faces (id VARCHAR(255), embedding VARCHAR(255), UNIQUE(id))")
except sqlite3.OperationalError:
    pass

# Insert every file into the database
for file in sorted(os.listdir(FACE_PIC_BASE_PATH)):
    file_path = os.path.join(FACE_PIC_BASE_PATH, file)

    # Sometimes an embedding can't be created.
    try:
        embedding = create_face_embedding(file_path)
    except: # IndexError:
        embedding = None
    
    # Ignore file if already uploaded.
    sql = """
        INSERT OR IGNORE INTO faces(id, embedding)
        VALUES(?, ?)
        """
    cur.execute(sql, (file, str(embedding))) # convert the embedding vector to a string.
    con.commit()
