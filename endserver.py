#!/usr/bin/env python3
import os
import subprocess


# Kill the actual game (WW13.dmb) so we can recompile it with the new map
def kill_server():
    command = "sudo pkill -9 -f WW13.dmb"
    subprocess.run(command, shell=True)


# Compile .dmb in linux using WW13.dme
def compile_dme_to_dmb():

    dme_file_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "WW13.dme"))
    os.system(f'DreamMaker {dme_file_path}') 


if __name__ == "__main__":
    kill_server()
    compile_dme_to_dmb()
