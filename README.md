# get-color-palettes-py

A Python3 script to retrieve color palettes using the colourlovers web API.

## Description

A script to retrieve the current most popular color palettes from www.colourlovers.com that have 5 colors.

Detailed description of the Colour Lovers web API can be found here:
* [Colour Lovers web API](https://www.colourlovers.com/api)

This script was inspired by the work of Matt DesLauriers:
* [nice-color-palettes (written in JavaScript)](https://github.com/Jam3/nice-color-palettes/)

## Getting Started

### Dependencies

* [Colourlovers-API-wrapper](https://github.com/juangallostra/Colourlovers-API-wrapper)
    * install with `pip install colourlovers`

### Installing

* [Optional] Create a new Python virtual environment and activate it
* Install colourlovers
    * install with `pip install colourlovers`

### Executing program

* Update `palette_target_count` in `main.py` and set the number of palette you want to retrieve from Colour Lovers web API
* run the script from the command line: `python main.py`
    * Note: there is a 5 second sleep per request so we don't spam the colourlovers server.
* the script will save into the `palettes` folder

## Authors

* Victor Stepanov
    * [@cgpython](https://twitter.com/cgpython)
    * Checkout my Python tutorials on [YouTube](https://www.youtube.com/channel/UCapoJgKKWSmyDcGOHl5UlNQ)


## Version History

* 0.01
    * Initial Release

## License

This project is licensed under the MIT License, see the LICENSE.md file for details.

Also license info can be found here: https://choosealicense.com/licenses/mit/

## Acknowledgments

This project is standing on the shoulders of these projects:
* [nice-color-palettes (written in JavaScript)](https://github.com/Jam3/nice-color-palettes/)
* [Colourlovers-API-wrapper](https://github.com/juangallostra/Colourlovers-API-wrapper)
