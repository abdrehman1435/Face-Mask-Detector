# Face Mask Detector
Face Mask Detector is a project that uses deep learning to detect whether people are wearing face masks. It can be used for applications such as enforcing mask-wearing policies, monitoring public health, or generating statistics on mask usage.

## Installation and Usage
To use this project, you need to follow these steps:

Clone this repository to your local machine using git clone https://github.com/your_username/face-mask-detector.git.
Download and install the required dependencies using pip install -r requirements.txt which is in the repository.

## Collecting data and creating the dataset
Collect a dataset of images containing people with and without face masks. You can use any source of images, such as online sources, web scraping, or your own camera, or download the dataset zip which is in this repository. You need to have around 3000 images for good performance or at least a minimum of 1000 images.
Annotate the images using Roboflow, a tool that helps you label, preprocess, and augment your images. You must draw bounding boxes around the masks and label them "Face-Mask". Then you can preprocess the data using the features provided by Roboflow. Next, you can augment the dataset using flip, blur, etc., and the various options provided by Roboflow and download the new dataset.

## Exporting the dataset
Export your dataset in a format that is compatible with your chosen framework. Roboflow provides ready-to-use export options for YOLOv5, TensorFlow Lite, YOLOv8, and other popular frameworks.

## Training the model using YOLOv8
Train the model using YOLOv8, a state-of-the-art object detection model from Ultralytics. You can use the command `pip install ultralytics` and then `import YOLO from ultralytics` to download. You also need your computer to have a GPU and you need to download valid NVIDIA device drivers and the CUDA toolkit by NVIDIA to use YOLOv8. You need to change the hardware accelerator to GPU. You need to use the custom dataset option and provide the path to your Roboflow dataset and it's more simpler to do this by mounting your Google Drive. You can use the default settings or adjust them according to your needs. The training process will save the model weights in the runs/train folder. This process is shown in the "FaceMask.ipynb" notebook in the repository.

## Alternative training using Roboflow
The model can also be trained using Roboflow using the Roboflow-train feature. The object can be trained using a pre-trained model like the COCO dataset or you can train your own custom model after exporting your dataset.

### Deploying your model from Roboflow
There are multiple ways in which we can deploy the model directly from Roboflow for example using NVIDIA Jetson or IOS device. A few of them are:

### Deploying using NVIDIA Jetson
#### Installation
You can take the edge acceleration version of your model to the NVIDIA Jetson, where you may need real-time speeds with limited hardware resources.

##### Step #1: Flash Jetson Device
Ensure that your Jetson is flashed with Jetpack 4.5, 4.6, or 5.1. You can check your existing with this repository from Jetson Hacks
git clone https://github.com/jetsonhacks/jetsonUtilities.git
cd jetsonUtilities
python jetsonInfo.py

##### Step #2: Run Docker Container
Next, run the Roboflow Inference Server using the accompanying Docker container:
``` sudo docker run --privileged --net=host --runtime=nvidia --mount source=roboflow,target=/tmp/cache -e NUM_WORKERS=1 roboflow/roboflow-inference-server-jetson-4.5.0:latest ```

The docker image you need depends on what Jetpack version you are using.
+ Jetpack 4.5: roboflow/roboflow-inference-server-jetson-4.5.0
- Jetpack 4.6: roboflow/roboflow-inference-server-jetson-4.6.1
* Jetpack 5.1: roboflow/roboflow-inference-server-jetson-5.1.1

The Jetson images default to using a CUDA execution provider. To use TensorRT, set the environment variable ' ONNXRUNTIME_EXECUTION_PROVIDERS=TensorrtExecutionProvider '. Note that while using TensorRT can increase performance, it also incurs an additional startup compilation cost.

##### Step #3: Use the Server
You can now use the server to run inference on any of your models. The following command shows the syntax for making a request to the inference API via ``` curl:
base64  **your_img.jpg** | curl -d @- "http://localhost:9001/[YOUR MODEL]/[YOUR VERSION]?api_key=[YOUR API KEY]" ```
When you send a request for the first time, your model will compile on your Jetson device for 5-10 minutes.


## Testing and validating the model using YOLOv8
Test and validate the model after training using the YOLOv8 command-line interface (CLI). You can use the --weights option to specify the path to your trained model weights, and the --source option to provide the path to your test images or video. The CLI will display the results on the screen and save them in the **runs/detect** folder.

## Creating a program
Use the trained model weights and create a program that can detect face masks in real-time using a webcam or a video file. You can use the train.py script in the repository as a reference. You need to import the YOLOv8 module and load your model weights using the **best.pt** in the results folder. Then, you need to create a loop that captures frames from your webcam or video file, passes them to the model using the predict function, and displays the results using OpenCV which draws bounding boxes around the detections and also displays the object identified and the confidence level

## Making the Back-end 
Create a Flask app using Python that can serve as the back-end for your project. You need to import Flask and create an app object using `app = Flask(__name__)`. Then, you need to define routes for your app using decorators such as `@app.route('/')`. The file dl.py can be used  You can use the **render_template** function to return HTML files from the templates folder, and the request object to handle user inputs. You also need to use the **send_from_directory** function to serve static files such as images, CSS, or JavaScript from the static folder.


## Make the Front-end and run the Flask app
 Here are some steps you can follow to create a simple Flask app with HTML and CSS as frontend:
<ul>
<li>Create a project folder and a virtual environment for your Flask app. You can use pip or conda to install Flask and other dependencies.</li>
<li>Create a subfolder called templates in your project folder and save your HTML files there. You can use any text editor or IDE to write your HTML code. You can
  also, use Bootstrap or other frameworks to style your HTML elements. Here I used 3 HTML pages namely 'indexpage.html' which is the front page of the web 
  application, 'ui.html' which is where the video is inputted by the user in either mp4 or mov format, and 'videoprojectnew.html' is where the Face-Mask-Detector 
  model is applied and the video is outputted with the bounding boxes and confidence level.</li>
<li>Create a subfolder called static in your project folder and save your CSS files there. You can use any text editor or IDE to write your CSS code. You can also
  use Sass or Less to preprocess your CSS code.</li>
<li>Create a Python file called app.py (dl.py in this repository) in your project folder and write your Flask code there. You can use the Flask class to create an app object and the render_template function to return your HTML files. You can also use the request object to handle user inputs and the url_for function to link your static files.</li>
<li>Run your Flask app using the command flask run in your terminal using local host or python dl.py. You should see a message like Running on http://127.0.0.1:5000/.</li>
</ul>

## Creating a GitHub repository and deploying the Flask app using Render
<ul>
<li>Create a GitHub account if you don’t have one already. You can sign up for free at GitHub.</li>
<li>Create a new repository on GitHub by clicking the [New] button on the top left corner of the page. You can name your repository as you like, such as “flask-app”. You can also add a description, a README file, a license, and a .gitignore file for Python. </li>
<li>The code uses Gunicorn to serve your app in a production setting. Install Flask, Gunicorn, and other dependencies using the command 
``` pip install -r requirements.txt ```.</li>
<li>Create a new Web Service on Render, and give Render permission to access your new repo.</li>
</ul>

Use the following values during creation:

Runtime:	**Python**
Build Command:	**pip install -r requirements.txt**
Start: Command:	**gunicorn dl: app**

That’s it! Your web service will be live on your Render URL as soon as the build finishes.


## Deploying Flask app using Heroku
To deploy a Flask app using Heroku, you need to have some basic knowledge of Git, GitHub, and Flask. You also need to install the Heroku CLI and create a Heroku account.

Here are some general steps to deploy a Flask app using Heroku:

+ Create a GitHub repository for your Flask app and push your code to it. You can use the `git init`,` git add`, `git commit`, and `git push` commands to do this. You 
  can also, use tools like GitHub Desktop or Visual Studio Code to manage your GitHub repository.
 
- Create a Heroku app using the heroku create command in your terminal. This will generate a unique name and URL for your app, such as https://flask-app- 
 1234.herokuapp.com/. You can also specify a custom name for your app using the --app option, such as heroku create --app flask-app-1234.
 
* Connect your Heroku app to your GitHub repository using the heroku git: remote command in your terminal. This will set up a remote branch called heroku that 
 links to your Heroku app. You can also use the Heroku dashboard to connect your app to your GitHub repository.
 
+ Configure your Flask app for deployment by creating some files in your project folder, such as:

- A requirements.txt file that lists the dependencies of your app, such as Flask, gunicorn, etc. You can use the pip freeze > requirements.txt command to generate this file automatically.
 
* A Procfile file that specifies the command to run your app on Heroku, such as web: gunicorn dl: app. This tells Heroku to use the gunicorn web server to run the  app object from the app.py file.
 
+ A runtime.txt file that specifies the Python version to use on Heroku, such as python-3.9.7. You can check the supported Python versions on Heroku.

- Deploy your Flask app to Heroku by pushing your code to the heroku remote branch using the git push heroku main command in your terminal. This will trigger the 
 build and deployment process on Heroku, which may take a few minutes. You can check the status of your deployment using the heroku logs --tail command or the 
 Heroku dashboard.
 
* Visit your Heroku app URL in your browser and you should see your Flask app running on the cloud.


# Acknowledgments
This project is inspired by and based on the following sources:

+ <a href="https://docs.ultralytics.com/">YOLOv8: Ultralytics Object Detection by Ultralytics</a>
- https://docs.roboflow.com/ 
* https://github.com/ultralytics/ultralytics
+ https://www.youtube.com/watch?v=pg11wmj8LbY
- https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

