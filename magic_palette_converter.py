import os
import argparse
import re


def parse_arguments():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-path",
                        "--palette_path",
                        help="Path to palettes you need converted",
                        default=os.path.join(os.getcwd(), "palettes"))
    parser.add_argument("-o",
                        "--overwrite",
                        help="Overwrite is true by default, to maintain current palette files and create new ones set "
                             "to False",
                        default="True")

    return parser.parse_args()


def convert_percent(which):
    return float(which) * 255


def convert_to_hex(palette_path, file_name, _overwrite):
    with open(os.path.join(palette_path, file_name), 'r+') as file:
        # Read each line of the file
        lines = file.readlines()

        # Loop through each line
        for i in range(len(lines)):
            try:
                # Split the line into individual RGB values
                if lines[i].startswith("#") or lines[i].strip() == "":
                    pass
                else:
                    the_split = re.sub('[ \t]+', ' ', lines[i]).strip().split(' ')
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
            except Exception as e:
                print("Could not process: " + file_name)
                print(str(e))
                lines = []
                break

        # Write the updated lines back to the file
        if len(lines) > 0:
            if _overwrite:
                file.seek(0)
                file.truncate()
                file.writelines(lines)
            else:
                with open(os.path.join(palette_path, "hex_" + file_name), 'w') as hex_file:
                    hex_file.writelines(lines)


if __name__ == '__main__':
    # Parse the arguments
    args = parse_arguments()

    print("You are converting your palettes from: " + args.palette_path)
    overwrite = args.overwrite.lower().capitalize() == "True"

    for filename in os.listdir(args.palette_path):
        # Check if the file is a text file
        if filename.endswith('.pal'):
            # Call the function to convert RGB values to hex and overwrite the file
            convert_to_hex(args.palette_path, filename, overwrite)

    print("Your palette conversion is complete.")