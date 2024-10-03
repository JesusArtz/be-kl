import base64
from uuid import uuid4

def processImage(image):

    string = image
    encript = uuid4()
    route = f"static/images/{encript}.png"

    with open(route, "wb") as fh:
        fh.write(base64.b64decode(string))

    return f"/{route}"