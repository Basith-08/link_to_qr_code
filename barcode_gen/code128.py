from pathlib import Path


def make_code128(data: str, out_path: Path, write_png: bool = True) -> Path:
    import barcode
    from barcode.writer import ImageWriter

    if write_png:
        code128 = barcode.get("code128", data, writer=ImageWriter())
        out_path = Path(out_path).with_suffix(".png")
    else:
        code128 = barcode.get("code128", data)
        out_path = Path(out_path).with_suffix(".svg")

    with out_path.open("wb") as f:
        code128.write(f)
    return out_path
