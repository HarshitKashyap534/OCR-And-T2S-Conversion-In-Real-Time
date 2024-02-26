import pytesseract
from PIL import Image
import pyttsx3

# Update this line with the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using pytesseract
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

# Function to convert text to speech using pyttsx3
def convert_text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in converting text to speech: {e}")

if __name__ == "__main__":
    # Your specific image path
    image_path = r'C:\Users\user\Sentiment2\Emotion_Detection_CNN\ocr_test_img.png'

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:", extracted_text)

    # If text is extracted, convert it to speech
    if extracted_text.strip():
        convert_text_to_speech(extracted_text)
    else:
        print("No text extracted from image.")
