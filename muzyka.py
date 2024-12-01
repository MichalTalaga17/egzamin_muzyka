import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.uic import loadUi

class MyApp(QMainWindow):
    albums = []
    current_album = 0
    def __init__(self):
        super().__init__()
        loadUi("muzyka.ui", self)
        self.get_data()
        self.update_display()
        self.next_button.clicked.connect(self.next_album)
        self.previous_button.clicked.connect(self.previous_album)
        self.download_button.clicked.connect(self.download_album)

    def get_data(self):
        data_file_path = "Data.txt"
        with open(data_file_path, "r", encoding="utf-8-sig") as file:
            lines = file.readlines()
        for i in range(0, len(lines), 6):
            artist = lines[i].strip()
            album = lines[i+1].strip()
            songs_number = int(lines[i+2].strip())
            year = int(lines[i+3].strip())
            download_number = int(lines[i+4].strip())
            self.albums.append({
                "artist": artist,
                "album": album,
                "songs_number": songs_number,
                "year": year,
                "download_number": download_number
                })
            
    def update_display(self):
        album = self.albums[self.current_album]
        self.artist_label.setText(album["artist"])
        self.album_label.setText(album["album"])
        self.songs_number_label.setText(f"{str(album["songs_number"])} utworów")
        self.year_label.setText(str(album["year"]))
        self.download_number_label.setText(str(album["download_number"]))

    def next_album(self):
        self.current_album += 1
        if self.current_album >= len(self.albums):
            self.current_album = 0
        self.update_display()

    def previous_album(self):
        self.current_album -= 1
        if self.current_album < 0:
            self.current_album = len(self.albums) - 1
        self.update_display()

    def download_album(self):
        self.albums[self.current_album]["download_number"] += 1
        self.update_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())