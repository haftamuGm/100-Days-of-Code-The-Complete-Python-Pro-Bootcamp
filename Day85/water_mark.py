import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Color, Rectangle, InstructionGroup, Ellipse
from kivy.uix.label import Label

kivy.require('2.1.0')


class WatermarkApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # File chooser to select image
        self.filechooser = FileChooserIconView(size_hint_y=None, height=200)
        self.layout.add_widget(self.filechooser)

        # Text input for watermark
        self.watermark_input = TextInput(hint_text="Enter watermark text", size_hint_y=None, height=40)
        self.layout.add_widget(self.watermark_input)

        # Button to apply watermark
        self.apply_button = Button(text="Apply Watermark", size_hint_y=None, height=50)
        self.apply_button.bind(on_press=self.apply_watermark)
        self.layout.add_widget(self.apply_button)

        # Label for status
        self.status_label = Label(text="Select an image and apply watermark.", size_hint_y=None, height=40)
        self.layout.add_widget(self.status_label)

        # Image display
        self.img_widget = Image(size_hint=(1, 1), allow_stretch=True)
        self.layout.add_widget(self.img_widget)

        return self.layout

    def apply_watermark(self, instance):
        image_path = self.filechooser.selection[0]
        watermark_text = self.watermark_input.text

        if not image_path or not watermark_text:
            self.status_label.text = "Please select an image and enter a watermark."
            return

        # Load the image into the widget
        self.img_widget.source = image_path
        self.img_widget.reload()  # Refresh the image

        # Add watermark text using Kivy's canvas
        self.add_watermark(watermark_text)

    def add_watermark(self, watermark_text):
        # Clear previous canvas instructions if any
        self.img_widget.canvas.clear()

        # Create a new canvas instruction group for watermark drawing
        with self.img_widget.canvas:
            instruction_group = InstructionGroup()

            # Set the watermark color (white) with transparency
            Color(1, 1, 1, 0.5)  # RGBA format, here 0.5 is for transparency

            # Draw watermark text (positioning at the bottom-right corner)
            instruction_group.add(
                Rectangle(size=(self.img_widget.width, self.img_widget.height), pos=(0, 0))
            )

            # Using Label to display text and position it on the image canvas
            label = Label(text=watermark_text, font_size=40, color=(1, 1, 1, 0.5), size_hint=(None, None))
            label.size = label.texture_size  # Adjust the label size based on its text
            label.pos = (self.img_widget.width - label.width - 10, 10)  # Bottom-right position

            # Draw the label on canvas (watermark text)
            instruction_group.add(label.canvas)

            # Adding the instruction group to the image widget's canvas
            self.img_widget.canvas.add(instruction_group)

        # Update status after applying watermark
        self.status_label.text = f"Watermark '{watermark_text}' applied!"


if __name__ == "__main__":
    WatermarkApp().run()
