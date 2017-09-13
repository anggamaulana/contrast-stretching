import cv2
import numpy as np
from matplotlib import pyplot as plt

nm_image='leopard.jpg'

img = cv2.imread(nm_image)
# cv2.imshow("nature",img)
# cv2.waitKey()
r1=30.0
s1=20.0
r2=150.0
s2=200.0
r3=255.0
s3=255.0
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite(nm_image+'gray.jpg',img_gray)
print img_gray
print img_gray.shape

# Untuk r <= 0 < r1, maka s = r . (s1 / r1)
# Untuk r1 <= r < r2, maka s = s1 + ( (r-r1) . ((s2-s1) / (r2-r1)) )
# Untuk r2 <= r <=(L-1), maka s = s2 + ( (r-r2) . ((L-1)-s2) / ((L-1) - r2) )

plt.hist(img_gray.ravel(),256,[0,256]); 

img_gray2=np.where((img_gray<r1) , np.floor(img_gray*(s1/r1)),
	np.where(((img_gray>r1)&(img_gray<r2)) , np.floor(s1+(img_gray-r1)*((s2-s1)/(r2-r1))),
		np.where(((img_gray>r2)&(img_gray<r3)) , np.floor(s2+(img_gray-r2)*((s3-s2)/(r3-r2))),img_gray)))

print "hasil modifikasi"

print img_gray2
print img_gray2.shape

cv2.imwrite(nm_image+'grayafter.jpg',img_gray2)

# plt.hist(img.ravel(),256,[0,256]); 

plt.hist(img_gray2.ravel(),256,[0,256]); plt.show()