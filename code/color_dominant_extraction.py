import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

img = cv.imread(r"color dominant extraction\color dominant image.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
img_resized = cv.resize(img, (200, 150), interpolation=cv.INTER_AREA)

X = img_resized.reshape(-1, 3)

k = 6
model = KMeans(n_clusters=k)
model.fit(X)

centroids = model.cluster_centers_
colors = np.array(centroids, dtype=np.uint8)
plt.figure(figsize=(12, 4))
for i, color in enumerate(colors, 1):
    plt.subplot(1, k, i)
    plt.axis('off')
    mat = np.zeros((100, 100, 3), dtype='uint8')
    mat[:, :, :] = color
    plt.imshow(mat)

plt.show()
