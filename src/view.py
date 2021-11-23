from tkinter import ttk, Text
from bnf import check_syntax

class View:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        
    def destroy(self):
        self._frame.destroy()
        
class StartView(View):
    def __init__(self, root, command):
        
        super().__init__(root)
        
        button1 = ttk.Button(
            master=self._frame,
            text='Load model',
        )
        
        button2 = ttk.Button(
            master=self._frame,
            text='New model',
            command=command,
        )
        button1.pack()
        button2.pack()
        
        self._frame.pack()
        
class EditModeView(View):
    def __init__(self, root):
        super().__init__(root)
        
        button = ttk.Button(
            master=self._frame,
            text='Draw',
            command=self._handle_button_click,
        )
        button.pack()
        
        self.textarea = Text(
            master=self._frame,
            width=40,
        )
        self.textarea.pack()
        
        self.is_correct_syntax = True
        
        self._frame.pack()
        
    def _handle_button_click(self):
        if not self.is_correct_syntax:
            self.syntax_error_label.destroy()
        
        input = self.textarea.get('1.0', 'end-1c')
        self.is_correct_syntax = check_syntax(input)
        
        if not self.is_correct_syntax:
            self.syntax_error_label = ttk.Label(
                master=self._frame,
                text='Syntax error',
            )
        
            self.syntax_error_label.pack()