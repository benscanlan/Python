import subprocess

def generate_abc_midi(abc_notation, output_file):
    abc_content = f'''X:1
T:Generated Music
M:4/4
L:1/4
K:C
{abc_notation}'''
    
    # Write ABC notation to a temporary file
    with open('temp.abc', 'w') as abc_file:
        abc_file.write(abc_content)

    # Convert ABC to MIDI using external 'abc2midi' command
    subprocess.run(['abc2midi', 'temp.abc', '-o', output_file])

    # Remove temporary ABC file
    subprocess.run(['rm', 'temp.abc'])

# Example usage
abc_notation = "C4 D4 E4 F4 G4 A4 B4"
output_file = "generated_music.mid"
generate_abc_midi(abc_notation, output_file)

