import base64
import os
import tempfile
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from barcode_gen import make_code128, make_qr

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    payload = request.get_json(silent=True) or {}
    text = (payload.get("text") or "").strip()
    barcode_type = payload.get("type", "qr")

    if not text:
        return jsonify({"error": "Masukkan URL atau teks terlebih dahulu."}), 400
    if barcode_type not in ("qr", "code128"):
        return jsonify({"error": "Tipe barcode tidak valid."}), 400

    fd, tmp = tempfile.mkstemp()
    os.close(fd)
    tmp_path = Path(tmp)
    out = None

    try:
        if barcode_type == "qr":
            out = make_qr(text, tmp_path)
        else:
            out = make_code128(text, tmp_path)

        mime = "image/png" if out.suffix == ".png" else "image/svg+xml"
        img_b64 = base64.b64encode(out.read_bytes()).decode()

        return jsonify({
            "image": f"data:{mime};base64,{img_b64}",
            "filename": f"barcode{out.suffix}",
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        tmp_path.unlink(missing_ok=True)
        if out is not None:
            out.unlink(missing_ok=True)
