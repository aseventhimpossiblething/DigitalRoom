from flask import request
import os

def store():
    print("os listdir() - ",os.listdir())
    # os.chdir();
    #print("request-",request.files['sheet']);
    return str("os list --- ",os.listdir());
