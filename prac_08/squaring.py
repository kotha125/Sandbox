from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class SquareNumberApp(App):
    result_text = StringProperty()

    def build(self):
        self.result_text = ""
        return super().build()

    def handle_calculate(self, value):
        try:
            number = int(value)
            self.result_text = str(number ** 2)
        except ValueError:
            self.result_text = "Invalid input"