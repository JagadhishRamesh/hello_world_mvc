from model import HelloWorldModel
from view import HelloWorldView


class HelloWorldController:
    def __init__(self):
        self.model = HelloWorldModel()
        self.view = HelloWorldView()

    def get_message(self):
        message = self.model.get_message()
        return self.view.display_message(message)