from lib.album import Album
from lib.album_repository import AlbumRepository

# When we call AlbumRepository#all
# We get a list of Album objects reflecting the seed data.
def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2)
    ]

# When we call AlbumRepository#create
# we get a new record in the database.
def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    new_album = Album('Supernova', 2021, 2)

    repository.create(new_album)

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
        Album('Supernova', 2021, 2)
    ]
    
# When we call AlbumRepository#delete
# We remove a record from the database
def test_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    # Delete by id
    repository.delete(1)
    print(repository.all())

    result = repository.all()
    assert result == [
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
    ]
    