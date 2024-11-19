import cv2
import os
from PIL import Image

mean_width = 0 
mean_height = 0

folder = "images" 
number_of_files = len(os.listdir(folder))
print(number_of_files)

for file_name in os.listdir(folder):
    image = Image.open(os.path.join(folder, file_name))
    width, height = image.size
    mean_height += height
    mean_width += width 

mean_width = mean_width//number_of_files
mean_height = mean_height//number_of_files

print(mean_height)
print(mean_width)

for file_name in os.listdir(folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
        image = Image.open(os.path.join(folder, file_name))
        resized_image = image.resize((mean_width, mean_height), Image.Resampling.LANCZOS)
        resized_image.save(file_name, "JPEG", quality = 95)
        print(resized_image)


cv2.waitKey()
cv2.destroyAllWindows()