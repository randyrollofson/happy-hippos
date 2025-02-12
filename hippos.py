import colors

bg = colors.bg
ol = colors.ol
c1 = colors.c1
c2 = colors.c2
c3 = colors.c3
c4 = colors.c4
c5 = colors.c5
ey = colors.ey
p1 = colors.p1
p2 = colors.p2


hippo_basic = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, c3, c2, ol, ol, ol, ol, ol, ol, ol, ol, ol, c3, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, c1, c1, c2, c2, c2, c2, c2, c2, c2, c2, c3, c1, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, c1, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

hippo_two_teeth = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, c3, c2, ol, ol, ol, ol, ol, ol, ol, ol, ol, c3, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, c1, c1, ol, ey, ol, c2, c2, c2, ol, ey, ol, c1, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, ol, ol, ol, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, c1, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

hippo_six_teeth = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, ol, ey, ol, ol, ol, ol, ol, ol, ol, ol, ol, ey, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, ol, ol, ol, ey, ol, ey, ol, ey, ol, ey, ol, ol, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, ol, ol, ol, ol, ol, ol, ol, ol, ol, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, c1, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

hippo_smile = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, ol, ey, ol, ol, ol, ol, ol, ol, ol, ol, ol, ey, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, ol, ol, ol, p1, p1, p1, p1, p1, p1, p1, ol, ol, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, ol, ol, p2, p2, p2, p2, p2, ol, ol, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, ol, ol, ol, ol, ol, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

hippo_tongue_out = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, c3, c2, ol, ol, ol, ol, ol, ol, ol, ol, ol, c3, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, c1, c1, c2, c2, ol, p1, p1, p1, p1, ol, c3, c1, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, c1, c1, c1, ol, p2, p2, ol, c1, c1, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, ol, ol, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

hippo_lick = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
    [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
    [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
    [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
    [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, ol, ol, c1, c1, c4, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, ol, p2, p2, ol, c1, c1, c4, ol, bg, bg, bg, bg],
    [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, ol, p1, p1, p1, p1, ol, ol, c3, ol, bg, bg, bg, bg],
    [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, c3, c2, ol, ol, ol, ol, ol, ol, ol, ol, ol, c3, c2, ol, bg, bg, bg, bg],
    [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, c1, c1, c2, c2, c2, c2, c2, c2, c2, c2, c3, c1, ol, bg, bg, bg, bg, bg],
    [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, ol, bg, bg, bg, bg, bg],
    [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, c1, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
    [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]