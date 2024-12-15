# PNG Extractor for `.FUI` Files

This repository contains a Python-based tool for extracting `.png` files from `.fui` files. `.fui` files are used in **Minecraft: Legacy Console Edition** to store UI assets, including images and textures.

The tool includes a **command-line version** and a **GUI version** for user convenience.

---

## Features

- **Extracts PNGs** from `.fui` files by identifying PNG headers and footers.
- Supports **batch extraction** of all PNG files stored in a `.fui` file.
- Includes a **simple GUI** for ease of use.
- Automatically saves the extracted PNG files with incremental naming (e.g., `ui1.png`, `ui2.png`, etc.).

---

## How It Works

The tool identifies PNG images within `.fui` files by detecting the PNG file structure:

- **Header:** `\x89PNG\r\n\x1a\n`
- **Footer:** `IEND\xaeB\x60\x82`

The program reads the `.fui` file in binary mode, searches for these patterns, and extracts the byte ranges between each header and footer.

---

## Installation

### Requirements

- Python 3.7+
- Required libraries:
  - `tkinter` (for GUI version)
  - No additional dependencies are needed for the command-line version.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/fui-png-extractor.git
   cd fui-png-extractor
