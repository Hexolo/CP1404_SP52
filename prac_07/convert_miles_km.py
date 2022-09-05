from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """ istanceConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ Construct the App """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Button that increase the number in text field by 1 or -1"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Get Valid Numeric Miles"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


DistanceConverterApp().run()
