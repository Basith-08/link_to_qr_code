# QR Code & Barcode Generator

Script Python untuk menghasilkan QR Code dan Code128 barcode dari link/URL.

## Fitur

- **QR Code (2D)** - Barcode 2D modern, bisa scan dengan smartphone
- **Code128 (1D)** - Barcode tradisional
- Output format: PNG atau SVG
- Customizable ukuran dan margin

## Instalasi

```bash
pip install -r requirements.txt
```

## Penggunaan

### Generate QR Code (default)
```bash
python make_barcode.py "https://github.com"
```

### Generate Code128 Barcode
```bash
python make_barcode.py "https://github.com" -t code128
```

### Pilihan Parameter

```bash
python make_barcode.py [LINK] [OPTIONS]
```

**Argumen wajib:**
- `LINK` - URL atau teks yang akan dijadikan barcode

**Opsi opsional:**
- `-t, --type` - Tipe barcode: `qr` (default) atau `code128`
- `-o, --output` - Nama file output (default: `barcode`)
- `--png` - Force output PNG untuk Code128
- `--svg` - Output SVG untuk Code128
- `--qr-box` - Ukuran box QR (default: 10)
- `--qr-border` - Margin putih QR (default: 4)

### Contoh Penggunaan

```bash
# QR Code dengan custom nama file
python make_barcode.py "https://github.com" -o my_qr_code

# QR Code dengan custom box size
python make_barcode.py "https://github.com" --qr-box 15 --qr-border 2

# Code128 output SVG
python make_barcode.py "123456789" -t code128 -o invoice --svg

# Code128 output PNG
python make_barcode.py "123456789" -t code128 -o invoice --png
```

## Output

- File PNG atau SVG akan tersimpan di direktori saat ini
- Default nama file: `barcode.png` atau `barcode.svg`

## Requirements

- Python 3.6+
- qrcode[pil] >= 7.0
- python-barcode >= 0.14.0