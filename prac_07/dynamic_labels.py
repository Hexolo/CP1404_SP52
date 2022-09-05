from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Bob', 'Sam', 'Tyrone', 'Chris']

    def build(self):
        """Construct the App"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
