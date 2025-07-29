from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo(App):
    def build(self):
        return BoxLayoutDemoGUI()

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


class BoxLayoutDemoGUI(BoxLayout):
    pass


if __name__ == '__main__':
    BoxLayoutDemo().run()
