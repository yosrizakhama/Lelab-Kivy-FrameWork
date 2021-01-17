from kivy.app import App
from kivy.properties import ObjectProperty

from canvas_exemples import *
from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass

class LeLabApp(App):
    manager=ObjectProperty(None)
    def build(self):
        self.manager=MyScreenManager()
        #return CanvasExemples7()
        return self.manager
    pass


LeLabApp().run()

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
#
# class TutorialApp(App):
#     def build(self):
#         mylayout = BoxLayout(orientation="vertical")
#         mylabel = Label(text= "My App")
#         mybutton =Button(text="Click me!")
#         mylayout.add_widget(mylabel)
#         mybutton.bind(on_press= lambda a:print(mylabel.text))
#         mylayout.add_widget(mybutton)
#         return mylayout
# TutorialApp().run()