class ZerolfieWM_WebViewApi:
    def __init__(self, wm):
        self.wm = wm
    
    def closeWindow(self):
        self.wm.close_window_attached_to_titlebar()

    def minimizeWndow(self):
        self.wm.minimize_window_attached_to_titlebar()

    def maximizeWindow(self):
        self.wm.maximize_window_attached_to_titlebar()