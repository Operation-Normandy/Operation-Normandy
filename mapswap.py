#!/usr/bin/env python3
import os
import sys


def modify_dme_file(winner):
    dme_file_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "WW13.dme"))

    # Manually enumerated list of maps in rotation, 
    # must be updated when maps are added to rotation
    include_statements = {
        "CITY": "maps\\city\\city_level1.dmm",
        "TOWER": "maps\\tower\\level1.dmm",
        "WINTER_LINE": "maps\\winter_line.dmm",
        "FACTORY": "maps\\factory\\factory.dmm"
    }

    with open(dme_file_path, "r") as dme_file:
        lines = dme_file.readlines()

    # Assuming the last #include statement is always the map .dmm,
    # remove it and replace with vote winner
    # If other files modify the .dmm in the future, will need to
    # make sure not to break things

    new_lines = lines[:-2]
    if winner in include_statements:
        new_lines.append(f'#include "{include_statements[winner]}"')
    else:
        print(f"Invalid winner: {winner}")
        sys.exit(1)
    new_lines.append("\n// END_INCLUDE")

    with open(dme_file_path, "w") as dme_file:
        dme_file.writelines(new_lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        
        # Only viewable when called as standalone file
        print("Usage: python mapswap.py <winner>")
        sys.exit(1)

    winner = sys.argv[1]
    modify_dme_file(winner)
