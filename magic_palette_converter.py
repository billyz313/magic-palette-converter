"""
Place palettes in a subdirectory named palettes.  Place this file in the parent directory.
run python magic_palette_converter.py
"""
import os


def convert_percent(which):
    return float(which) * 255


def convert_to_hex(file_name):
    with open(os.path.join("palettes", file_name), 'r+') as file:
        # Read each line of the file
        lines = file.readlines()

        # Loop through each line
        for i in range(len(lines)):
            try:
                # Split the line into individual RGB values
                if lines[i].startswith("#") or lines[i].strip() == "":
                    pass
                else:
                    the_split = lines[i].replace('\t', ' ').replace('   ', ' ').replace('  ', ' ').strip().split(' ')
                    r = the_split[0]
                    g = the_split[1]
                    b = the_split[2]
                    if float(r) <= 1 and float(g) <= 1 and float(b) <= 1:
                        r = convert_percent(r)
                        g = convert_percent(g)
                        b = convert_percent(b)

                    # Convert the RGB values to hex
                    hex_value = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))

                    # Overwrite the RGB values with the hex value
                    lines[i] = hex_value + '\n'
            except:
                print("Could not process: " + file_name)
                lines = []
                break

        # Write the updated lines back to the file
        if len(lines) > 0:
            file.seek(0)
            file.truncate()
            file.writelines(lines)


cwd = os.path.join(os.getcwd(), "palettes")
for filename in os.listdir(cwd):
    # Check if the file is a text file
    if filename.endswith('.pal'):
        # Call the function to convert RGB values to hex and overwrite the file
        convert_to_hex(filename)
