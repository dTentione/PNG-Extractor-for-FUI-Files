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

---

## Screenshots Of GUI Version
![Screenshot 2024-12-15 140201](https://github.com/user-attachments/assets/b979873e-07d6-4fa6-882c-60e7e3bbd243)
![Screenshot 2024-12-15 140230](https://github.com/user-attachments/assets/2200a885-a0c4-4289-a2ab-9de089543218)
![Screenshot 2024-12-15 140256](https://github.com/user-attachments/assets/1a13bdec-79d2-4157-8947-22e793690897)


---

### Issues

- If you encounter any problems, please report these on the Issues page.
