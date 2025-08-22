from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
       
        button = Button(
            text="Clique aqui!",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
       
        button.bind(on_press=self.on_press_button)
        
        return button  
    
    def on_press_button(self, instance):
        print("Você apertou o botão!")

if __name__ == "__main__":
    app = ButtonApp()
    app.run()