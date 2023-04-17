from fastapi import FastAPI
from controller import HelloWorldController

app = FastAPI()
helloworld_controller = HelloWorldController()


@app.get('/')
def hello_world():
    return helloworld_controller.get_message()

