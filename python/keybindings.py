# Keybindings for ZerolfieWM
from Xlib.display import Display
from Xlib import X, XK
from zerolfiewm import ZerolfieWM
class Keybindings:
    def __init__(self, wm: ZerolfieWM): # ZerolfieWM class helper for keybindings
        self.bindings = {
            XK.string_to_keysym("F1"): self.wm.toggle_fullscreen,
            XK.string_to_keysym("F2"): self.wm.toggle_maximize,
            XK.string_to_keysym("F3"): self.wm.toggle_minimize,
            XK.string_to_keysym("F4"): self.wm.close_window,
            XK.string_to_keysym("F5"): self.wm.toggle_window_to_front,
            XK.string_to_keysym("F6"): self.wm.toggle_window_to_back,
            XK.string_to_keysym("F7"): self.wm.toggle_window_to_top,
            XK.string_to_keysym("F8"): self.wm.toggle_window_to_bottom,
            XK.string_to_keysym("F9"): self.wm.toggle_window_to_left,
            XK.string_to_keysym("F10"): self.wm.toggle_window_to_right,
            XK.string_to_keysym("F11"): self.wm.toggle_window_to_center,
            XK.string_to_keysym("F12"): self.wm.toggle_window_to_top_left,
            XK.string_to_keysym("F13"): self.wm.toggle_window_to_top_right,
            XK.string_to_keysym("F14"): self.wm.toggle_window_to_bottom_left
        }
    
    def handle_keypress(self, ev: X.KeyPressEvent) -> None:
        keysym = self.display.keycode_to_keysym(ev.detail, 0)
        if keysym in self.bindings:
            # Find the focused window (simplified)
            focused_window = ev.child if ev.child != X.NONE else None
            if focused_window:
                self.bindings[keysym](focused_window)