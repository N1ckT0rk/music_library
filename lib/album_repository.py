from lib.album import Album

class AlbumRepository():
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
        [album.title, album.release_year, album.artist_id])
        return None

    def delete(self, id):
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])
        return None