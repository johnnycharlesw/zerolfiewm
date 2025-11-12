class SessionManager:
    def __init__(self, wm):
        self.wm = wm
        
    def logout(self):
        self.wm.root.ungrab_key(self.display.keysym_to_keycode(XK.string_to_keysym("F1")), X.Mod1Mask)
        self.wm.display.close()
        
