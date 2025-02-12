from pydub import AudioSegment
from pydub.playback import play
from musicBoxMaker import *

partition = parsePartitionFile("listNotes.txt")#put your partition here

notes = AudioSegment.from_mp3("it.mp3")#put your recording here

#put the start time (in ms) of each note here
startTimes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000]


noteLength = 200 #length of each note (in ms)
song = AudioSegment.empty()
nbNotes = partition.shape[0]
for i in range(partition.shape[1]):#loop over the partition
    note = AudioSegment.silent(duration=noteLength)
    for j in range(nbNotes):#loop over the notes
        if partition[nbNotes-j-1,i]:
            note = note.overlay(notes[startTimes[j]:startTimes[j]+300])
    song += note
play(song) #play the partition
