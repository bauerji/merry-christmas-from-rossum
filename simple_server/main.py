import requests

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    text: str
    local_address: str


class Response(BaseModel):
    status: str


def call_rossum_display(request: Request) -> Response:
    response = requests.get(request.local_address, {"text": request.text})
    return Response(**response.json())


@app.post("/")
async def root(request: Request):
    return call_rossum_display(request)
