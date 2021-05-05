


import cv2
import numpy as np


img = cv2.imread('imageToSave.jpg')
h, w, c = img.shape
mask = np.zeros([h + 2, w + 2], np.uint8)
result = img.copy()


cv2.floodFill(result, mask, (0,0), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (38,313), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (363,345), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (619,342), (255,255,255), (3,151,65), (3,151,65), flags=8)


gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
cv2.imwrite("test.jpg", gray)
# display it
cv2.imshow("result", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()