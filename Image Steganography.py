import cv2
import string
import os

# Create dictionaries for character to ASCII and vice versa
char_to_ascii = {chr(i): i for i in range(256)}
ascii_to_char = {i: chr(i) for i in range(256)}

# Read the image
image = cv2.imread("free-nature-images.jpg")

# Get image dimensions
height, width, _ = image.shape
print(f"Image dimensions: {height}x{width}")

# Input security key and text to hide
key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

# Ensure the image is large enough to hold the text
if len(text) > height * width * 3:
    print("Error: The text is too long to be hidden in this image.")
    exit()

# Initialize variables for encoding
key_length = len(key)
text_length = len(text)
key_index = 0
color_plane = 0
row = 0
column = 0

# Hide text in image
for char in text:
    image[row, column, color_plane] = char_to_ascii[char] ^ char_to_ascii[key[key_index]]
    key_index = (key_index + 1) % key_length
    color_plane = (color_plane + 1) % 3
    column += 1
    if column == width:
        column = 0
        row += 1

# Save and open the encrypted image
cv2.imwrite("encrypted_img.jpg", image)
os.startfile("encrypted_img.jpg")
print("Data hiding in image completed successfully.")

# Extracting data from image
print("\nOptions:\n1. Decode data from Image\n2. Exit")
choice = input("Enter your choice: ").strip().lower()

if choice == '1' or choice == 'decode':
    reentered_key = input("\nRe-enter key to extract text: ")
    decrypted_text = ""

    if key == reentered_key:
        key_index = 0
        color_plane = 0
        row = 0
        column = 0

        for _ in range(text_length):
            decrypted_text += ascii_to_char[image[row, column, color_plane] ^ char_to_ascii[key[key_index]]]
            key_index = (key_index + 1) % key_length
            color_plane = (color_plane + 1) % 3
            column += 1
            if column == width:
                column = 0
                row += 1

        print("Encrypted text was:", decrypted_text)
    else:
        print("Key doesn't match.")
elif choice == '2' or choice == 'exit':
    print("Thank you. EXITING.")
else:
    print("Invalid choice. EXITING.")
