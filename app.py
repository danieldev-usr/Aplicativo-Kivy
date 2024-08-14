import json
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.size = (400, 800)
        self.pos = (50, 50)
        
        layout = FloatLayout()
        
        background = Image(source='img.jpg', allow_stretch=True, keep_ratio=False,
                           size_hint=(1, 1))
        layout.add_widget(background)  # img↑
       
        label = Label(text="C.D.M - Ipatinga City",
                      size_hint=(None, None),
                      size=(200, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(label)
        
        button = Button(text="Clique aqui",
                        size_hint=(None, None),
                        size=(250, 50),
                        pos_hint={'center_x': 0.5, 'center_y': 0.1})
        button.bind(on_press=self.switch_to_screen2)
        layout.add_widget(button)
        
        self.add_widget(layout)
    
    def switch_to_screen2(self, instance):
        self.manager.current = 'screen2'

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        label = Label(text="ALUCARD REVOLUTIONARY",
                      size_hint=(None, None),
                      size=(200, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(label)
        
        button_layout = BoxLayout(orientation='vertical',
                                  size_hint=(None, None),
                                  size=(300, 500),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})
                                  
        button_texts = [
            "Polvora", "Pavio", "termite caseira", "Nitroglicerina"
        ]
        
        for text in button_texts:
            button = Button(text=text,
                            size_hint=(None, None),
                            size=(200, 50))
            button.bind(on_press=lambda instance, t=text: self.switch_to_screen(t))
            button_layout.add_widget(button)
        
        back_button = Button(text="Voltar",
                             size_hint=(None, None),
                             size=(200, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.1})
        back_button.bind(on_press=self.switch_to_screen1)
        layout.add_widget(button_layout)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def switch_to_screen(self, text, *args):
        print(f"Trocando para a tela com o texto: {text}")
        screen = self.manager.get_screen(text)
        if screen:
            screen.update_label_text(self.manager.textos.get(text, "Texto não encontrado"))
            self.manager.current = text
        else:
            print(f"Screen {text} não encontrada.")
    
    def switch_to_screen1(self, instance):
        self.manager.current = 'main'

class AdditionalScreen(Screen):
    def __init__(self, screen_name, **kwargs):
        super(AdditionalScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        self.label = Label(text="C.D.M!",
                           size_hint=(None, None),
                           size=(400, 400),
                           text_size=(400, None), 
                           halign='center', valign='middle',
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.label)
        
        back_button = Button(text="Voltar",
                             size_hint=(None, None),
                             size=(200, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.1})
        back_button.bind(on_press=self.switch_to_screen2)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def switch_to_screen2(self, instance):
        self.manager.current = 'screen2'
    
    def update_label_text(self, new_text):
        print(f"Atualizando texto para: {new_text}")
        self.label.text = new_text

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # JSON
        try:
            with open('textos.json', 'r') as f:
                sm.textos = json.load(f)
                print(f"JSON carregado: {sm.textos}")
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.")
            sm.textos = {}
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
            sm.textos = {}

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Screen2(name='screen2'))
        
        screen_names = [
            "Polvora", "Pavio", "termite caseira", "Nitroglicerina"
        ]
        
        for name in screen_names:
            text = sm.textos.get(name, "Texto não encontrado")
            print(f"Tela {name} carregada com o texto: {text}")
            screen = AdditionalScreen(name=name, screen_name=name)
            screen.update_label_text(text)
            sm.add_widget(screen)
        
        return sm

if __name__ == '__main__':
    MyApp().run()