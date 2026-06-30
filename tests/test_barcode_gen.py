import os
import tempfile
from pathlib import Path

import pytest

from barcode_gen import make_code128, make_qr


@pytest.fixture
def tmp_path_no_suffix():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    p = Path(path)
    yield p
    p.unlink(missing_ok=True)


def test_make_qr_creates_png(tmp_path_no_suffix):
    out = make_qr("https://github.com", tmp_path_no_suffix)
    assert out.suffix == ".png"
    assert out.exists()
    assert out.stat().st_size > 0
    out.unlink()


def test_make_qr_custom_options(tmp_path_no_suffix):
    out = make_qr("hello", tmp_path_no_suffix, box_size=5, border=1)
    assert out.exists()
    out.unlink()


def test_make_code128_creates_png(tmp_path_no_suffix):
    out = make_code128("123456", tmp_path_no_suffix, write_png=True)
    assert out.suffix == ".png"
    assert out.exists()
    assert out.stat().st_size > 0
    out.unlink()


def test_make_code128_creates_svg(tmp_path_no_suffix):
    out = make_code128("123456", tmp_path_no_suffix, write_png=False)
    assert out.suffix == ".svg"
    assert out.exists()
    out.unlink()
