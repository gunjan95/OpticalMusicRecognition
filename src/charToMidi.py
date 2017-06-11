from midiutil import MIDIFile
import meta
def keyMapping(testResults,fileName):
    #print testResults
    #midiKeyMap = dict({"sa": 60, "re": 62, "ga": 64, "ma": 65, "pa": 67, "dha": 69, "ni": 71, "saa": 72})
    dict = {"sa": 60, "re": 62, "ga": 64, "ma": 65, "pa": 67, "dha": 69, "ni": 71, "saa": 72, "hy":00}

    mappedKeys = []
    for symbol in testResults:
        mappedKeys.append(dict[symbol])
    createMidi(mappedKeys,fileName)

def createMidi(mappedKeys,fileName):
    track = 0
    channel = 0
    time = 0  # In beats
    duration = 1  # In beats
    tempo = 100  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1,adjust_origin=True)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(mappedKeys):
        if (mappedKeys[i] != 00):
            if(len(mappedKeys) > i+1):
                if(mappedKeys[i+1]!=00):
                    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
                else:
                    MyMIDI.addNote(track, channel, pitch, time + i, duration+1, volume)
            else:
                MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open(meta.getRootDir() + '/MIDI_files/'+fileName+'.mid', "wb") as output_file:
        MyMIDI.writeFile(output_file)