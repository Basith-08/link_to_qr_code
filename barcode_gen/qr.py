from pathlib import Path


def make_qr(data: str, out_path: Path, box_size: int = 10, border: int = 4) -> Path:
    import qrcode

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    out_path = Path(out_path).with_suffix(".png")
    img.save(out_path)
    return out_path
