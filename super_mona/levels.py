"""Original stages for Super Mona

Each factory returns a fresh Level so restarting a stage resets its blocks,
stars and enemies. Rows run 0 (top) to 14; ground tops sit on row 13.
"""

from game import Level


def scenery(level, hills=(), bushes=(), clouds=()):
    for x in hills:
        level.hill(x)
    for x in bushes:
        level.bush(x)
    for x, y in clouds:
        level.cloud(x, y)


def hello_world():
    lv = Level("1-1 HELLO WORLD", 190, "day", 300, switch=False)
    lv.ground(0, 68)
    lv.ground(71, 85)
    lv.ground(89, 150)
    lv.ground(153, 189)
    scenery(lv,
            hills=(0, 40, 92, 140, 178),
            bushes=(9, 33, 60, 104, 130, 157),
            clouds=((6, 3), (24, 2), (47, 4), (70, 3), (96, 2), (118, 4),
                    (146, 3), (166, 2)))

    lv.row(12, 9, "Q")
    lv.row(18, 9, "B-B")
    lv.block(19, 9, "chip")
    lv.star_line(18, 5, 3)
    lv.enemy(24)
    lv.pipe(28, 2)
    lv.enemy(33)
    lv.pipe(38, 3)
    lv.enemy(44)
    lv.enemy(46)
    lv.pipe(52, 4)
    lv.star_line(57, 10, 4)
    lv.enemy(63, "shellbot")

    lv.star_line(68, 9, 4)
    lv.row(74, 9, "BB-BB")
    lv.block(76, 9, "multi6", brick=True)
    lv.block(78, 5, "1up", brick=True)
    lv.enemy(81, "shellbot")

    lv.star_line(86, 8, 3)
    lv.row(92, 9, "QQQ")
    lv.enemy(96)
    lv.enemy(98)
    lv.row(100, 9, "BBBBBB")
    lv.block(103, 5, "sparkle")
    lv.star_line(100, 4, 3)
    lv.enemy(108, "shellbot")
    lv.enemy(112)
    lv.enemy(114)

    lv.stairs(120, 4)
    lv.stairs(124, 4, up=False)
    lv.enemy(132)
    lv.pipe(138, 2)
    lv.row(144, 9, "Q", "chip")
    lv.star_line(150, 8, 4)
    lv.enemy(157)
    lv.enemy(159)
    lv.stairs(161, 7)
    lv.flag(176)
    return lv


def server_room():
    lv = Level("1-2 SERVER ROOM", 165, "cave", 300, switch=True)
    lv.ground(0, 39)
    lv.ground(43, 77)
    lv.ground(81, 103)
    lv.ground(107, 164)
    lv.ceiling(0, 150)

    lv.row(10, 9, "QQQ")
    lv.block(13, 9, "chip")
    lv.enemy(18)
    lv.enemy(20)
    for y in (10, 11, 12):
        lv.row(26, y, "BB")
    lv.row(32, 8, "BBBBBB")
    lv.star_line(33, 7, 4)
    lv.star_line(40, 9, 3)

    lv.enemy(46, "shellbot")
    lv.enemy(50)
    lv.enemy(52)
    lv.row(56, 9, "BB-BB")
    lv.block(58, 9, "sparkle")
    lv.row(56, 5, "BBBBB")
    lv.pipe(66, 3)
    lv.enemy(70)
    lv.pipe(72, 2)
    lv.star_line(78, 9, 3)

    lv.row(84, 9, "BBBBBBBB")
    lv.row(84, 5, "BBBBBBBB")
    lv.block(88, 9, "multi8", brick=True)
    lv.star_line(85, 7, 6)
    lv.enemy(94)
    lv.enemy(96)
    lv.enemy(99, "shellbot")
    lv.star_line(104, 9, 3)

    lv.stairs(112, 4)
    lv.row(122, 9, "Q", "1up")
    lv.enemy(128)
    lv.enemy(130)
    lv.row(134, 9, "Q", "chip")
    lv.stairs(140, 6)
    lv.flag(152)
    return lv


def sky_bridge():
    lv = Level("1-3 SKY BRIDGE", 175, "dusk", 300, switch=True)
    lv.ground(0, 20)
    lv.ground(33, 50)
    lv.ground(72, 95)
    lv.ground(100, 120)
    lv.ground(127, 174)
    scenery(lv,
            hills=(2, 36, 76, 130, 165),
            bushes=(12, 45, 88, 110, 140),
            clouds=((8, 3), (28, 2), (52, 4), (80, 2), (108, 3), (136, 2),
                    (156, 4)))

    lv.row(10, 9, "QBQ")
    lv.enemy(15)
    lv.row(24, 10, "======")
    lv.star_line(24, 9, 6)

    lv.pipe(38, 3)
    lv.enemy(42, "shellbot")
    lv.row(44, 9, "BQB", "chip")
    lv.enemy(47)

    lv.row(54, 10, "====")
    lv.row(60, 8, "====")
    lv.row(66, 10, "====")
    lv.star_line(60, 7, 4)
    lv.enemy(62, "bug", y=7)

    lv.enemy(78)
    lv.enemy(80)
    lv.enemy(83, "shellbot")
    lv.row(86, 9, "Q", "sparkle")
    lv.stairs(90, 3)
    lv.row(97, 11, "==")

    lv.row(104, 9, "BB-BB")
    lv.block(106, 9, "multi6", brick=True)
    lv.enemy(108)
    lv.enemy(110)
    lv.pipe(114, 4)
    lv.row(122, 9, "====")
    lv.star_line(122, 8, 4)

    lv.enemy(132, "shellbot")
    lv.enemy(134)
    lv.enemy(136)
    lv.block(140, 9, "1up")
    lv.enemy(146)
    lv.stairs(150, 6)
    lv.flag(162)
    return lv


def firewall():
    """World 1 castle: low ceiling, pits bridged by girders, dense blocks."""
    lv = Level("1-4 FIREWALL", 150, "castle", 300, switch=True)
    lv.ground(0, 14, top=10)
    lv.ground(15, 30)
    lv.ground(34, 52)
    lv.ground(57, 80)
    lv.ground(84, 110)
    lv.ground(114, 149)
    lv.ceiling(0, 134, rows=(1, 2))
    lv.start = (2, 9)

    lv.row(17, 9, "Q", "chip")
    lv.enemy(22)
    lv.row(24, 6, "HHHHHH")
    lv.star_line(31, 10, 3)

    lv.enemy(38)
    lv.enemy(40)
    lv.row(42, 9, "BQB", "sparkle")
    lv.stairs(48, 3)
    lv.row(53, 11, "===")

    lv.row(60, 6, "HHHHHHHHHHHH")
    lv.row(62, 9, "BBBB")
    lv.block(64, 9, "multi8", brick=True)
    lv.enemy(68, "shellbot")
    lv.enemy(74)
    lv.enemy(76)
    lv.star_line(81, 10, 3)

    lv.pipe(88, 2)
    lv.enemy(93)
    lv.enemy(95)
    lv.row(98, 9, "Q", "1up")
    lv.stairs(104, 4)
    lv.row(111, 11, "==")

    lv.enemy(118, "shellbot")
    lv.enemy(122)
    lv.stairs(126, 5)
    lv.flag(138)
    return lv


def pull_request():
    """World 2 overworld: pipes in pairs, long block rows and stair pits."""
    lv = Level("2-1 PULL REQUEST", 185, "day", 300, switch=True)
    lv.ground(0, 45)
    lv.ground(48, 98)
    lv.ground(102, 132)
    lv.ground(135, 184)
    scenery(lv,
            hills=(0, 50, 104, 150),
            bushes=(14, 38, 66, 90, 120, 168),
            clouds=((8, 2), (30, 4), (58, 2), (84, 3), (112, 2), (140, 4),
                    (164, 3)))

    lv.row(8, 9, "BQB", "chip")
    lv.row(14, 9, "QQ")
    lv.enemy(18)
    lv.enemy(20)
    lv.pipe(24, 2)
    lv.pipe(30, 3)
    lv.enemy(34, "shellbot")
    lv.row(38, 5, "BBQBB", "sparkle")
    lv.star_line(38, 4, 5)
    lv.star_line(45, 9, 3)

    lv.stairs(52, 3)
    lv.stairs(55, 3, up=False)
    lv.enemy(60)
    lv.enemy(62)
    lv.enemy(64)
    lv.row(68, 9, "BBBBBBBB")
    lv.block(71, 9, "multi6", brick=True)
    lv.row(70, 5, "Q", "1up")
    lv.pipe(80, 4)
    lv.enemy(85, "shellbot")
    lv.pipe(90, 2)
    lv.star_line(98, 9, 4)

    lv.row(104, 9, "QBQBQ")
    lv.enemy(108)
    lv.enemy(110)
    lv.stairs(116, 4)
    lv.row(124, 9, "Q", "chip")
    lv.star_line(131, 8, 4)

    lv.enemy(140, "shellbot")
    lv.enemy(144)
    lv.enemy(146)
    lv.pipe(150, 3)
    lv.stairs(158, 8)
    lv.flag(172)
    return lv


def stack_overflow():
    """World 2 underground: brick towers, tight corridors and a pipe maze."""
    lv = Level("2-2 OVERFLOW", 160, "cave", 300, switch=True)
    lv.ground(0, 34)
    lv.ground(38, 70)
    lv.ground(74, 112)
    lv.ground(116, 159)
    lv.ceiling(0, 145)

    lv.row(8, 9, "QQQQ")
    lv.block(9, 9, "chip")
    lv.enemy(14)
    for i, h in enumerate((1, 2, 3, 4)):
        for y in range(13 - h, 13):
            lv.row(18 + i * 3, y, "B")
    lv.star_line(18, 7, 10)
    lv.enemy(30)
    lv.star_line(35, 9, 3)

    lv.row(42, 6, "BBBBBBBBBB")
    lv.row(42, 9, "B-B-BQB", "sparkle")
    lv.enemy(46)
    lv.enemy(48)
    lv.enemy(52, "shellbot")
    lv.pipe(58, 2)
    lv.pipe(62, 3)
    lv.pipe(66, 4)
    lv.star_line(71, 8, 3)

    lv.row(78, 9, "BBBBBB")
    lv.row(78, 5, "BBBBBB")
    lv.block(80, 5, "1up", brick=True)
    lv.star_line(78, 7, 6)
    lv.enemy(88)
    lv.enemy(90)
    lv.enemy(92)
    lv.stairs(98, 4)
    lv.stairs(102, 4, up=False)
    lv.star_line(113, 9, 3)

    lv.row(120, 9, "Q", "chip")
    lv.enemy(124, "shellbot")
    lv.enemy(128)
    lv.stairs(134, 6)
    lv.flag(148)
    return lv


def cloud_deploy():
    """World 2 athletic stage: girder hops high above the clouds."""
    lv = Level("2-3 CLOUD DEPLOY", 175, "cloud", 300, switch=True)
    lv.ground(0, 14)
    lv.ground(46, 56)
    lv.ground(98, 108)
    lv.ground(135, 174)
    scenery(lv,
            hills=(2, 144),
            bushes=(8, 50, 102, 156),
            clouds=((10, 8), (22, 3), (36, 10), (60, 2), (76, 9), (92, 3),
                    (116, 10), (130, 4)))

    lv.row(8, 9, "Q", "chip")
    lv.row(17, 11, "=========")
    lv.row(29, 10, "========")
    lv.star_line(30, 9, 6)
    lv.enemy(33, "bug", y=9)
    lv.row(40, 11, "======")

    lv.row(48, 9, "BQB", "sparkle")
    lv.enemy(52)
    lv.row(59, 11, "=========")
    lv.row(71, 10, "========")
    lv.star_line(72, 9, 6)
    lv.enemy(75, "bug", y=9)
    lv.row(82, 8, "Q", "1up")
    lv.row(83, 11, "============")

    lv.enemy(102, "shellbot")
    lv.row(111, 11, "=========")
    lv.row(123, 10, "=======")
    lv.star_line(124, 9, 5)
    lv.enemy(127, "bug", y=9)
    lv.star_line(133, 7, 3)

    lv.row(144, 9, "QBQ", "chip")
    lv.enemy(148)
    lv.enemy(150)
    lv.stairs(152, 6)
    lv.flag(164)
    return lv


def merge_conflict():
    """World 2 castle: the final stage, longer pits and more shellbots."""
    lv = Level("2-4 CONFLICT", 165, "castle", 300, switch=True)
    lv.ground(0, 14, top=10)
    lv.ground(15, 28)
    lv.ground(32, 46)
    lv.ground(51, 66)
    lv.ground(71, 92)
    lv.ground(96, 120)
    lv.ground(125, 164)
    lv.ceiling(0, 150, rows=(1, 2))
    lv.start = (2, 9)

    lv.row(18, 9, "Q", "chip")
    lv.enemy(22, "shellbot")
    lv.row(24, 6, "HHHH")
    lv.star_line(29, 10, 3)

    lv.enemy(35)
    lv.enemy(37)
    lv.row(38, 9, "BQB", "sparkle")
    lv.stairs(42, 3)
    lv.row(47, 11, "===")

    lv.row(54, 6, "HHHHHHHHHH")
    lv.row(56, 9, "BBBB")
    lv.block(57, 9, "multi8", brick=True)
    lv.enemy(60, "shellbot")
    lv.enemy(63)
    lv.row(67, 11, "===")

    lv.pipe(74, 3)
    lv.enemy(79)
    lv.enemy(81)
    lv.enemy(83, "shellbot")
    lv.row(86, 9, "Q", "1up")
    lv.stairs(88, 4)
    lv.star_line(93, 9, 3)

    lv.enemy(100)
    lv.enemy(102)
    lv.row(104, 6, "HHHHHHHH")
    lv.enemy(110, "shellbot")
    lv.stairs(114, 4)
    lv.row(121, 11, "===")

    lv.enemy(130)
    lv.enemy(132)
    lv.enemy(134, "shellbot")
    lv.stairs(138, 6)
    lv.flag(152)
    return lv


# Worlds 3-8 ----------------------------------------------------------------
# Built from small original segments so 24 stages stay light on badge RAM.
# Each world runs overworld, underground, sky, castle; k (0-5) raises the
# difficulty with wider pits and more enemies.

ITEMS = ("chip", "sparkle", "chip", "1up", "multi6")


class _Rand:
    def __init__(self, seed):
        self.s = seed

    def __call__(self, n):
        self.s = (self.s * 1103515245 + 12345) & 0x7FFFFFFF
        return (self.s >> 16) % n


def _flat(lv, x, k, r):
    lv.ground(x, x + 9)
    lv.star_line(x + 2, 9, 3)
    lv.enemy(x + 4 + r(3))
    if k > 2:
        lv.enemy(x + 8)
    return x + 10


def _pipes(lv, x, k, r):
    lv.ground(x, x + 15)
    lv.pipe(x + 2, 2 + r(2))
    lv.enemy(x + 6)
    lv.pipe(x + 9, 3 + r(2))
    if k > 1:
        lv.enemy(x + 13, "shellbot")
    return x + 16


def _blocks(lv, x, k, r):
    lv.ground(x, x + 13)
    lv.row(x + 2, 9, "BQBBB")
    lv.block(x + 5, 9, ITEMS[r(len(ITEMS))])
    if r(2):
        lv.block(x + 4, 5, "multi6", brick=True)
    else:
        lv.star_line(x + 3, 5, 3)
    lv.enemy(x + 9)
    lv.enemy(x + 11)
    return x + 14


def _pit(lv, x, k, r):
    w = 2 + min(2, (k + r(2)) // 2)
    lv.star_line(x, 9, w)
    lv.ground(x + w, x + w + 3)
    return x + w + 4


def _stairs(lv, x, k, r):
    h = 3 + min(1, k // 2)
    lv.ground(x, x + h)
    lv.stairs(x + 1, h)
    x2 = x + h + 1 + (2 if k >= 2 else 0)
    lv.ground(x2, x2 + h + 2)
    lv.stairs(x2, h, up=False)
    lv.enemy(x2 + h + 1)
    return x2 + h + 3


def _swarm(lv, x, k, r):
    lv.ground(x, x + 13)
    lv.row(x + 4, 8, "Q", "1up" if r(4) == 0 else "chip")
    lv.enemy(x + 3)
    lv.enemy(x + 5)
    lv.enemy(x + 8, "shellbot")
    if k >= 2:
        lv.enemy(x + 11)
    return x + 14


def _towers(lv, x, k, r):
    lv.ground(x, x + 15)
    for i in range(4):
        for y in range(12 - i, 13):
            lv.row(x + 1 + i * 3, y, "B")
    lv.star_line(x + 1, 7, 10)
    lv.enemy(x + 14)
    return x + 16


def _corridor(lv, x, k, r):
    lv.ground(x, x + 11)
    lv.row(x + 1, 9, "BBBBBBBB")
    lv.row(x + 1, 5, "BBBBBBBB")
    lv.block(x + 3 + r(4), 9, ITEMS[r(len(ITEMS))], brick=True)
    lv.star_line(x + 2, 7, 6)
    lv.enemy(x + 10)
    return x + 12


def _hops(lv, x, k, r):
    lv.row(x + 2, 11, "=" * 9)
    lv.row(x + 14, 10, "=" * 8)
    lv.star_line(x + 15, 9, 6)
    lv.enemy(x + 18, "bug", y=9)
    lv.row(x + 25, 11, "=" * 6)
    return x + 34


def _bridge(lv, x, k, r):
    lv.row(x + 1, 11, "===")
    lv.star_line(x + 1, 8, 3)
    lv.ground(x + 5, x + 10)
    lv.enemy(x + 8)
    return x + 11


def _roof(lv, x, k, r):
    lv.ground(x, x + 15)
    lv.row(x + 2, 6, "H" * 10)
    lv.row(x + 4, 9, "BBBB")
    lv.block(x + 5, 9, "multi8" if r(2) else "sparkle", brick=True)
    lv.enemy(x + 8, "shellbot")
    lv.enemy(x + 12)
    return x + 16


SEGMENTS = {
    "f": _flat, "p": _pipes, "b": _blocks, "g": _pit, "s": _stairs,
    "w": _swarm, "t": _towers, "c": _corridor, "h": _hops, "x": _bridge,
    "r": _roof,
}


def _build(name, theme, plan, k, seed, width):
    lv = Level(name, width, theme, 300, switch=True)
    r = _Rand(seed)
    lv.ground(0, 9)
    lv.row(5, 9, "Q", "chip")
    x = 10
    for code in plan:
        x = SEGMENTS[code](lv, x, k, r)
    lv.ground(x, x + 23)
    lv.stairs(x + 2, 6)
    lv.flag(x + 14)
    end = x + 24
    if theme == "cave":
        lv.ceiling(0, x + 13)
    elif theme == "castle":
        lv.ceiling(0, x + 13, rows=(1, 2))
    else:
        for hx in range(0, end - 3, 37):
            if lv.solid(hx, 13) and lv.solid(hx + 2, 13):
                lv.hill(hx)
        for bx in range(9, end - 3, 23):
            if lv.solid(bx, 13) and lv.solid(bx + 2, 13) and not lv.solid(bx + 1, 12):
                lv.bush(bx)
        for i, cx in enumerate(range(6, end - 3, 21)):
            lv.cloud(cx, 2 + i % 3)
    return lv, end


def _stage(name, theme, plan, k, seed):
    def factory():
        _, width = _build(name, theme, plan, k, seed, 200)
        return _build(name, theme, plan, k, seed, width)[0]
    return factory


_WORLDS = (
    (("CLONE", "FORK", "PUSH", "PULL"),
     ("day", "cave", "cloud", "castle"),
     ("bpgwsbgp", "cgtwcgs", "bhwh", "rxwrxs")),
    (("ACTION", "TRIGGER", "PRE-PROD", "PROD"),
     ("day", "cave", "dusk", "castle"),
     ("pgpbwgsp", "tcgwtcs", "fhbhw", "xrwxrs")),
    (("BUG BASH", "STACK TRACE", "BREAKPOINT", "SEGFAULT"),
     ("dusk", "cave", "cloud", "castle"),
     ("wbgpswgb", "ctgwcts", "hwbh", "rxwxrws")),
    (("CONTAINER", "KERNEL PANIC", "EDGE CACHE", "DEADLOCK"),
     ("day", "cave", "dusk", "castle"),
     ("pbgwpgsw", "tcwgtcgs", "bhwhf", "xrxwrxs")),
    (("CLONE", "STASH", "PR", "MERGE"),
     ("day", "cave", "cloud", "castle"),
     ("bgpwgsbpg", "cgtwcgts", "hbhw", "rxwrxws")),
    (("PLAN", "BUILD", "TEST", "SHIP-IT"),
     ("dusk", "cave", "dusk", "castle"),
     ("wpgbsgwpg", "tcgwctgs", "hwhbh", "xrwxrwxs")),
)

EXTRA = []
for _w, (_names, _themes, _plans) in enumerate(_WORLDS):
    for _s in range(4):
        EXTRA.append(_stage("%d-%d %s" % (_w + 3, _s + 1, _names[_s]),
                            _themes[_s], _plans[_s], _w, _w * 4 + _s + 7))

LEVELS = (hello_world, server_room, sky_bridge, firewall,
          pull_request, stack_overflow, cloud_deploy, merge_conflict) + tuple(EXTRA)
