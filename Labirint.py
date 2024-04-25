import random

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Handler for the http://127.0.0.1:5000/ URL for our local server
@app.route('/', methods=['GET'])
def hello_world():
    return 'Welcome to the application'

"""
# We define handler for the http://127.0.0.1:5000/app for our local server
@app.route('/app', methods=['GET', 'POST'])  # methods allowed for this URL
def handle_app():
    # request is Flask built-in variable that stores data of current request
    if request.method == 'GET':
        return 'Send POST request with some data'
    elif request.method == 'POST':
        # request.data returns payload of current request as a binary string
        # As we print it, you can see it in console (like b'2')
        print(request.data)
        # Convert request.data to the usual string
        decoded_data = request.data.decode('utf-8')
        return f'You sent data: {decoded_data} {decoded_data}'

n=0

@app.route('/game/start', methods=['POST'])
def handle_game_start():
    global n
    n=random.randint(1, 10)
    return "NUmber was created"

@app.route('/game/guess', methods=['POST'])
def handle_game_guess():
    guest_num = int(request.data.decode('utf-8'))
    if guest_num < n:
        return ("Your number is smaller than our")
    if guest_num > n:
        return ("Your number is bigger than our")
    if guest_num == n:
        return ("You won")
    return " "
"""
@app.route('/game/labirint/start', methods=['POST'])
def labirint_game_start():
    mas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0], [0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0], [0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0], [0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0], [0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0], [0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0], [0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,0], [0,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0], [0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0], [0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0], [0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0], [1,1,1,0,1,1,0,1,1,0,0,1,0,0,0,0], [0,0,1,0,0,0,1,1,1,0,0,1,1,1,0,0], [0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return ("Labirint was created")
x=0
y=0
a=[x,y]

@app.route ('/game/labirint/right', methods=['POST'])
def labirint_game_right(a,x,y):
    #guest_decision = int(request.data.decode('utf-8'))
    if x+1==1:
        x=x+1
    else:
        print("You can not go there")
    y=y

@app.route('/game/labirint/left', methods=['POST'])
def labirint_game_left(a,x,y):
    if x-1==1:
        x=x-1
    else:
        print ("You can not go there")
    y=y

@app.route ('/game/labirint/up', methods=['POST'])
def labirint_game_up(a,x,y):
    if y+1==1:
        y=y+1
    else:
        print ("You can not go there")
    x=x

@app.route ('/game/labirint/down', methods=['POST'])
def labirint_game_down(a,x,y):
    if y-1==1:
        y=y-1
    else:
        print ("You can not go there")
    x=x

@app.route ('/game/labirint/observe', methods=['POST'])
def labirint_game_observe(a):
    print ("Перед вами рисунок лабиринта, который вас окружает. Вы находитесь в центральном поле")


if __name__ == '__main__':
    app.run(debug=True,port=8008)
