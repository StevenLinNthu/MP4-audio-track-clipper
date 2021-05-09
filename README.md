# MP4-audio-track-clipper

Usage:

```cmd
python audio_extractor.py --source <source path>
```

Song list:

​	The song list should be in the same directory of the audio_extractor.py, and the format should be as followed.

```cmd
<start-time> Song title
<start-time> Song title2
```

For example:

```cmd
00:00:01 Bad Day
00:03:49 END
```

The start time of next song will be the end time of the current song.