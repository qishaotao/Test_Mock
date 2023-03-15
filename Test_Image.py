from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'c://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('./Picture/test.jpg'))
print(text)