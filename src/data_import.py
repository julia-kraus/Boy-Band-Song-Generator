# after the blog post in https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29

import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import json

file = open("lyrics_4.txt", "w")  # File to write lyrics to
genius = lg.Genius('rBHwjaJIqHEkwwNfMRDdw0c5qJRVZXNdf_K0UAHPNzbktN3NxMHsMshu7TxLFYH9',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)


# read file
with open('artist_conf.json', 'r') as myfile:
    data=myfile.read()

# parse file
artists = json.loads(data)["first_time_error"]


def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  # Counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))  # Deliminator
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:  #  Broad catch which will give us the name of artist and song that threw the exception
            print(f"some exception at {name}: {c}")


get_lyrics(artists, 100)
