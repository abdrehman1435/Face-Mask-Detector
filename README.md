# Face Mask Detector
Face Mask Detector is a project that uses deep learning to detect whether people are wearing face masks. It can be used for applications such as enforcing mask-wearing policies, monitoring public health, or generating statistics on mask usage.

# Installation and Usage
To use this project, you need to follow these steps:

Clone this repository to your local machine using git clone https://github.com/your_username/face-mask-detector.git.
Download and install the required dependencies using pip install -r requirements.txt which is in the repository.

# Collecting data 
Collect a dataset of images containing people with and without face masks. You can use any source of images, such as online sources, web scraping, or your own camera, or download the dataset zip which is in this repository. You need to have around 3000 images for good performance or at least a minimum of 1000 images.
Annotate the images using Roboflow, a tool that helps you label, preprocess, and augment your images. You must draw bounding boxes around the masks and label them "Face-Mask". Then you can preprocess the data using the features provided by Roboflow. Next, you can augment the dataset using flip, blur, etc., and the various options provided by Roboflow and download the new dataset.

# Training the model using YOLOv8
Train the model using YOLOv8, a state-of-the-art object detection model from Ultralytics. You can use the command 'pip install ultralytics and then import YOLO from ultralytics' to download. You also need your computer to have a GPU and you need to download valid NVIDIA device drivers and the CUDA toolkit by NVIDIA to use YOLOv8. You need to change the hardware accelerator to GPU. You need to use the custom dataset option and provide the path to your Roboflow dataset and it's more simpler to do this by mounting your Google Drive. You can use the default settings or adjust them according to your needs. The training process will save the model weights in the runs/train folder. This process is shown in the "FaceMask.ipynb" notebook in the repository.

# Alternative training using Roboflow
The model can also be

# Testing and validating the model using YOLOv8
Test and validate the model after training using the YOLOv8 command-line interface (CLI). You can use the --weights option to specify the path to your trained model weights, and the --source option to provide the path to your test images or video. The CLI will display the results on the screen and save them in the runs/detect folder.

# Creating a program
Use the trained model weights and create a program that can detect face masks in real-time using a webcam or a video file. You can use the train.py script in the repository as a reference. You need to import the YOLOv8 module and load your model weights using the best.pt in the results folder. Then, you need to create a loop that captures frames from your webcam or video file, passes them to the model using the predict function, and displays the results using OpenCV.

# Making the Back-end 
Create a Flask app using Python that can serve as the back-end for your project. You need to import Flask and create an app object using app = Flask(__name__). Then, you need to define routes for your app using decorators such as @app.route('/'). The file dl.py can be used  You can use the render_template function to return HTML files from the templates folder, and the request object to handle user inputs. You also need to use the send_from_directory function to serve static files such as images, CSS, or JavaScript from the static folder.

# Making the Front-end
Create a front-end for your project using HTML and CSS that can interact with your Flask app. You need to create HTML files in the templates folder that contain the structure and content of your web pages. You can use Bootstrap or other frameworks to style your HTML elements.





Acknowledgments
This project is inspired by and based on the following sources:

[YOLOv8: Ultralytics Object Detection] by Ultralytics

