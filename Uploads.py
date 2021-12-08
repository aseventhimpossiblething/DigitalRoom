import request

def store():
    print("request-",request.files['sheet']);
    return request.files['sheet'];
