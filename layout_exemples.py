from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file('layout_exemples.kv')
class MainWidget(Widget):
    pass

class BoxLayoutExemple(BoxLayout):
    pass
    '''def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text = "A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)'''

class AnchorLayoutExemple(AnchorLayout):
    pass

# class GridLayoutExemple(GridLayout):
#     pass

class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="rl-bt"
        for i in range(100):
            b=Button(text = str(i),size_hint = (None,None),size = (dp(50),dp(50)))
            self.add_widget(b)