import cv2
import pytesseract
from PIL import Image, ImageDraw, ImageFont

# Load the image
image_path = 'the_run.jpg'
image = cv2.imread(image_path)

# Perform OCR to detect text
text = pytesseract.image_to_string(image)

# Replace the detected text with the desired text
new_text = "New Text"

# Convert the image to PIL format for editing
pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_image)

# Specify the font and size
font = ImageFont.truetype("arial.ttf", 36)

# Specify the position to overlay the text
position = (50, 50)

# Draw the new text on the image
draw.text(position, new_text, fill="white", font=font)

# Save the edited image
pil_image.save("edited_image.jpg")

# Display the edited image
pil_image.show()