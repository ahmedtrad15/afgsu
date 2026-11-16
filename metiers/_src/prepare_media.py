#!/usr/bin/env python3
"""Encode les photos et vidéos de l'archive dans metiers/NN-…/media/.

Usage : python3 metiers/_src/prepare_media.py /chemin/vers/archive-dezippee
        python3 metiers/_src/prepare_media.py --galerie /chemin/vers/afgsu-assets-dezippe

Photos : JPEG progressif, deux largeurs (-640 et -1200, ou la largeur source si plus petite).
Vidéos : MP4 H.264 720×1280, son AAC, démarrage rapide, plus une image d'aperçu (poster).
"""
import pathlib
import subprocess
import sys

from PIL import Image, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from media import FOLDERS, GALLERY, PHOTOS, VIDEOS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]


def site_dir(num):
    return next(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(num + "-"))


def photo(src, out_dir, stem):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    for w in (640, 1200):
        tw = min(w, im.width)
        th = round(im.height * tw / im.width)
        im.resize((tw, th), Image.LANCZOS).save(out_dir / f"{stem}-{w}.jpg", "JPEG",
                                                 quality=78, optimize=True, progressive=True)


def video(src, out_dir, stem):
    out = out_dir / f"{stem}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", "scale=720:-2",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "27", "-profile:v", "high",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart",
                    str(out)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.2", "-i", str(src), "-frames:v", "1",
                    "-vf", "scale=540:-2", "-q:v", "4", str(out_dir / f"{stem}-poster.jpg")], check=True)


def main(src_root):
    src_root = pathlib.Path(src_root)
    for num, folder in FOLDERS.items():
        out_dir = site_dir(num) / "media"
        out_dir.mkdir(exist_ok=True)
        for f, stem, _alt, _slot in PHOTOS[num]:
            photo(src_root / folder / f, out_dir, stem)
        f, stem, _t, _d = VIDEOS[num]
        video(src_root / folder / f, out_dir, stem)
        print("OK", out_dir.relative_to(ROOT), sum(p.stat().st_size for p in out_dir.iterdir()) // 1024, "Ko")


def gallery(src_root):
    src_root = pathlib.Path(src_root)
    for num, (_t, _i, items) in GALLERY.items():
        out_dir = site_dir(num) / "media"
        out_dir.mkdir(exist_ok=True)
        for f, stem, _alt, _cap in items:
            photo(src_root / f, out_dir, stem)
        print("OK galerie", out_dir.relative_to(ROOT))


if __name__ == "__main__":
    if sys.argv[1] == "--galerie":
        gallery(sys.argv[2])
    else:
        main(sys.argv[1])
