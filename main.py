"""main function to start http server."""

import argparse

parser = argparse.ArgumentParser(description="PyCon JP 2019!")
parser.add_argument('--port')
args = parser.parse_args()
