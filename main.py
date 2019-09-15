"""main function to start http server."""

import argparse
from aiohttp import web

parser = argparse.ArgumentParser(description="PyCon JP 2019!")
parser.add_argument('--port')
args = parser.parse_args()

app = web.Application()

web.run_app(app, port=args.port)
