def main():
    music1 = Music("Ed Sheeran","1", "Hearts Don't Break Around Here", "Divide", 2017)
    music2 = Music("Queen", "1", "Bohemian Rhapsody", "A Night at the Opera", 1975)
    print(music1,"\n")
    print(music2)
class Music:
    def __init__(self, artist, track, title, album, year):
        self.artist = artist
        self.track = track
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f"Performer: {self.artist}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}" 



if __name__ == "__main__":
    main()