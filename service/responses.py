
def success_response(statusCode,message,data):
    return{
        "status": statusCode,
        "message": message,
        "data": data
    }

def error_response(statusCode,message):
    return{
        "status": statusCode,
        "message": message
    }

def onlySuccessResponseWithoutData(statusCode,message):
    return{
        "status": statusCode,
        "message": message
    }