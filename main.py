from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask( __name__)
app.config[ 'SECRET_KEY'] = 'vnkdjnfjknfl1232#'
soc = SocketIO( app)


@app.route('/')
def sessions():
    return render_template('session.html')


def message_received( methods = [ 'GET', 'POST']):
    print( 'Message received successfully!')


@soc.on('my event')
def handle_custom_event( json, methods = [ 'GET', 'POST']):
    print('Received my event', str( json))
    soc.emit( 'my response', json, callback = message_received)
    

if __name__ == '__main__':
    soc.run( app, debug = True)
