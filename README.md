# QR Code & Barcode Generator

Library dan CLI Python untuk menghasilkan QR Code dan Code128 barcode dari link/URL.

## Fitur

- **QR Code (2D)** — bisa di-scan dengan smartphone
- **Code128 (1D)** — barcode tradisional
- Output format: PNG atau SVG
- Bisa dipakai sebagai CLI maupun library (di-import)

## Instalasi

### Sebagai library (direkomendasikan)

```bash
pip install -e .
```

Setelah install, perintah `barcode-gen` tersedia langsung di terminal.

### Hanya dependensi

```bash
pip install -r requirements.txt
```

## Penggunaan

### CLI

#### Generate QR Code (default)
```bash
barcode-gen "https://github.com"
# atau
python make_barcode.py "https://github.com"
```

#### Generate Code128 Barcode
```bash
barcode-gen "https://github.com" -t code128
```

#### Semua Opsi

```
barcode-gen [LINK] [OPTIONS]

Argumen wajib:
  LINK                  URL atau teks yang akan dijadikan barcode

Opsi:
  -t, --type            Tipe barcode: qr (default) atau code128
  -o, --output          Nama file output tanpa ekstensi (default: barcode)
  --svg                 Output SVG untuk Code128 (default: PNG)
  --qr-box INT          Ukuran box QR (default: 10)
  --qr-border INT       Margin putih QR (default: 4)
```

#### Contoh

```bash
# QR Code dengan nama file custom
barcode-gen "https://github.com" -o my_qr

# QR Code dengan ukuran box dan border custom
barcode-gen "https://github.com" --qr-box 15 --qr-border 2

# Code128 output SVG
barcode-gen "123456789" -t code128 -o invoice --svg

# Code128 output PNG
barcode-gen "123456789" -t code128 -o invoice
```

### Sebagai Library

```python
from pathlib import Path
from barcode_gen import make_qr, make_code128

# Generate QR Code
make_qr("https://github.com", Path("output/my_qr"))

# Generate QR Code dengan ukuran custom
make_qr("https://github.com", Path("output/my_qr"), box_size=15, border=2)

# Generate Code128 PNG
make_code128("123456789", Path("output/invoice"))

# Generate Code128 SVG
make_code128("123456789", Path("output/invoice"), write_png=False)
```

## Struktur Paket

```
barcode_gen/
├── __init__.py    # ekspor make_qr, make_code128
├── qr.py          # logika QR Code
├── code128.py     # logika Code128
└── cli.py         # antarmuka command line
```

## Requirements

- Python 3.9+
- qrcode[pil] >= 7.0
- python-barcode >= 0.14.0
