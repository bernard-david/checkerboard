from flask import Flask
app = Flask(__name__)

@app.route('/')
def base_board():
    pass

@app.route('/<int:num>')
def new_board(num):
    pass

@app.route('/<int:x>/<int:y>')
def custom_board(x,y):
    pass

if __name__=="__main__":
    app.run(debug==True)