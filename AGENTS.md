# Agent instructions

This repository contains **Super Mona**, a MicroPython game for the GitHub
Universe 2026 badge (RP2350B, USB ID `2e8a:1101`). The badge app is the
`super_mona/` folder.

## Deploying to a connected badge

Follow these steps when a user asks you to install or deploy Super Mona.

1. **Get the code.** If you aren't already in a checkout of this repository,
   clone it to a temporary or working directory:
   `git clone https://github.com/martinwoodward/super-mona`.
2. **Check prerequisites.** You need `python3` (3.8+) and `mpremote`.
   - If `mpremote` is missing, install it with
     `python3 -m pip install --user mpremote`. If that is blocked
     (externally managed Python), use `pipx install mpremote` or
     `brew install mpremote` on macOS.
3. **Find the badge.** Run `mpremote devs` and look for a line containing
   `2e8a:1101`.
   - If there isn't one, ask the user to connect the badge with a USB-C *data*
     cable and wake it.
   - Close other programs that hold the port (Thonny, `screen`, Web Serial
     tabs). **Never run serial commands in parallel:** only one process can own
     the port.
4. **Install.** From the repository root, run `python3 install.py`. Allow
   about two minutes. The script:
   - calls `powman.reset_into_msc()` over serial to enter USB mass-storage mode;
   - waits for the `BADGER` volume and replaces `apps/super_mona/` on it;
   - ejects the volume, waits for the serial port to return, and checks every
     file under `/system/apps/super_mona`;
   - resets the badge.

   Pass `--port <port>` if more than one badge is connected.
5. **Report the result.** On success the script ends with
   `verified N files in /system/apps/super_mona`. Tell the user that Super
   Mona is now in the badge menu, and summarise the controls:
   - D-pad: move;
   - A: jump;
   - B: run, carry and throw;
   - Menu: pause;
   - Home: quit.

### Troubleshooting

| Symptom | Fix |
| --- | --- |
| `BADGER volume did not appear` | Older firmware may lack `powman.reset_into_msc`. Ask the user to double-tap the reset button (or open the **Mass Storage** app), then run `python3 install.py --volume <path>` |
| Volume path on Linux | Usually `/media/$USER/BADGER` or `/run/media/$USER/BADGER`; mount it with `udisksctl mount -b /dev/sdX1` if it isn't automounted |
| Volume path on Windows | The drive letter whose label is `BADGER`, for example `E:\` |
| `Device not configured` or a port that is busy | Another process owns the port. Close it and retry. A `read failed` error from the mode switch itself is expected, because the badge reboots |
| Badge doesn't return to serial after eject | Ask the user to press reset. The files are already copied; confirm with `mpremote connect <port> fs ls :/system/apps/super_mona` |
| App crashes on launch with `NameError` or `ImportError` for `badge`, `screen` or `badgeware` | The badge needs the October 2026 (or later) firmware |

### Manual fallback

Use this if `install.py` can't run but the `BADGER` volume is mounted. The
volume root corresponds to `/system` on the badge.

```sh
rm -rf "<BADGER>/apps/super_mona"
cp -R super_mona "<BADGER>/apps/"
find "<BADGER>/apps/super_mona" -name '._*' -delete   # macOS only
# macOS: diskutil eject "<BADGER>"   Linux: eject "<BADGER>"   Windows: eject from Explorer
```

### Rules

- Only write to `apps/super_mona/` on the badge. Don't modify `main.py`,
  `secrets.py`, other apps, or anything under `/state`.
- Normal REPL mode mounts `/system` read-only. `mpremote fs cp` to
  `:/system/...` fails with `EROFS`, so use mass-storage mode, as `install.py`
  does.
- Remote paths in `mpremote fs` commands start with `:`.

## Developing the game

- Run the tests with `python3 -m unittest discover -s tests` (needs Pillow).
  Keep them passing.
- The art is generated. Edit `tools/build_super_mona_assets.py` and run it
  rather than hand-editing PNGs in `super_mona/assets/`. `icon.png` must stay
  24x24.
- `super_mona/README.md` must start with a one-sentence description, because
  the badge menu uses it.
- Firmware API notes (Universe 2026):
  - **Globals:** `badge`, `screen`, `image`, `color`, `shape`, `vec2`,
    `rect`, `run` and the button constants are runtime globals. Don't import
    `badge`.
  - **Input:** use `badge.pressed()`, `badge.held()` and `badge.released()`
    with logical buttons (`BUTTON_SELECT`, `BUTTON_BACK`, `BUTTON_LEFT` and
    so on).
  - **Timing:** use `badge.ticks_delta` for frame-rate-independent movement.
  - **Display mode:** the game uses `badge.mode(LORES | VSYNC)` (160x120).
  - **Text rendering:** set `screen.fill_rule = image.EVEN_ODD` for correct
    vector text.
  - **Sprite flipping:** `screen.blit(img, rect(x, y, -w, h))` mirrors the
    sprite *in place*; it still covers `x..x+w`. Don't add `w` to `x` when
    flipping, or the sprite jumps one tile when it turns. Negative `h` works
    the same way vertically.
  - **Save data:** use `badgeware.State.load/save("super_mona", ...)`. It is
    stored under `/state` on the badge.
- **Quick hardware smoke test without installing:** run
  `mpremote connect <port> exec "import sys; sys.path.insert(0,'/system/apps/super_mona'); exec(open('/system/apps/super_mona/__init__.py').read())"`.
  Stop it after a few seconds; no traceback means it launched. Then run
  `mpremote connect <port> reset`.
