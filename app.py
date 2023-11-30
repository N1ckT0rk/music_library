from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
        print("Welcome to the music library manager!")       
        print("What would you like to do?")
        print(" 1 - List all albums")
        print(" 2 - List all artists")
        x = input('Enter your choice:')
        if x == '2':
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")

        elif x == '1':
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print("Here is the list of albums:")
            for album in albums:
                print(f"{album.id} - {album.title}")

        print("That's not a valid option!")
        

if __name__ == '__main__':
    app = Application()
    app.run()