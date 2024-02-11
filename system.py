import cv2
import pytesseract



pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def extract_text_from_image(image_path):

    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

if __name__ == "__main__":
    # Path to image file
    image_path = './sample-image.png'

    extracted_text = extract_text_from_image(image_path)

    print("Extracted Text:")
    print(extracted_text)