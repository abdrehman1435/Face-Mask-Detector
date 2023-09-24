#import the following packages using pip
from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))

    # Load the YOLO model from the best.pt file
    model = YOLO("best.pt")
    # Define a list of class names for the model output
    classNames = ["Face Mask"]
    # Loop until the video ends or the user presses a key
    while True:
        # Read a frame from the video capture object and store it in img
        success, img = cap.read()
        # Run the YOLO model on the img and get the results as a list of objects
        results = model(img, stream=True)
        # Loop through each object in the results list
        for r in results:
            # Get the bounding boxes of the detected objects as a list of Box objects
            boxes = r.boxes
            # Loop through each box in the boxes list
            for box in boxes:
                # Get the coordinates of the top-left and bottom-right corners of the box as floats
                x1, y1, x2, y2 = box.xyxy[0]
                # Convert the coordinates to integers
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # Print the coordinates to the console
                print(x1, y1, x2, y2)
                # Draw a rectangle around the box on the img using OpenCV rectangle function
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                # Get the confidence score of the box as a float between 0 and 1
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Get the class index of the box as an integer between 0 and n-1, where n is the number of classes
                cls = int(box.cls[0])
                # Get the class name of the box from the classNames list using the class index
                class_name = classNames[cls]
                # Create a label string that contains the class name and the confidence score
                label = f'{class_name}{conf}'
                # Get the size of the label text as a tuple of width and height using OpenCV getTextSize function
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                # Print the size of the label text to the console
                print(t_size)
                # Calculate the coordinates of the bottom-right corner of the label background as a tuple of x and y using t_size and x1 and y1 values
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                # Draw a filled rectangle around the label text on the img using OpenCV rectangle function with negative thickness value
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                # Put the label text on top of the label background on the img using OpenCV putText function with white color and anti-aliased line type
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        # Return img as an output of this function
        yield img

#Release all resources used by OpenCV VideoCapture object
cv2.destroyAllWindows()
