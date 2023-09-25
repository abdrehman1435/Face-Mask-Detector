# Required to run the YOLOv8 model
from flask import Flask, Response,jsonify,request,render_template,session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,StringField,DecimalRangeField,IntegerRangeField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired,NumberRange
import os
import cv2

# train is the python file which contains the code for our object detection model
#Video Detection is the Function which performs Object Detection on Input Video
from train import video_detection
app = Flask(__name__)

app.config['SECRET_KEY'] = 'smoothrelic33'
app.config['UPLOAD_FOLDER'] = 'static/images'
#Generate_frames function takes path of input video file and  gives us the output with bounding boxes
# around detected objects


#Use FlaskForm to get input video file  from user
class UploadFileForm(FlaskForm):
    #We store the uploaded video file path in the FileField in the variable file
    #We have added validators to make sure the user inputs the video in the valid format  and user does upload the
    #video when prompted to do so
    file = FileField("File",validators=[InputRequired()])
    submit = SubmitField("Run")

#Now we will display the output video with detection
def generate_frames(path_x = ''):
    # yolo_output variable stores the output for each detection
    # the output with bounding box around detected objects

    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref,buffer=cv2.imencode('.jpg',detection_)
        # Any Flask application requires the encoded image to be converted into bytes
        #We will display the individual frames using Yield keyword,
        #we will loop over all individual frames and display them as video
        #When we want the individual frames to be replaced by the subsequent frames the Content-Type, or Mini-Type
        #will be used
        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')


def generate_frames_web(path_x):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref,buffer=cv2.imencode('.jpg',detection_)

        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')



@app.route('/', methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    session.clear()
    return render_template('indexpage.html')

@app.route('/FrontPage', methods=['GET','POST'])
def front():
    # Upload File Form: Create an instance for the Upload File Form
    form = UploadFileForm()
    if form.validate_on_submit():
        # Our uploaded video file path is saved here
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))  # Then save the file
        # Use session storage to save video file path
        session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                                             secure_filename(file.filename))
    return render_template('videoprojectnew.html', form=form)

@app.route('/video')
def video():

    return Response(generate_frames(path_x = session.get('video_path', None)),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/webapp')
def webapp():

    return Response(generate_frames_web(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route("/webcam", methods=['GET','POST'])

def webcam():
    session.clear()
    return render_template('ui.html')

if __name__ == "__main__":
    app.run(debug=True)
