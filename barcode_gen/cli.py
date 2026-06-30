import argparse
import os
from pathlib import Path

from .code128 import make_code128
from .qr import make_qr


def main():
    parser = argparse.ArgumentParser(
        description="Generate barcode dari link/URL (QR Code atau Code128)."
    )
    parser.add_argument("link", help="Link/URL yang akan dijadikan barcode")
    parser.add_argument(
        "-t", "--type",
        choices=["qr", "code128"],
        default="qr",
        help="Tipe barcode (default: qr)",
    )
    parser.add_argument(
        "-o", "--output",
        default="barcode",
        help="Nama file output tanpa ekstensi (default: barcode)",
    )
    parser.add_argument(
        "--svg", action="store_true",
        help="Untuk Code128, output SVG (abaikan untuk QR).",
    )
    parser.add_argument(
        "--qr-box", type=int, default=10,
        help="(QR) Ukuran box (default: 10)",
    )
    parser.add_argument(
        "--qr-border", type=int, default=4,
        help="(QR) Margin putih (default: 4)",
    )
    args = parser.parse_args()

    out_path = Path(os.getcwd()) / args.output

    if args.type == "qr":
        path = make_qr(args.link, out_path, box_size=args.qr_box, border=args.qr_border)
        print(f"QR Code berhasil dibuat: {path}")
    else:
        path = make_code128(args.link, out_path, write_png=not args.svg)
        print(f"Code128 berhasil dibuat: {path}")


if __name__ == "__main__":
    main()
