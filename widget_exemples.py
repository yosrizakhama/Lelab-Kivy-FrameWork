from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

Builder.load_file('widget_exemples.kv')

class WidgetExemple(GridLayout):
    text = StringProperty("Bonjour")
    compteur = 0
    toggle=BooleanProperty(False)
    # slide_value=StringProperty("50")
    name = StringProperty("TOTO")
    def click_button(self):
        if self.toggle:
            self.compteur+=1
            self.text = "Click N:" + str(self.compteur)

    def state_change(self,widget):
        self.toggle=not self.toggle
        widget.text = "OFF"
        if widget.state=="down":
            widget.text="ON"

    def swith_on_active(self,widget):
        print(str(widget.active))

    def on_slide_value(self, widget):
        i = int(widget.value)
        print(f"la valeaur du slide est : {i}")
        # self.slide_value = str(i)
        # pass
    def on_text_validate(self, widget):
        self.name = widget.text

class MyImage(Image):
    im = Image(source='images/donut.gif')
    # -- do something --
    im.reload()