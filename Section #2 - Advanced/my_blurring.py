import cv2 as cv

img = cv.imread("Resources\Photos\park.jpg")

# kernel size is the number of rows and columns of the crop
# blur is something applied to the crop's middle pixel as result of its surrounding ones
# sometimes, it's the average intensity of all pixels surrounding the middle pixel
average = cv.blur(img, (3, 3))
cv.imshow("Average", average)

# Gaussin Blur gives a particular weight for each surrounding pixel
# the average of the products of those weights gives the value of the true center
# It has less blur than the average method, but it's more natural
gauss = cv.GaussianBlur(img, (7,7), 0) # 0 is the standard deviation in the x direction
cv.imshow("Gaussian", gauss)

# Similar to average
# It finds the median of the intensity of the surrounding pixels
median = cv.medianBlur(img, 3) # there's no need for a tuple, it's a square kernel
cv.imshow("Median Blur", median)

# Bilateral
# The most effective, used in a lot computer vision projects
# Instead of blurring the edges, bilateral retains it.

bilateral = cv.bilateralFilter(img, 10, 35, 25)
# colorSigma means that more colors in the neighbourhood will be considered to compute blur
# colorSpace means that further out from the central pixel will influence blurring calculation


cv.waitKey(0)