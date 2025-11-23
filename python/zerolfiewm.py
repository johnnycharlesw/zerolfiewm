# ZerolfieWM is a window manager for X11

from Xlib.display import Display
from Xlib import X, XK
from Xlib.ext import randr as RandR

import keybindings
import sessions
class ZerolfieWM:
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    X11_MOUSE_BUTTON_MASK = X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask
    TOP = [1,0,0,0]
    BOTTOM = [0,1,0,0]
    CENTER = [0.5,0.5,0,0]
    BACK = [0,0,1,0]
    LEFT = [0,0,0,-1]
    RIGHT = [0,0,0,1]
    TOP_LEFT = [0,0,-1,-1]
    TOP_RIGHT = [0,0,1,-1]


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
        event = self.display.next_event()
        if event.type == X.KeyPress:
            self.handle_keypress(event)
        elif event.type == X.ButtonPress:
            self.handle_mouse_press(event)
        elif event.type == X.MotionNotify and self.start:
            self.handle_mouse_move(event)
        elif event.type == X.ButtonRelease:
            self.start = None
        elif event.type == RandR.ScreenChangeNotify:
            pass

    
    def handle_mouse_press(self, event):
        if event.child != X.NONE:
            attr = event.child.get_geometry()
            self.start = event

    def handle_mouse_release(self, event):
        self.start = None

    def handle_keypress(self, event: X.KeyPressEvent) -> None:
        if event.child != X.NONE:
            event.child.configure(stack_mode = X.Above)

    def handle_mouse_move(event: X.MotionNotify):
        xdiff = event.root_x - start.root_x
        ydiff = event.root_y - start.root_y
        self.start.child.configure(
            x = attr.x + (start.detail == 1 and xdiff or 0),
            y = attr.y + (start.detail == 1 and ydiff or 0),
            width = max(1, attr.width + (start.detail == 3 and xdiff or 0)),
            height = max(1, attr.height + (start.detail == 3 and ydiff or 0))
        )

    def resize_and_move_to_corner(window: Window, corner):
        attr = window.get_geometry()
        window.configure(
            x = attr.x + (corner[0] * attr.width),
            y = attr.y + (corner[1] * attr.height),
            width = max(1, attr.width + (corner[2] * attr.width)),
            height = max(1, attr.height + (corner[3] * attr.height))
        )

    def resize(window: Window, width, height):
        attr = window.get_geometry()
        window.configure(
            width = max(1, width),
            height = max(1, height)
        )

    def move(window: Window, x, y):
        attr = window.get_geometry()
        window.configure(
            x = x,
            y = y
        )

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
        # Implement window closing logic here
        pass

    def toggle_window_to_back(self, window):
        # Implement minimize toggle logic here
        self.toggle_window_to(window, self.BACK)

    def toggle_window_to_front(self, window):
        # Implement minimize toggle logic here
        self.toggle_window_to(window, self.FRONT)

    def toggle_window_to_left(self,window):
        self.toggle_window_to(window, self.LEFT)

    def toggle_window_to_right(self,window):
        self.toggle_window_to(window, self.RIGHT)

    def toggle_window_to_top(self,window):
        self.toggle_window_to(window, self.TOP)

    def toggle_window_to_center(self,window):
        self.toggle_window_to(window, self.CENTER)

    def toggle_window_to_bottom_left(self,window):
        self.toggle_window_to(window, self.TOP_LEFT)

    def toggle_window_to_top_right(self,window):
        self.toggle_window_to(window, self.TOP_RIGHT)

    def toggle_window_to(self,window,corner):
        
        pass