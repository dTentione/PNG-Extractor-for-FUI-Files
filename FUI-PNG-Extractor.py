import os

def extract_pngs(input_file):
    # Define the PNG header and footer signatures in hexadecimal
    png_header = b'\x89PNG\r\n\x1a\n'
    png_footer = b'IEND\xaeB`\x82'

    # Ask the user for the output directory
    output_dir = input("Enter the directory where you want to save the extracted PNGs: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the entire .fui file in binary mode
    with open(input_file, 'rb') as f:
        data = f.read()

    # Start searching for PNGs
    start = 0
    count = 0

    while start < len(data):
        # Find the next occurrence of the PNG header
        header_index = data.find(png_header, start)
        if header_index == -1:
            break  # No more headers found, exit loop

        # Find the next occurrence of the PNG footer after the header
        footer_index = data.find(png_footer, header_index)
        if footer_index == -1:
            break  # No more footers found, exit loop

        # Include the entire block from header to the end of the footer
        end = footer_index + len(png_footer)
        png_data = data[header_index:end]

        # Save the extracted PNG to a file
        count += 1
        output_file_path = os.path.join(output_dir, f"ui{count}.png")
        with open(output_file_path, 'wb') as out_file:
            out_file.write(png_data)
        print(f"Extracted: {output_file_path}")

        # Move the start point forward to search for the next PNG
        start = end

    if count == 0:
        print("No PNG files were found in the provided .fui file.")
    else:
        print(f"Extraction complete! {count} PNG(s) were extracted.")

if __name__ == "__main__":
    # Ask the user for the .fui file path
    input_file_path = input("Enter the path of the .fui file: ")
    if os.path.isfile(input_file_path):
        extract_pngs(input_file_path)
    else:
        print("Invalid file path. Please provide a valid .fui file.")

