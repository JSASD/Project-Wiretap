# main.py

import os
import argparse

from src import Args,Gdms

# Set location of current directory for reliable file opening
__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.dirname(
            __file__)
        )
)

print('\n')

# Get arguments from console
#args = Args.getArgs()

Gdms.makeRequest()