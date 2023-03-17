# Magic Palette Converter for THREDDS 5.x

[![Python: 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This script is used primarily for converting palette files from RGB values to hex values.  In THREDDS V4.8 and below 
the palettes were defined by either RGB values or RGB percentages.  In THREDDS V5.x they require the palettes 
to be hex values.
To make the conversion an easier process I have created the Magic Palette Converter for THREDDS.

## Use
- Clone the script
- run the script

### Quick note before running the script
This script will overwrite existing palettes which usually is the desired outcome due to 
naming. If you would like to preserve the original palettes you can pass -o False and new palettes will be 
created with the prefix hex_

When running, pass -path with the full system path to your palettes.  Relative paths from the python file usually 
work, but full paths always work.

```shell
python magic_palette_converter.py -path PATH_TO_YOUR_PALETTES
```

If there were any palette files that could not be converted they will be noted in the console.  This could
happen if there are unusual lines of text in the files.  If you find a case where this happens, please create an [issue](https://github.com/billyz313/magic-palette-converter/issues).

## Contact

### Authors

- [Billy Ashmall](https://github.com/billyz313)


## License and Distribution

Magic Palette Converter for THREDDS is distributed by Billy Ashmall under the terms of the MIT License. See
[LICENSE](https://github.com/billyz313/magic-palette-converter/blob/master/LICENSE) in this directory for more 
information.

## Privacy & Terms of Use

Magic Palette Converter for THREDDS in no way collects or uses any personal information.  This is completely 
open source software (OSS), you are free to  use this software as you find it useful to your tasks.  
Feel free to modify, update, and submit a pull request.
