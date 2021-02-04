import requests
from bs4 import BeautifulSoup
import re
import pyperclip

artist = input("Enter artist (example young thug):  ").lower()
new_artist = artist.replace(" ", "")
first_letter = new_artist[0]
source = requests.get(f"https://www.azlyrics.com/{first_letter}/{new_artist}.html").text
soup = BeautifulSoup(source, "html.parser")


album_names = soup.find_all("div", attrs={"class": "album"})
album_items = soup.find_all("div", attrs={"class": "listalbum-item"})


def get_albums():
    index = 0
    for elem in album_names:
        index += 1
        print(str(index) + ".", elem.get_text())


def find_songs():
    index = -1
    songs = []
    for elem in album_items:
        index += 1
        print(str(index) + ".", elem.get_text())
        songs.append(elem.get_text())

    print("\n--> Lyrics <--\n")
    get_song = input("Enter song number or song name: ")
    try:
        s = int(get_song)
        song_index = songs[s]
        reg = r"\([\s\S]*\)"
        new_song = re.sub(reg, "()", song_index)
        new_song = new_song.replace("(", "")
        new_song = new_song.replace(")", "")
        new_song = new_song.replace("&", "")
        new_song = new_song.replace("?", "")
        new_song = new_song.replace(".", "")
        new_song = new_song.replace('"', "")
        new_song = new_song.replace("'", "")
        new_song = new_song.replace(" ", "")
        new_song = new_song.lower()
        url = f"https://www.azlyrics.com/lyrics/{new_artist}/{new_song}.html"
        pyperclip.copy(url)
        print("link copied to clipboard")
        source = requests.get(
            f"https://www.azlyrics.com/lyrics/{new_artist}/{new_song}.html"
        ).text
        soup = BeautifulSoup(source, "html.parser")
        st = ""
        lyrics = soup.find_all("div", attrs={"class": "col-xs-12 col-lg-8 text-center"})
        for i in lyrics:
            st += i.get_text()
        x = st.rsplit("\n", 47)[0].lstrip()
        x = re.sub(r"\n\s*\n", "\n\n", x)
        print(x)
    except:
        reg = r"\([\s\S]*\)"
        new_song = re.sub(reg, "()", get_song)
        new_song = new_song.replace("(", "")
        new_song = new_song.replace(")", "")
        new_song = new_song.replace("&", "")
        new_song = new_song.replace("?", "")
        new_song = new_song.replace(".", "")
        new_song = new_song.replace('"', "")
        new_song = new_song.replace("'", "")
        new_song = new_song.replace(" ", "")
        new_song = new_song.lower()
        url = f"https://www.azlyrics.com/lyrics/{new_artist}/{new_song}.html"
        pyperclip.copy(url)
        print("link copied to clipboard")
        source = requests.get(
            f"https://www.azlyrics.com/lyrics/{new_artist}/{new_song}.html"
        ).text
        soup = BeautifulSoup(source, "html.parser")
        st = ""
        lyrics = soup.find_all("div", attrs={"class": "col-xs-12 col-lg-8 text-center"})
        for i in lyrics:
            st += i.get_text()
        x = st.rsplit("\n", 47)[0].lstrip()
        x = re.sub(r"\n\s*\n", "\n\n", x)
        print(x)


def menu():
    while True:
        menu = input(
            """
1. search all artists albums
2. Search all artists songs
\nChoice: """
        )
        if menu == "1" or menu == 1:
            get_albums()
        else:
            find_songs()


if __name__ == "__main__":
    menu()
