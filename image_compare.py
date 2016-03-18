# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
#import Image
#import ImageChops


def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	 
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	 
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	 
	# show the images
	plt.show()


def test():
## graphical comparisson between image 1 and image 2
 #   im1 = Image.open("/home/wtpc-12/Escritorio/figure_1.png")
 #   im2 = Image.open("/home/wtpc-12/Escritorio/figure_2.png")

 #   diff = ImageChops.difference(im2, im1)

## MSE and SSIM
# load the images img1.png y img2.png
    img1 = cv2.imread("figure_1.png")
    img2 = cv2.imread("figure_2.png")

# convert the images to grayscale
    imgA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    imgB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    m = mse(imgA, imgB)
    s = ssim(imgA, imgB)

    print(m, s)

# <codecell>

if __name__ == '__main__':

## sonogram

## MSE and SSIM
# load the images img1.png y img2.png
    img1 = cv2.imread('./plots/sonogram/sonogram_canary_XC122552 - Atlantic Canary - Serinus canaria_001.png')
    img2 = cv2.imread('./plots/sonogram/sonogram_glareola_pratincola_call1_005.png')

# convert the images to grayscale
    imgA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    imgB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    compare_images(imgA,imgB, 'sonogram')














