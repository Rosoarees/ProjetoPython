from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import sp  

class CalculatorApp(App):
    def build(self):
        
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
      
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
      
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
       
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=sp(70),  
            size_hint=(1, 0.4),  
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1),
            text="0",
            padding=[20, 20]  
        )
        main_layout.add_widget(self.solution)
 
        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=5, size_hint=(1, 0.12)) 
            for label in row:
             
                if label == "=":
                    bg_color = (0, 0.7, 0, 1)
                elif label in ["C", "⌫"]:
                    bg_color = (1, 0.3, 0.3, 1)
                elif label in self.operators or label == "%":
                    bg_color = (1, 0.5, 0, 1)
                else:
                    bg_color = (0.2, 0.2, 0.2, 1)
                
                button = Button(
                    text=label,
                    font_size=sp(30),
                    background_color=bg_color,
                    color=(1, 1, 1, 1),
                    bold=True
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if current == "0" and button_text not in self.operators and button_text not in ["C", "⌫", "=", "%"]:
            current = ""
        
        if button_text == "C":
            self.solution.text = "0"
            self.last_was_operator = None
            self.last_button = None
            
        elif button_text == "⌫":
            if len(current) > 1:
                self.solution.text = current[:-1]
            else:
                self.solution.text = "0"
                
        elif button_text == "%":
            if current and current != "0":
                try:
                    result = str(float(current) / 100)
                    self.solution.text = result
                except:
                    self.solution.text = "Erro"
                    
        elif button_text == "=":
            self.calculate_result()
            
        elif button_text in self.operators:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "0" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
                self.last_button = button_text
                self.last_was_operator = True
                
        else:
            if button_text == "." and "." in current.split(self.operators[-1])[-1]:
                return
            
            new_text = current + button_text
            self.solution.text = new_text
            self.last_button = button_text
            self.last_was_operator = False
    
    def calculate_result(self):
        try:
            expression = self.solution.text.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
            
            self.solution.text = str(result)
            self.last_was_operator = False
            self.last_button = self.solution.text[-1] if self.solution.text else None
            
        except ZeroDivisionError:
            self.solution.text = "Erro: Divisão por zero"
        except Exception as e:
            self.solution.text = "Erro"

if __name__ == "__main__":
    CalculatorApp().run()clear
    