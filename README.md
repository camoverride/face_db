# face_db

Simple script to generate a database of face embeddings from [the FFHQ dataset](https://github.com/NVlabs/ffhq-dataset).


## Steps

Download [the dataset](https://www.kaggle.com/datasets/arnaud58/flickrfaceshq-dataset-ffhq/).

Install all `requirements.txt`.

Run the database generating script like this: `python create_embedding_db.py path/to/face/images`.


## Properties

If a face is unable to be embedded, it will not appear as an entry in the database.

The resulting sqlite database will be named `face_embeddings.db`.

It will look like this:

```
id | embedding
```

And you can inspect it like this:

```
> sqlite3 face_embeddings.db
> .tables
> SELECT * FROM faces LIMIT 10;
> .exit
```

If you're in the process of generating the database and want to check on the progress, use this query:

```
> SELECT id FROM faces ORDER BY id DESC LIMIT 1;
```

Enjoy!
