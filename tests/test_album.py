from lib.album import Album
# Album constructs with an id, title, release_year 
# and artist_id

def test_album_contructs():
    album = Album("Test title", 1995, 1)
    assert album.title == "Test title"
    assert album.release_year == 1995
    assert album.artist_id == 1