#!/usr/bin/env python3
"""Serve the repository locally and open Super Mona in the browser."""

import argparse
import errno
import functools
import http.server
import pathlib
import threading
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parents[1]


def open_server(port, handler):
    """Bind to port, or to the next free one if something else holds it."""
    for candidate in range(port, port + 20):
        try:
            return http.server.ThreadingHTTPServer(("127.0.0.1", candidate), handler)
        except OSError as err:
            if err.errno != errno.EADDRINUSE:
                raise
            print("Port %d ist belegt, versuche %d ..." % (candidate, candidate + 1))
    raise SystemExit("Kein freier Port zwischen %d und %d gefunden." % (port, port + 19))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    with open_server(args.port, handler) as server:
        url = "http://127.0.0.1:%d/web/" % server.server_address[1]
        print("Super Mona: %s  (Strg+C beendet den Server)" % url)
        if not args.no_browser:
            threading.Timer(0.5, webbrowser.open, [url]).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
