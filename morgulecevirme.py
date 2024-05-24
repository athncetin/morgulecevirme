import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "gul.jpg"
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

lower_red = np.array([100, 0, 0])
upper_red = np.array([255, 100, 100])
rose_mask = cv2.inRange(image_rgb, lower_red, upper_red)

image_rgb[rose_mask == 0] = [0, 0, 0]

image_rgb[rose_mask > 0] = [128, 0, 128]

output_path_opencv = "gul_modified_opencv.jpg"
cv2.imwrite(output_path_opencv, cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))

plt.imshow(image_rgb)
plt.axis('off')
plt.show()

output_path_opencv