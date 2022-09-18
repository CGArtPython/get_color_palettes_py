"""
A script to retrieve color palettes using the Colour Lovers web API
https://www.colourlovers.com/api

This script was inspired by the work of Matt DesLauriers
https://github.com/Jam3/nice-color-palettes/
"""

from pathlib import Path
import json
import sys
import time

# check if the colourlovers module is installed
try:
    from colourlovers import clapi

    print("the `colourlovers` module was imported")
except ModuleNotFoundError:
    print("ERROR: the `colourlovers` module is not installed")
    print("ERROR: please pip install `colourlovers`")
    sys.exit(-1)


def main():
    cl = clapi.ColourLovers()

    five_color_palettes = []

    # how many five color palette do we want to return
    palette_target_count = 100

    # the colourlovers API supports a maximum of 100 results in a single request
    number_of_results = 100

    # used to offset the result that is returned from the API
    index = 0
    while len(five_color_palettes) < palette_target_count:

        if index != 0:
            seconds = 10
            print(f"\n\tSleeping {seconds} seconds so we don't spam the server with requests...\n")
            time.sleep(seconds)

        # query the colourlovers API for the most popular palettes
        palettes_result = cl.search_palettes(
            request="top",
            numResults=number_of_results,
            resultOffset=index * number_of_results,
        )
        index += 1

        if not palettes_result:
            print("ERROR: the colourlovers API returned an empty result")
            continue

        # extract the hex triplet color palettes
        for result in palettes_result:

            # not all color palettes have exactly 5 colors
            if len(result.colors) == 5:
                # make a list of colors with the '#' char
                five_color_palettes.append([f"#{color}" for color in result.colors])

        print(f"Retrieve {len(five_color_palettes)} color palettes...")

    # if we have downloaded some color palettes saved them into a JSON file in a folder named 'palettes'
    if five_color_palettes:
        palettes_folder_path = Path(__file__).parent.absolute().joinpath("palettes")
        palettes_folder_path.mkdir(exist_ok=True)

        color_palettes_json_path = palettes_folder_path.joinpath(f"{palette_target_count}_five_color_palettes.json")
        with open(color_palettes_json_path, "w") as json_palettes:
            json_palettes.write(json.dumps(five_color_palettes[:palette_target_count], indent=4))


if __name__ == "__main__":
    main()
