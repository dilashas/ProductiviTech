import pandas as pd
from beeprint import pp as debug
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify

import frameDetails as fd
from User.service import save_user, init_db, verify_user, list_users
from camera import Camera

# ----------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)

video_stream = Camera()
videoFps = video_stream.fps

framesDf = pd.DataFrame()
frameCount = 0


# ----------------------------------------------------------------------------------------------------------------------

@app.route('/')
def index():
    init_db()
    return render_template('index.html')


# ----------------------------------------------------------------------------------------------------------------------

def gen(camera):
    global frameCount
    global framesDf

    while True:
        frame, facePresent, eyesPresent, distance = camera.get_frame()

        # frame = camera.get_frame()

        # Increment the frame count at each step of the loop
        frameCount += 1
        # Create a current frame object using the parameters returned by detect.
        # We will do this for each split of the camera
        currFrame = fd.customFrame(frameCount, facePresent, eyesPresent, distance, videoFps)

        # debug statement that prints all the properties of the class
        debug(currFrame)

        # Add the currentFrame object to the dataframe
        framesDf[frameCount] = [currFrame]

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# ----------------------------------------------------------------------------------------------------------------------

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ----------------------------------------------------------------------------------------------------------------------

@app.route('/camera')
def camera():
    return render_template('camera.html')


# ----------------------------------------------------------------------------------------------------------------------

@app.route('/about')
def about():
    if request.args:
        username = request.args['username']
        return render_template('about.html', messages={"username": username})
    else:
        return render_template('about.html')


@app.route('/login')
def login():
    if request.args:
        not_valid = request.args['notValid']
        return render_template('login.html', messages={"notValid": not_valid})
    else:
        return render_template('login.html')
    # is_valid = request.args['is_valid']


@app.route('/profile')
def profile():
    if request.args:
        username = request.args['username']
        return render_template('profile.html', messages={"username": username})
    else:
        return render_template('profile.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/history')
def history():
    if request.args:
        username = request.args['username']
        return render_template('history.html', messages={"username": username})
    else:
        return render_template('history.html')


@app.route('/upload')
def upload():
    if request.args:
        username = request.args['username']
        return render_template('upload.html', messages={"username": username})
    else:
        return render_template('upload.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    print("username = {}, password = {}, email= {}".format(username, password, email))
    save_user(username=username, email=email, password=password)
    return redirect(url_for('login'))


@app.route('/checklogin', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print("username = {}, password = {}".format(username, password))
    user = verify_user(username=username, password=password)
    print("valid= " + str(user))
    if user:
        return redirect(url_for('upload', username=username))
    else:
        return redirect(url_for('login', notValid=True))


@app.route("/list")
def list_user():
    users = list_users()
    return jsonify(users)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', debug=True, port="5000")
