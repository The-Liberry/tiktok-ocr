# OCR-Tiktok

This is a utilization of Tesseract (pytesseract) for Optical Character Recognition (OCR) for Summer 2025

## Requirements

Python 3.12.8 was used for this project

Use this website to download tesseract and add it to path:
https://docs.coro.net/featured/agent/install-tesseract-windows/

After, create a .venv using the `requirements.txt` file to download all dependencies

## Usage

Everything is made on the `OCR2.ipynb` and can be run on there. Excess code in `deprecated_code` is no longer in use.

## Issues

Since pytesseract has a hard time deciphering emojis, certain artifacts might appear, or other incorrect recognition can render certain items non-legible.

Many artifacts are similar in nature, so if here are a list of some I've found:

- BX
- Bl
- lx
- Lxi
- tk
- other miscellaneous symbols and letters (@=, +\*\*, etc.)

Additionally, pytesseract has a hard time deciphering the follower counts, so almost all the time they are wrong. Looking at the bios, at the end of a short bio, it might have miscellaneous symbols and/or "Showcase" or "Description." These are from the tiktok videos, since the crop for the bio was intentionally made a bit taller to avoid accidental cutoff from longer bios.

## Fixes/upcoming items later on

Future/improvements that want to be made are listed here.

- [ ] Try and set up training data to maybe make the OCR more accurate
- [ ] Train Tesseract to recognize emojis or find a way to remove them
- [ ] Fix up regular expressions to make the searches more flexible
