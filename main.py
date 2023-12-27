from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class HelloWorldApp(MDApp):
    def build(self):
        # Create a screen
        screen = MDScreen()

        # Create a label widget with text "Hello, World!"
        label = MDLabel(
            text="Hello, World!",
            halign="center",  # Horizontal alignment (centered)
            theme_text_color="Secondary",  # Text color
            font_style="H2",  # Font style and size
        )

        # Add the label to the screen
        screen.add_widget(label)

        return screen

if __name__ == "__main__":
    HelloWorldApp().run()
