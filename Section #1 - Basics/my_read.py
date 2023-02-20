import cv2 as cv

# img = cv.imread("Resources\Photos\cat_large.jpg")

# cv.imshow('Cat', img)

cap = cv.VideoCapture('Resources\Videos\dog.mp4')

while True:
    isTrue, frame = cap.read()

    # check if the frame was correctly read
    if not isTrue:
        print("Could not read, closing...")
        break

    # display frame
    cv.imshow("Video", frame)

    # wait 'q' to be pressed and finish loop
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()