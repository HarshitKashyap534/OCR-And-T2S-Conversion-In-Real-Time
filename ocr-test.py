import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open(r'C:\Users\user\Sentiment2\Emotion_Detection_CNN\ocr_test_img.png')

text = tess.image_to_string(img)

print(text)
