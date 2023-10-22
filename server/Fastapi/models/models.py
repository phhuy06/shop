from pydantic import BaseModel


def successResponse(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def errorResponse(error, code, message):
    return {"error": error, "code": code, "message": message}