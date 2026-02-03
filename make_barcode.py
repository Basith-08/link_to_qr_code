#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from pathlib import Path

def make_qr(data: str, out_path: Path, box_size: int = 10, border: int = 4):
    import qrcode
    # Config QR
    qr = qrcode.QRCode(
        version=None,              # auto fit
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,         # ukuran kotak dasar
        border=border              # margin putih
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()         # pakai PIL default (hitam-putih)
    out_path = out_path.with_suffix(".png")
    img.save(out_path)
    return out_path

def make_code128(data: str, out_path: Path, write_png: bool = True):
    # Code128 (1D) — bisa PNG (butuh pillow) atau SVG (tanpa pillow)
    import barcode
    from barcode.writer import ImageWriter

    code128 = barcode.get('code128', data)
    if write_png:
        out_path = out_path.with_suffix(".png")
        code128.write(out_path.open("wb"), writer=ImageWriter())
    else:
        out_path = out_path.with_suffix(".svg")
        code128.write(out_path.open("wb"))
    return out_path

def main():
    parser = argparse.ArgumentParser(
        description="Generate barcode dari link/URL (QR Code atau Code128)."
    )
    parser.add_argument("link", help="Link/URL yang akan dijadikan barcode")
    parser.add_argument(
        "-t", "--type",
        choices=["qr", "code128"],
        default="qr",
        help="Tipe barcode (default: qr)"
    )
    parser.add_argument(
        "-o", "--output",
        default="barcode",
        help="Nama file output tanpa ekstensi (default: barcode)"
    )
    parser.add_argument(
        "--png", action="store_true",
        help="Untuk Code128, paksa output PNG (default PNG). Jika tidak diset dan --svg digunakan, hasil SVG)."
    )
    parser.add_argument(
        "--svg", action="store_true",
        help="Untuk Code128, output SVG (abaikan untuk QR)."
    )
    parser.add_argument(
        "--qr-box", type=int, default=10,
        help="(QR) Ukuran box (default: 10)"
    )
    parser.add_argument(
        "--qr-border", type=int, default=4,
        help="(QR) Margin putih (default: 4)"
    )
    args = parser.parse_args()

    out_path = Path(os.getcwd()) / args.output

    if args.type == "qr":
        path = make_qr(args.link, out_path, box_size=args.qr_box, border=args.qr_border)
        print(f"QR Code berhasil dibuat: {path}")
    else:
        if args.svg:
            path = make_code128(args.link, out_path, write_png=False)
        else:
            path = make_code128(args.link, out_path, write_png=True)
        print(f"Code128 berhasil dibuat: {path}")

if __name__ == "__main__":
    main()
