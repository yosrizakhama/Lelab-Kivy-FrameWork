from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = []
    def push(self,screen):

        if not(self.current in self.screen_stack):
            self.screen_stack.append(self.current)
        else:
            self.screen_stack.remove(self.current)
            self.screen_stack.append(self.current)
        self.current = screen
        print(self.screen_stack)
        pass
    def pop(self):
        if not(self.screen_stack == []):
            self.current = self.screen_stack[-1]
            del(self.screen_stack[-1])
            print(self.current)
            print(self.screen_stack)

        pass
