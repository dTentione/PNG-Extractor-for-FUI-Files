import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def extract_pngs(input_file, output_dir, log_widget):
    # Define the PNG header and footer signatures in hexadecimal
    png_header = b'\x89PNG\r\n\x1a\n'
    png_footer = b'IEND\xaeB`\x82'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the entire .fui file in binary mode
    with open(input_file, 'rb') as f:
        data = f.read()
    
    # Find all occurrences of the PNG header and footer
    start_indices = [match.start() for match in re.finditer(re.escape(png_header), data)]
    end_indices = [match.end() for match in re.finditer(re.escape(png_footer), data)]
    
    log_widget.insert(tk.END, f"Found {len(start_indices)} PNG headers\n")
    log_widget.insert(tk.END, f"Found {len(end_indices)} PNG footers\n")
    log_widget.see(tk.END)
    
    # Ensure there's at least one match
    if not start_indices or not end_indices:
        log_widget.insert(tk.END, "No PNG headers or footers found. Please check the file content.\n")
        log_widget.see(tk.END)
        return
    
    # Extract each PNG and save it to the output directory
    min_matches = min(len(start_indices), len(end_indices))
    for i in range(min_matches):
        start = start_indices[i]
        end = end_indices[i]
        png_data = data[start:end]
        output_file_path = os.path.join(output_dir, f"ui{i+1}.png")
        with open(output_file_path, 'wb') as out_file:
            out_file.write(png_data)
        log_widget.insert(tk.END, f"Extracted: {output_file_path}\n")
        log_widget.see(tk.END)
    
    log_widget.insert(tk.END, "Extraction complete!\n")
    log_widget.see(tk.END)

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("FUI files", "*.fui"), ("All files", "*.*")])
    if file_path:
        input_file_var.set(file_path)

def select_output_dir():
    dir_path = filedialog.askdirectory()
    if dir_path:
        output_dir_var.set(dir_path)

def start_extraction():
    input_file = input_file_var.get()
    output_dir = output_dir_var.get()
    if not input_file or not os.path.isfile(input_file):
        messagebox.showerror("Error", "Please select a valid .fui file.")
        return
    if not output_dir:
        messagebox.showerror("Error", "Please select a valid output directory.")
        return
    log_widget.delete(1.0, tk.END)
    extract_pngs(input_file, output_dir, log_widget)

# Create the main window
root = tk.Tk()
root.title("PNG Extractor from FUI")

# Input file selection
input_file_var = tk.StringVar()
tk.Label(root, text="Select .fui File:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=input_file_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

# Output directory selection
output_dir_var = tk.StringVar()
tk.Label(root, text="Select Output Directory:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_dir).grid(row=1, column=2, padx=10, pady=5)

# Start extraction button
tk.Button(root, text="Extract PNGs", command=start_extraction).grid(row=2, column=1, pady=10)

# Log output
log_widget = scrolledtext.ScrolledText(root, width=70, height=15)
log_widget.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
