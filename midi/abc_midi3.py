from midiutil import MIDIFile

def generate_hello_world_midi(output_file):
    # Create MIDIFile object with one track
    midi = MIDIFile(1)

    # Add track name and tempo
    track = 0
    time = 0
    midi.addTrackName(track, time, "Hello World Track")
    midi.addTempo(track, time, 120)  # Tempo in BPM

    # Add notes for a simple "hello world" melody
    notes = [60, 62, 64, 65, 67, 69, 71]  # MIDI note numbers for C major scale
    durations = [1, 1, 1, 1, 1, 1, 1]      # Durations (in beats) for each note
    volume = 100                           # Volume (0-127)

    for note, duration in zip(notes, durations):
        midi.addNote(track, 0, note, time, duration, volume)

        # Increment time for the next note
        time += duration

    # Write the MIDI file
    with open(output_file, "wb") as midi_file:
        midi.writeFile(midi_file)

# Example usage
output_file = "hello_world.mid"
generate_hello_world_midi(output_file)
print(f"Generated {output_file}")

