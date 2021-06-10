from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base_board():
    return render_template('index.html', x = 8, y = 8, color1 = "red", color2 = "black")

@app.route('/<int:num>')
def new_board(num):
    return render_template('index.html', x = 8, y = num, color1 = "red", color2 = "black")

@app.route('/<int:x>/<int:y>')
def custom_board(x,y):
    return render_template('index.html', x = x, y = y, color1 = "red", color2 = "black")

if __name__=="__main__":
    app.run(debug=True)