from pathlib import Path


def make_code128(data: str, out_path: Path, write_png: bool = True) -> Path:
    import barcode
    from barcode.writer import ImageWriter

    code128 = barcode.get("code128", data)
    if write_png:
        out_path = Path(out_path).with_suffix(".png")
        code128.write(out_path.open("wb"), writer=ImageWriter())
    else:
        out_path = Path(out_path).with_suffix(".svg")
        code128.write(out_path.open("wb"))
    return out_path
