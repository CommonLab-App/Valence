# Rebuilds the ValenceLab wordmark in the four logos (SVG and PNG) and on the social card:
# "valence" in Bricolage Grotesque Bold, "lab" in ExtraBold and the accent colour. The drawn mark is kept as it is.
#
# The font is not in the repository. Get the variable font "BricolageGrotesque[opsz,wdth,wght].ttf"
# (Google Fonts, OFL), then, from the repository root:
#   python3 -m venv /tmp/logo-venv && /tmp/logo-venv/bin/pip install fonttools cairosvg pillow
#   /tmp/logo-venv/bin/python docs/media-kit/tools/build-logos.py <font.ttf> .
import sys, io, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
import cairosvg
from PIL import Image

FONT, REPO = sys.argv[1:3]
KIT = REPO + '/docs/media-kit'
_inst = {}
def inst(opsz, wght):
    k = (opsz, wght)
    if k not in _inst:
        _inst[k] = instantiateVariableFont(TTFont(FONT), {'opsz': opsz, 'wght': wght, 'wdth': 100})
    return _inst[k]

def run(text, opsz, wght, x, tracking):
    """[(x, path d)], next x, ink right edge — all in font units."""
    f = inst(opsz, wght); gs = f.getGlyphSet(); cmap = f.getBestCmap(); out = []; right = x
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs, ntos=lambda v: ('%.1f' % v).rstrip('0').rstrip('.')); gs[g].draw(pen)
        bp = BoundsPen(gs); gs[g].draw(bp)
        out.append((x, pen.getCommands())); right = x + bp.bounds[2]
        x += f['hmtx'][g][0] + tracking
    return out, x, right

def wordmark(opsz, tracking, scale, ink, accent):
    a, x, _ = run('valence', opsz, 700, 0, tracking)
    b, _, right = run('lab', opsz, 800, x, tracking)
    def grp(glyphs, fill):
        return '<g fill="%s">%s</g>' % (fill, ''.join(
            '<path transform="translate(%.2f,0) scale(%.5f,%.5f)" d="%s"/>' % (gx * scale, scale, -scale, d) for gx, d in glyphs))
    return grp(a, ink) + grp(b, accent), right * scale

def mark_of(svg):  # the drawn mark, kept exactly as it is in the existing file
    return re.search(r'<g transform="translate\(4,1\)"><g>.*?</g></g>', svg, re.S).group(0)

VARIANTS = {  # file suffix: (ink, accent for "lab")
    '': ('#17151c', '#c2185b'), '-on-dark': ('#fbf9fb', '#ff6fa3'),
    '-mono-black': ('#17151c', '#17151c'), '-mono-white': ('#ffffff', '#ffffff'),
}
for suffix, (ink, accent) in VARIANTS.items():
    path = '%s/logos/valence-logo%s.svg' % (KIT, suffix)
    word, w = wordmark(14, -21, 0.074, ink, accent)
    W = round(128 + w + 13, 1)  # same 13-unit margin as on the left
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s 112" width="%d" height="336">%s'
           '<g transform="translate(128,80.4)">%s</g></svg>\n' % (W, round(W * 3), mark_of(open(path).read()), word))
    open(path, 'w').write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=path[:-4] + '.png', output_height=645, output_width=round(645 * W / 112))
    print(path, 'viewBox width', W)

# Social card: the old word is painted out and the new one set at the same place, size and optical size.
card = Image.open(KIT + '/valence-social-card.png').convert('RGB')
BG = (251, 249, 251); assert card.getpixel((600, 150)) == BG and card.getpixel((1000, 320)) == BG
size = 85 / 695  # px per font unit: the old cap height was 85 px, 695 units at optical size 96
word, w = wordmark(96, 0, size, '#17151c', '#c2185b')
f = inst(96, 700); bp = BoundsPen(f.getGlyphSet()); f.getGlyphSet()[f.getBestCmap()[ord('v')]].draw(bp)
x0 = 349 - bp.bounds[0] * size  # the old word's ink began at x = 349; its baseline was y = 297
assert x0 + w < 1000, 'word runs into the screenshot'
layer = cairosvg.svg2png(bytestring=('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1260">'
                                     '<g transform="translate(%.2f,297)">%s</g></svg>' % (x0, word)).encode())
card.paste(BG, (335, 195, 1010, 335))
layer = Image.open(io.BytesIO(layer)); card.paste(layer, (0, 0), layer)
for dest in (KIT + '/valence-social-card.png', KIT + '/web/social-card.png', REPO + '/public/social-card.png'):
    card.save(dest, optimize=True)
print('card word ends at x =', round(x0 + w))
