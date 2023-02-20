import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # to access the width and height, we need to type the shape index of the array (i.e. the frame)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    print(dimensions)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

cap = cv.VideoCapture("Resources\Videos\dog.mp4")


while True:
    isTrue, frame = cap.read()
    
    # check if the frame was correctly read
    if not isTrue:
        print("Could not read, closing...")
        break

    # display frame
    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    # wait 'q' to be pressed and finish loop
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()