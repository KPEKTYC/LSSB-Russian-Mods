"""Draw docs/images/lively-before-after.png from the installed game and the built mod archive.

The same character layers are composed twice: the game's originals scaled x3 and the mod's
@2 layers scaled x1.5, both bilinear, as a window three times the game's size would show them.
Usage: python tools/make_lively_comparison.py <game folder> <localization .rpa>
"""
import io, pickle, sys, zlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

LAYERS = ["", "_bot_nopreg_palla_casual", "_top_nopreg_palla_casual", "_nohaircut"]
STEM = "dlc_lively/bg/coffeeshop/npc/palla/bg_coffeeshop_palla"
OUT = Path(__file__).resolve().parents[1] / "docs/images/lively-before-after.png"


class Archive:
    def __init__(self, path):
        self.file = open(path, "rb")
        head = self.file.readline().split()
        self.key = int(head[2], 16)
        self.file.seek(int(head[1], 16))
        self.index = pickle.loads(zlib.decompress(self.file.read()))

    def image(self, name):
        entry = self.index[name][0]
        self.file.seek(entry[0] ^ self.key)
        prefix = entry[2] if len(entry) > 2 and isinstance(entry[2], bytes) else b""
        return Image.open(io.BytesIO(prefix + self.file.read(entry[1] ^ self.key))).convert("RGBA")


def compose(archive, suffix):
    layers = [archive.image(STEM + layer + suffix) for layer in LAYERS]
    canvas = Image.new("RGBA", layers[0].size)
    for layer in layers:
        canvas.alpha_composite(layer)
    return canvas


def main(game, mod):
    original = compose(Archive(Path(game) / "dlc_lively.rpa"), ".webp")
    hd = compose(Archive(mod), "@2.webp")
    assert hd.size == (original.width * 2, original.height * 2), hd.size
    # Head and shoulders, in 1x game pixels.
    left, top = original.getbbox()[:2]
    box = (left + 40, top, left + 200, top + 150)
    panels = [original.crop(box).resize((480, 450), Image.BILINEAR),
              hd.crop(tuple(v * 2 for v in box)).resize((480, 450), Image.BILINEAR)]
    font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    sheet = Image.new("RGBA", (1000, 520), (214, 220, 226, 255))
    draw = ImageDraw.Draw(sheet)
    for x, panel, label in ((14, panels[0], "Оригинал, окно ×3"), (506, panels[1], "С модом: HD-слои")):
        sheet.alpha_composite(panel, (x, 56))
        draw.text((x + 240, 30), label, font=font, fill=(24, 44, 56), anchor="mm")
    sheet.convert("RGB").save(OUT, optimize=True)
    print(OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main(*sys.argv[1:3])
