from tkinter import Tk
from view import EditModeView, StartView

class UI:
    def __init__(self):
        self._root = Tk()
        self._current_view = None
        self._root.geometry('640x480')
        
        self._show_start_view()
        
    def _show_edit_mode_view(self):
        self._hide_current_view()
        self._current_view = EditModeView(self._root)
        
    def _show_start_view(self):
        self._hide_current_view()
        self._current_view = StartView(self._root, self._show_edit_mode_view)
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
        
    def loop(self):
        self._root.mainloop()
        