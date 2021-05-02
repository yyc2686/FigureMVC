# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
INPUT_DIR = os.path.join(BASE_DIR, r"resources\input")
OUTPUT_DIR = os.path.join(BASE_DIR, r"resources\output")

PATH = {
    "out/pdf": os.path.join(OUTPUT_DIR, "pdfOutput"),
}
