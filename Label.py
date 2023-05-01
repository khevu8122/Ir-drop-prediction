import cv2

im = cv2.imread('"D:\MU\AI Project\label set\57-RISCY-a-1-c2-u0.75-m4-p6-f0.npy"')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8