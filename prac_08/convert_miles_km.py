from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.output_text = "0.0"
        return super().build()

    def handle_convert(self, value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.output_text = str(km)

    def handle_increment(self, value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0
        miles += 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(miles)

    def handle_decrement(self, value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0
        miles -= 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(miles)
