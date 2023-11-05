from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/video')
def videopage():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )