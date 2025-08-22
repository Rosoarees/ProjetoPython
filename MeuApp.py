from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MainApp(App):
    def build(self):
       
        Window.clearcolor = get_color_from_hex('#2E3440')  
        
       
        label = Label(
            text="Fala Galera!",
            font_size='40sp',  
            size_hint=(.5, .5),
            pos_hint={"center_x": .5, "center_y": .5},
            color=get_color_from_hex('#88C0D0'),  
            bold=True
        )
        return label

if __name__ == "__main__":
    app = MainApp()
    app.run()