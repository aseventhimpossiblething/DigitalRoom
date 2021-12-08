from flask import request

def store():
    print("request-",request.files['sheet']);
    return str(request.files['sheet']);
