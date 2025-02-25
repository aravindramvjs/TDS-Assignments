from PIL import Image

# Load the scrambled image
scrambled_image = Image.open('./jigsaw.webp')  # Replace with your file path if needed

# Define the mapping data
mapping_data = [
    (2, 1, 0, 0), (1, 1, 0, 1), (4, 1, 0, 2), (0, 3, 0, 3), (0, 1, 0, 4),
    (1, 4, 1, 0), (2, 0, 1, 1), (2, 4, 1, 2), (4, 2, 1, 3), (2, 2, 1, 4),
    (0, 0, 2, 0), (3, 2, 2, 1), (4, 3, 2, 2), (3, 0, 2, 3), (3, 4, 2, 4),
    (1, 0, 3, 0), (2, 3, 3, 1), (3, 3, 3, 2), (4, 4, 3, 3), (0, 2, 3, 4),
    (3, 1, 4, 0), (1, 2, 4, 1), (1, 3, 4, 2), (0, 4, 4, 3), (4, 0, 4, 4)
]

# Create a blank image for the reconstructed result
reconstructed_image = Image.new('RGB', (500, 500))

# Loop through each mapping and place pieces in their original positions
piece_size = scrambled_image.width // 5  # Each piece is assumed to be square
for original_row, original_col, scrambled_row, scrambled_col in mapping_data:
    # Calculate coordinates of the scrambled piece
    left = scrambled_col * piece_size
    upper = scrambled_row * piece_size
    right = left + piece_size
    lower = upper + piece_size

    # Crop the piece from the scrambled image
    piece = scrambled_image.crop((left, upper, right, lower))

    # Calculate coordinates for placing the piece in the reconstructed image
    dest_left = original_col * piece_size
    dest_upper = original_row * piece_size

    # Paste the piece into its correct position
    reconstructed_image.paste(piece, (dest_left, dest_upper))

# Save the reconstructed image as PNG
reconstructed_image.save('reconstructed_image.png')
print("Reconstructed image saved as 'reconstructed_image.png'")