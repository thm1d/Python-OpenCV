import cv2
from matplotlib import pyplot as plt

bgr = cv2.imread('Images\input4.jpg')

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(bgr)
axs[0].set_title('BGR Image')
axs[1].imshow(rgb)
axs[1].set_title('RGB Image')

plt.show()

cv2.imwrite('Images\output_04.jpg', bgr)