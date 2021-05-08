from moviepy.editor import *


def extract_songs(source, songs):
    for key, val in songs.items():
        newsound = source.subclip(val[0], val[1]) 
        newsound.write_audiofile("./{}.mp3".format(key))

def parse_time(time):
    time = [int(x) for x in time.split(":")]
    while len(time)<3:
        time = [0]+time
    return time

def generate_songs_duration(fn='./song_list.txt'):
    with open(fn, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
    song_list = []
    for line in lines:
        vals = line.split(" ")
        time = parse_time(vals[0])
        title = " ".join(vals[1:])
        song_list.append((title, "{:0>2d}:{:0>2d}:{:0>2d}".format(time[0], time[1], time[2])))
    songs = dict()
    for i in range(len(song_list)-1):
        item = song_list[i]
        next_item = song_list[i+1]
        songs[item[0]] = (item[1], next_item[1])
    return songs
        

if __name__ == '__main__':
    source = AudioFileClip("./sample.mp4")
    songs = koko_arare_live()
    extract_songs(source, songs)
