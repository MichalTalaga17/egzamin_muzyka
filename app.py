class album:
    def __init__(self, artist, album, songs_number, year, download_number):
        self.artist = artist
        self.album = album
        self.songs_number = songs_number
        self.year = year
        self.download_number = download_number
    
class AlbumList:
    def __init__(self):
        self.albums = []
        self.get_data()
        self.print_albums()

        
    def get_data(self):
        data_file_path = "Data.txt"
        with open(data_file_path, "r", encoding="utf-8-sig") as file:
            lines = file.readlines()
        for i in range(0, len(lines), 6):
            new_album = album(lines[i].strip(), lines[i + 1].strip(), int(lines[i + 2].strip()), int(lines[i + 3].strip()), int(lines[i + 4].strip()))
            self.albums.append(new_album)
        
    """
    *******************************************
    Nazwa funkcji:       print_albums
    Opis funkcji:        Funkcja iteruje po wszystkich albumach przypisanych do obiektu (właściwość `self.albums`) i wyświetla informacje o każdym z nich(artysta, album, liczbę utworów, rok oraz liczbę pobrań.
    Parametry:           self - instancja klasy, której metoda jest wywoływana
    Zwracany typ i opis: brak (funkcja niczego nie zwraca, jedynie wypisuje dane na ekranie)
    Autor:               05251xxxxxx
    *******************************************
    """

    def print_albums(self):
        for album in self.albums:
            print(album.artist)
            print(album.album)
            print(album.songs_number)
            print(album.year)
            print(album.download_number)
            print("")

if __name__ == "__main__":
    AlbumList()

