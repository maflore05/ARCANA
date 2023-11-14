from PIL import Image
import pytesseract
import easygui
# Set the path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
image_path = easygui.fileopenbox()
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)