"""Checks that the browser player in web/ loads every file the app needs."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "super_mona"
INDEX = ROOT / "web" / "index.html"


def listed(name):
    """Return the strings in `const <name> = [...]` in web/index.html."""
    match = re.search(r"const %s = \[(.*?)\];" % name, INDEX.read_text(), re.S)
    if not match:
        raise AssertionError("web/index.html has no %s list" % name)
    return sorted(re.findall(r'"([^"]+)"', match.group(1)))


class WebPlayerTests(unittest.TestCase):
    def test_modules_match_app(self):
        expected = sorted(p.name for p in APP.glob("*.py"))
        self.assertEqual(listed("MODULES"), expected,
                         "update MODULES in web/index.html")

    def test_sprites_match_assets(self):
        expected = sorted(p.name for p in (APP / "assets").glob("*.png"))
        self.assertEqual(listed("SPRITES"), expected,
                         "update SPRITES in web/index.html")


if __name__ == "__main__":
    unittest.main()
