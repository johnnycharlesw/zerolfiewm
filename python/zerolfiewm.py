# ZerolfieWM is a window manager for X11

from Xlib.display import Display
from Xlib import X, XK
import keybindings
import sessions
class ZerolfieWM:
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    X11_MOUSE_BUTTON_MASK = X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask

    def __init__(self) -> None:
        self.display: Display = Display()
        self.root = self.display.screen().root
        self.root.grab_key(self.display.keysym_to_keycode(XK.string_to_keysym("F1")), X.Mod1Mask, 1,
        X.GrabModeAsync, X.GrabModeAsync)

        for button in self.LEFT_BUTTON, self.RIGHT_BUTTON:
            self.grab_mouse_button(button, X.Mod1Mask, 1)
        
        self.start = None

    def grab_mouse_button(self, button: int, mask: int, detail: int) -> None:
        self.root.grab_button(button, mask, detail, self.X11_MOUSE_BUTTON_MASK,
        X.GrabModeAsync, X.GrabModeAsync, X.NONE, X.NONE)

    def tick(self):
        ev = self.display.next_event()
        if ev.type == X.KeyPress and ev.child != X.NONE:
            ev.child.configure(stack_mode = X.Above)
        elif ev.type == X.ButtonPress and ev.child != X.NONE:
            attr = ev.child.get_geometry()
            start = ev
        elif ev.type == X.MotionNotify and start:
            xdiff = ev.root_x - start.root_x
            ydiff = ev.root_y - start.root_y
            start.child.configure(
                x = attr.x + (start.detail == 1 and xdiff or 0),
                y = attr.y + (start.detail == 1 and ydiff or 0),
                width = max(1, attr.width + (start.detail == 3 and xdiff or 0)),
                height = max(1, attr.height + (start.detail == 3 and ydiff or 0)))
        elif ev.type == X.ButtonRelease:
            self.start = None
    def mainloop(self):
        while True:
            self.tick()

    def toggle_fullscreen(self, window):
        # Implement fullscreen toggle logic here
        pass

    def toggle_maximize(self, window):
        # Implement maximize toggle logic here
        pass

    def toggle_minimize(self, window):
        # Implement minimize toggle logic here
        pass

    def close_window(self, window):
        # Implement minimize toggle logic here
        pass

    def toggle_window_to_front(self, window):
        # Implement minimize toggle logic here
        pass

    def toggle_window_to_back(self, window):
        # Implement minimize toggle logic here
        pass

    def toggle_window_to_front(self, window):
        # Implement minimize toggle logic here
        pass

    def toggle_window_to_left(self,window):
        pass

    def toggle_window_to_right(self,window):
        pass

    def toggle_window_to_top(self,window):
        pass

    def toggle_window_to_center(self,window):
        pass

    def toggle_window_to_bottom_left(self,window):
        pass

    def toggle_window_to_top_right(self,window):
        pass

    def toggle_window_to_bottom_left(self,window):
        pass

    def toggle_window_to(self,window,corner):
        pass