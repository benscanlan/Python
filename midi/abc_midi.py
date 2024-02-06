from midiutil import MIDIFile

def generate_abc_midi(abc_notation, output_file):
    # Create MIDIFile object
    midi = MIDIFile(1)

    # Add a track to the MIDI file
    track = 0
    time = 0
    midi.addTrackName(track, time, "Generated Track")
    midi.addTempo(track, time, 120)  # Tempo in BPM

    # Add ABC notation to the MIDI file
    midi.addABCMIDI(track, time, abc_notation)

    # Save the MIDI file
    with open(output_file, "wb") as midi_file:
        midi.writeFile(midi_file)

# Example usage
abc_notation = "C4 D4 E4 F4 G4 A4 B4"
output_file = "generated_music.mid"
generate_abc_midi(abc_notation, output_file)
