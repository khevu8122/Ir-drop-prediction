import cv2
file="D:/MU/AI Project/label set/8092-zero-riscy-a-2-c5-u0.7-m1-p2-f0.npy"
import numpy as np
import matplotlib.pyplot as plt
data=np.load(file)
for i in range(1):
    plt.imshow(data[:,:,i])
    plt.savefig("D:/MU/AI Project/labels_output 9/"+str(i)+".png")
   