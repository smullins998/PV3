from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.debug = True

#Backend 
@app.route('/')
def main():
    return render_template('main.html')

#Backend 
@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/proj_songspy')
def proj_songspy():
    return render_template('proj_songspy.html')

@app.route('/proj_reversemomentum')
def proj_reversemomentum():
    return render_template('proj_reversemomentum.html')

@app.route('/proj_speech')
def proj_speech():
    return render_template('proj_speech.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
