from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line, Ellipse

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
Builder.load_file('canvas_exemples.kv')

class CanvasExemples1(Widget):
    pass

class CanvasExemples2(Widget):
    pass

class CanvasExemples3(Widget):
    pass

class CanvasExemples4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.w=self.width
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=(200,200),size=(200,200))
            Color(0, 1, 0)
            Line(rectangle=(50,50,100,100),width=2)
            Color(0, 0, 1)
            Line(circle=(550, 250, 100), width=2)
            Color(1, 1, 0)
            Line(points=(0, 0, self.w/4, 50,self.w/2,0,self.w*3/4,50,self.w,0), width=2)
        # Clock.schedule_interval(self.update,1/60)

    def mouve_rect(self):
        if self.rect.pos[0]+self.rect.size[0]+dp(10)<=self.width:
            self.rect.pos=(self.rect.pos[0]+dp(10),self.rect.pos[1])
        else:
            self.rect.pos = (self.width-self.rect.size[0] , self.rect.pos[1])

class CanvasExemples5(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.dir=1
        self.dir_y = 1
        with self.canvas:
            Color(1,0,0)
            self.ball = Ellipse(pos=(self.center_x, self.center_y), size= (dp(30),dp(30)))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self,*args):
        self.ball.pos = (self.center_x-self.ball.size[0]/2, self.center_y-self.ball.size[1]/2)

    def update(self,dt):
        p=dp(5)
        if self.dir == 1 :
            if self.ball.pos[0]+self.ball.size[0]+p<=self.width:
                self.ball.pos=(self.ball.pos[0]+p,self.ball.pos[1])
            else:
                self.dir *= -1
                self.ball.pos = (self.width - self.ball.size[0], self.ball.pos[1])
        else:
            if self.ball.pos[0]>=0:
                self.ball.pos=(self.ball.pos[0]-p,self.ball.pos[1])
            else:
                self.dir *= -1
                self.ball.pos = (0 , self.ball.pos[1])

        if self.dir_y == 1 :
            if self.ball.pos[1]+self.ball.size[1]+p<=self.height:
                self.ball.pos=(self.ball.pos[0],self.ball.pos[1]+p)
            else:
                self.dir_y *= -1
                self.ball.pos = (self.ball.pos[0], self.height-self.ball.size[1])
        else:
            if self.ball.pos[1]>=0:
                self.ball.pos=(self.ball.pos[0],self.ball.pos[1]-p)
            else:
                self.dir_y *= -1
                self.ball.pos = (self.ball.pos[0] , 0)

class CanvasExemples6(Widget):
    pass

class CanvasExemples7(BoxLayout):
    pass