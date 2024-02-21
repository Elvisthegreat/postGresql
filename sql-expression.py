# import some classes from sqlalchemy
from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for the "Artist" table
artist_table = Table(
    "artist", meta,
    Column("artist_id", integer, primary_key=True),
    Column("name", String)
)

# create variable for "Album" table
album_table = Table(
    "album", meta,
    Column("album_id", integer, primary_key=True),
    Column("title", String),
    Column("artist_id", integer, ForeignKey("artist_table.artist_id")),
    Column("album_id", integer, primary_key=False),
)

# create variable for "Track" table
track_table = Table(
    "track", meta,
    Column("track_id", integer, primary_key=True),
    Column("name", String),
    Column("media_type_id", integer, ForeignKey("album_table.album_id")),
    Column("genre_id", integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)