"""
A script to retrieve color palettes using the Colour Lovers web API
https://www.colourlovers.com/api

YouTube tutorial here: https://youtu.be/GLrj1_SUFD4

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


def extract_hex_triplet_color_palettes(palettes_result, target_color_count):
    color_palettes = []
    # extract the hex triplet color palettes
    for result in palettes_result:
        # not all color palettes have exactly `target_color_count` colors
        if len(result.colors) == target_color_count:
            # make a list of colors with the '#' char
            color_palettes.append([f"#{color}" for color in result.colors])

    print(f"Retrieve {len(color_palettes)} color palettes...")

    return color_palettes


def save_color_palettes_to_json(color_palettes, target_palette_count):
    """
    if we have downloaded some color palettes saved them into a JSON file in a folder named 'palettes'
    """
    if color_palettes:
        palettes_folder_path = Path(__file__).parent.absolute().joinpath("palettes")
        palettes_folder_path.mkdir(exist_ok=True)

        color_palettes_json_path = palettes_folder_path.joinpath(f"{target_palette_count}_color_palettes.json")
        with open(color_palettes_json_path, "w") as json_palettes:
            json_text = json.dumps(color_palettes[:target_palette_count], indent=4)
            json_palettes.write(json_text)
    else:
        print("WARNING: no color palettes found")


def get_color_palettes(target_palette_count, target_color_count):
    """Use the Colour Lovers web API to download color palettes"""
    cl = clapi.ColourLovers()

    color_palettes = []

    # the colourlovers API supports a maximum of 100 results in a single request
    number_of_results = 100

    # how long we want to sleep between each request
    sleep_seconds = 10

    # used to offset the result that is returned from the API
    index = 0
    while len(color_palettes) < target_palette_count:
        if index != 0:
            print(f"\n\tSleeping {sleep_seconds} seconds so we don't spam the server with requests...\n")
            time.sleep(sleep_seconds)

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

        result = extract_hex_triplet_color_palettes(palettes_result, target_color_count)
        color_palettes.extend(result)

    return color_palettes


def main():
    # how many five color palette do we want to return
    target_palette_count = 200

    # how many colors we want each color palette to have
    target_color_count = 5
    color_palettes = get_color_palettes(target_palette_count, target_color_count)

    save_color_palettes_to_json(color_palettes, target_palette_count)


if __name__ == "__main__":
    main()
