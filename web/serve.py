#!/usr/bin/env python3
"""Serve Super Mona locally and open it in the browser."""

import argparse
import errno
import functools
import http.server
import pathlib
import threading
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parents[1]
SERVED = (ROOT / "web", ROOT / "super_mona")


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serve only the player and the app, and only to this machine."""

    def send_head(self):
        # A page from another site can point its own host name at 127.0.0.1
        # (DNS rebinding), but it cannot fake the Host header.
        port = self.server.server_address[1]
        host = self.headers.get("Host", "").lower()
        if host not in ("127.0.0.1:%d" % port, "localhost:%d" % port):
            self.send_error(403)
            return None
        # translate_path() resolves "..", so check where the request really
        # lands; this keeps .git and the rest of the repository private.
        target = pathlib.Path(self.translate_path(self.path)).resolve()
        if not any(target == top or top in target.parents for top in SERVED):
            self.send_error(404)
            return None
        return super().send_head()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    handler = functools.partial(Handler, directory=str(ROOT))
    try:
        server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as err:
        if err.errno != errno.EADDRINUSE:
            raise
        raise SystemExit("Port %d ist belegt; einen anderen mit --port wählen." % args.port)
    with server:
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
