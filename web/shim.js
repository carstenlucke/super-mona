// Browser stand-in for the Universe 2026 badge firmware: canvas drawing,
// bitmap fonts and input. badge_shim.py wraps this in the Python API that
// super_mona/ expects (screen, image, color, badge, run, ...).

// Pixel fonts --------------------------------------------------------------
// Rows 0-6 sit on the baseline, rows 7-8 are descenders.
const GLYPHS = {
  " ": "...",
  "!": "#|#|#|#|#|.|#",
  "%": "##...|##..#|...#.|..#..|.#...|#..##|...##",
  "'": "#|#",
  "(": ".#|#.|#.|#.|#.|#.|.#",
  ")": "#.|.#|.#|.#|.#|.#|#.",
  "*": "...|#.#|.#.|#.#",
  "+": "...|...|.#.|###|.#.",
  ",": "..|..|..|..|..|.#|.#|#.",
  "-": "...|...|...|###",
  ".": ".|.|.|.|.|.|#",
  "/": "..#|..#|.#.|.#.|.#.|#..|#..",
  ":": ".|.|#|.|.|#",
  "<": "...|..#|.#.|#..|.#.|..#",
  "=": "...|...|###|...|###",
  ">": "...|#..|.#.|..#|.#.|#..",
  "?": ".##.|#..#|...#|..#.|.#..|....|.#..",
  "_": "....|....|....|....|....|....|####",
  "0": ".##.|#..#|#..#|#..#|#..#|#..#|.##.",
  "1": ".#.|##.|.#.|.#.|.#.|.#.|###",
  "2": ".##.|#..#|...#|..#.|.#..|#...|####",
  "3": "###.|...#|...#|.##.|...#|...#|###.",
  "4": "#..#|#..#|#..#|####|...#|...#|...#",
  "5": "####|#...|#...|###.|...#|...#|###.",
  "6": ".##.|#...|#...|###.|#..#|#..#|.##.",
  "7": "####|...#|...#|..#.|..#.|.#..|.#..",
  "8": ".##.|#..#|#..#|.##.|#..#|#..#|.##.",
  "9": ".##.|#..#|#..#|.###|...#|...#|.##.",
  "A": ".##.|#..#|#..#|####|#..#|#..#|#..#",
  "B": "###.|#..#|#..#|###.|#..#|#..#|###.",
  "C": ".##.|#..#|#...|#...|#...|#..#|.##.",
  "D": "###.|#..#|#..#|#..#|#..#|#..#|###.",
  "E": "####|#...|#...|###.|#...|#...|####",
  "F": "####|#...|#...|###.|#...|#...|#...",
  "G": ".##.|#..#|#...|#.##|#..#|#..#|.###",
  "H": "#..#|#..#|#..#|####|#..#|#..#|#..#",
  "I": "###|.#.|.#.|.#.|.#.|.#.|###",
  "J": "..##|...#|...#|...#|#..#|#..#|.##.",
  "K": "#..#|#..#|#.#.|##..|#.#.|#..#|#..#",
  "L": "#...|#...|#...|#...|#...|#...|####",
  "M": "#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#",
  "N": "#..#|##.#|##.#|#.##|#.##|#..#|#..#",
  "O": ".##.|#..#|#..#|#..#|#..#|#..#|.##.",
  "P": "###.|#..#|#..#|###.|#...|#...|#...",
  "Q": ".##.|#..#|#..#|#..#|#..#|#.#.|.#.#",
  "R": "###.|#..#|#..#|###.|#.#.|#..#|#..#",
  "S": ".###|#...|#...|.##.|...#|...#|###.",
  "T": "#####|..#..|..#..|..#..|..#..|..#..|..#..",
  "U": "#..#|#..#|#..#|#..#|#..#|#..#|.##.",
  "V": "#...#|#...#|#...#|#...#|.#.#.|.#.#.|..#..",
  "W": "#...#|#...#|#...#|#.#.#|#.#.#|##.##|#...#",
  "X": "#...#|#...#|.#.#.|..#..|.#.#.|#...#|#...#",
  "Y": "#...#|#...#|.#.#.|..#..|..#..|..#..|..#..",
  "Z": "####|...#|..#.|..#.|.#..|#...|####",
  "a": "....|....|.##.|...#|.###|#..#|.###",
  "b": "#...|#...|###.|#..#|#..#|#..#|###.",
  "c": "...|...|.##|#..|#..|#..|.##",
  "d": "...#|...#|.###|#..#|#..#|#..#|.###",
  "e": "....|....|.##.|#..#|####|#...|.##.",
  "f": ".##|#..|#..|###|#..|#..|#..",
  "g": "....|....|.###|#..#|#..#|#..#|.###|...#|.##.",
  "h": "#...|#...|###.|#..#|#..#|#..#|#..#",
  "i": "#|.|#|#|#|#|#",
  "j": ".#|..|.#|.#|.#|.#|.#|.#|#.",
  "k": "#..|#..|#.#|#.#|##.|#.#|#.#",
  "l": "#.|#.|#.|#.|#.|#.|.#",
  "m": ".....|.....|####.|#.#.#|#.#.#|#.#.#|#.#.#",
  "n": "....|....|###.|#..#|#..#|#..#|#..#",
  "o": "....|....|.##.|#..#|#..#|#..#|.##.",
  "p": "....|....|###.|#..#|#..#|#..#|###.|#...|#...",
  "q": "....|....|.###|#..#|#..#|#..#|.###|...#|...#",
  "r": "...|...|#.#|##.|#..|#..|#..",
  "s": "....|....|.###|#...|.##.|...#|###.",
  "t": ".#.|.#.|###|.#.|.#.|.#.|..#",
  "u": "....|....|#..#|#..#|#..#|#..#|.###",
  "v": "...|...|#.#|#.#|#.#|#.#|.#.",
  "w": ".....|.....|#...#|#...#|#.#.#|#.#.#|.#.#.",
  "x": "...|...|#.#|#.#|.#.|#.#|#.#",
  "y": "....|....|#..#|#..#|#..#|#..#|.###|...#|.##.",
  "z": "....|....|####|...#|.##.|#...|####",
};

// "sins" is the small HUD font; "absolute" is the chunky title font, made by
// thickening the same glyphs and doubling their top, middle and bottom rows.
const FONTS = {
  sins: { rows: [0, 1, 2, 3, 4, 5, 6, 7, 8], bold: 0, gap: 1, height: 7 },
  absolute: { rows: [0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8], bold: 1, gap: 2, height: 10 },
};

const glyphRows = {};
for (const [ch, src] of Object.entries(GLYPHS)) glyphRows[ch] = src.split("|");

function rowsFor(ch) {
  return glyphRows[ch] || glyphRows[ch.toUpperCase()] || glyphRows["?"];
}

function ctxOf(canvas) {
  if (!canvas._ctx) {
    canvas._ctx = canvas.getContext("2d");
    canvas._ctx.imageSmoothingEnabled = false;
  }
  return canvas._ctx;
}

const glyphCache = new Map();

function glyphCanvas(fontName, css, ch) {
  const key = fontName + "\u0000" + css + "\u0000" + ch;
  let c = glyphCache.get(key);
  if (c) return c;
  const font = FONTS[fontName] || FONTS.sins;
  const rows = rowsFor(ch);
  const w = rows[0].length;
  c = document.createElement("canvas");
  c.width = w + font.bold;
  c.height = font.rows.length;
  const g = ctxOf(c);
  g.fillStyle = css;
  font.rows.forEach((src, y) => {
    const row = rows[src] || "";
    for (let x = 0; x < row.length; x++) {
      if (row[x] === "#") g.fillRect(x, y, 1 + font.bold, 1);
    }
  });
  glyphCache.set(key, c);
  return c;
}

function advance(font, ch) {
  return rowsFor(ch)[0].length + font.bold + font.gap;
}

// Drawing ------------------------------------------------------------------
const Shim = {
  images: {},

  newCanvas(w, h) {
    const c = document.createElement("canvas");
    c.width = Math.max(1, w | 0);
    c.height = Math.max(1, h | 0);
    return c;
  },

  loadedImage(path) {
    const name = String(path).split("/").pop();
    const c = Shim.images[name];
    if (!c) throw new Error("image not preloaded: " + path);
    return c;
  },

  fillRect(canvas, css, x, y, w, h) {
    const g = ctxOf(canvas);
    g.fillStyle = css;
    g.fillRect(Math.floor(x), Math.floor(y), Math.round(w), Math.round(h));
  },

  clear(canvas, css, x, y, w, h) {
    const g = ctxOf(canvas);
    g.clearRect(x, y, w, h);
    g.fillStyle = css;
    g.fillRect(x, y, w, h);
  },

  // A negative width or height mirrors the sprite in place, like the firmware.
  blit(dst, src, sx, sy, sw, sh, dx, dy, dw, dh) {
    const g = ctxOf(dst);
    dx = Math.floor(dx);
    dy = Math.floor(dy);
    const w = Math.abs(dw);
    const h = Math.abs(dh);
    if (dw >= 0 && dh >= 0) {
      g.drawImage(src, sx, sy, sw, sh, dx, dy, w, h);
      return;
    }
    g.save();
    g.translate(dx + (dw < 0 ? w : 0), dy + (dh < 0 ? h : 0));
    g.scale(dw < 0 ? -1 : 1, dh < 0 ? -1 : 1);
    g.drawImage(src, sx, sy, sw, sh, 0, 0, w, h);
    g.restore();
  },

  text(canvas, fontName, css, msg, x, y) {
    const font = FONTS[fontName] || FONTS.sins;
    const g = ctxOf(canvas);
    let cx = Math.floor(x);
    const cy = Math.floor(y);
    for (const ch of String(msg)) {
      if (ch !== " ") g.drawImage(glyphCanvas(fontName, css, ch), cx, cy);
      cx += advance(font, ch);
    }
  },

  measureWidth(fontName, msg) {
    const font = FONTS[fontName] || FONTS.sins;
    let w = 0;
    for (const ch of String(msg)) w += advance(font, ch);
    return w ? w - font.gap : 0;
  },

  fontHeight(fontName) {
    return (FONTS[fontName] || FONTS.sins).height;
  },
};

// Input --------------------------------------------------------------------
// Bit values match BUTTON_* in badge_shim.py.
const UP = 1, DOWN = 2, LEFT = 4, RIGHT = 8, SELECT = 16, BACK = 32, MENU = 64, HOME = 128;

const KEYS = {
  ArrowUp: UP, KeyW: UP,
  ArrowDown: DOWN, KeyS: DOWN,
  ArrowLeft: LEFT, KeyA: LEFT,
  ArrowRight: RIGHT, KeyD: RIGHT,
  KeyX: SELECT, Space: SELECT, KeyK: SELECT,
  KeyZ: BACK, KeyY: BACK, ShiftLeft: BACK, ShiftRight: BACK, KeyJ: BACK,
  Enter: MENU, Escape: MENU, KeyP: MENU,
};

// Standard gamepad layout: bottom face button jumps, left face button runs.
const PAD_BUTTONS = [[0, SELECT], [2, BACK], [1, BACK], [9, MENU], [12, UP], [13, DOWN], [14, LEFT], [15, RIGHT]];

const keysDown = new Set();
let latched = 0; // buttons tapped and released between two frames
let prevHeld = 0;
let touchHeld = 0; // buttons held on the touch pad

function keyMask() {
  let m = 0;
  for (const code of keysDown) m |= KEYS[code];
  return m;
}

// Set by badge_shim.run() to the app's on_exit(), which saves the high score.
// It only saves a better score, so calling it more than once is harmless.
Shim.exitHook = null;

function runExitHook() {
  if (!Shim.exitHook) return;
  try {
    Shim.exitHook();
  } catch (err) {
    console.error(err);
  }
}

// Home quits the app on the badge; here it restarts at the title screen.
const QUIT_KEYS = new Set(["Home", "KeyQ"]);

addEventListener("keydown", (e) => {
  if (QUIT_KEYS.has(e.code) && !e.metaKey && !e.ctrlKey) {
    runExitHook();
    location.reload();
    return;
  }
  const bit = KEYS[e.code];
  if (!bit || e.metaKey || e.ctrlKey || e.altKey) return;
  e.preventDefault();
  if (e.repeat) return;
  keysDown.add(e.code);
  latched |= bit;
});
addEventListener("keyup", (e) => {
  if (KEYS[e.code]) keysDown.delete(e.code);
  // macOS sends no keyup for keys released while Cmd is down, so they would
  // stay held.
  if (e.key === "Meta") keysDown.clear();
});

// Forget every held key and touch button when the page loses focus or is
// hidden; their release events may never arrive.
function releaseAll() {
  keysDown.clear();
  touchHeld = 0;
  for (const el of document.querySelectorAll("[data-button].down")) el.classList.remove("down");
}
addEventListener("blur", releaseAll);
addEventListener("pagehide", () => {
  releaseAll();
  runExitHook();
});
document.addEventListener("visibilitychange", () => {
  if (document.hidden) releaseAll();
});

// getGamepads() throws a SecurityError in an iframe without the gamepad
// permission; play on without a gamepad then.
let gamepadsAllowed = !!navigator.getGamepads;

function padMask() {
  let m = 0;
  let pads = [];
  if (gamepadsAllowed) {
    try {
      pads = navigator.getGamepads();
    } catch (err) {
      gamepadsAllowed = false;
    }
  }
  for (const pad of pads) {
    if (!pad) continue;
    for (const [i, bit] of PAD_BUTTONS) if (pad.buttons[i] && pad.buttons[i].pressed) m |= bit;
    const [ax, ay] = pad.axes;
    if (ax < -0.5) m |= LEFT;
    if (ax > 0.5) m |= RIGHT;
    if (ay < -0.5) m |= UP;
    if (ay > 0.5) m |= DOWN;
  }
  return m;
}

// Touch buttons on the page carry data-button="UP" and so on.
const touchBits = { UP, DOWN, LEFT, RIGHT, SELECT, BACK, MENU };
function bindTouch(root) {
  for (const el of root.querySelectorAll("[data-button]")) {
    const bit = touchBits[el.dataset.button];
    const on = (e) => { e.preventDefault(); touchHeld |= bit; latched |= bit; el.classList.add("down"); };
    const off = (e) => { e.preventDefault(); touchHeld &= ~bit; el.classList.remove("down"); };
    el.addEventListener("pointerdown", on);
    el.addEventListener("pointerup", off);
    el.addEventListener("pointercancel", off);
    el.addEventListener("pointerleave", off);
  }
}

Shim.bindTouch = bindTouch;
Shim.held = 0;
Shim.pressed = 0;
Shim.released = 0;

Shim.beginFrame = function () {
  const held = keyMask() | padMask() | touchHeld;
  Shim.pressed = (held & ~prevHeld) | latched;
  Shim.released = prevHeld & ~held;
  Shim.held = held;
  prevHeld = held;
  latched = 0;
};

// Main loop ----------------------------------------------------------------
Shim.start = function (tick) {
  const loop = (now) => {
    try {
      tick(now);
    } catch (err) {
      window.showError(String((err && err.message) || err));
      return;
    }
    requestAnimationFrame(loop);
  };
  requestAnimationFrame(loop);
};

window.SuperMonaShim = Shim;
