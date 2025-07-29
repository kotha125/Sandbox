from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.root = BoxLayout()
        names = ["Alice", "Bob", "Charlie", "Dana"]

        main_box = BoxLayout(orientation='vertical')
        for name in names:
            label = Label(text=name)
            main_box.add_widget(label)

        self.root.add_widget(main_box)
        return self.root
