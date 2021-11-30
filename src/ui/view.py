from tkinter import ttk, Text, Canvas
from bnf import check_syntax, BNF

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
        button.grid(row=0, column=0)
        
        self.textarea = Text(
            master=self._frame,
            width=40,
        )
        self.textarea.grid(row=1, column=0)
        
        self.is_correct_syntax = True
        
        self.canvas = Canvas(
            master=self._frame,
            width=600,
            height=300,
            bg='white'
        )
        
        self.canvas.grid(row=1, column=1)
        
        self._frame.pack()
  
    def _draw_sequence(self, line, sx, y):
        
        k2 = 20
        margin = 4
    
        for i in range(len(line)):
            type = line[i]['type']
            label = line[i]['label']
        
            self.canvas.create_line(sx, y, sx + k2, y)
            sx += k2
            
            a = self.canvas.create_text(sx + margin, y, text=label, anchor='w')
            
            text_bbox = self.canvas.bbox(a)
            text_width = text_bbox[2] - text_bbox[0]
            
            x1 = sx
            y1 = y - 10
            y2 = y + 10
            
            if type == 'non-terminal':
                x2 = sx + margin + text_width + margin
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='#000000')
            elif type == 'terminal':
                x2 = sx + max(margin + text_width + margin, 20)
                self.canvas.create_oval(x1, y1, x2, y2, outline='#000000')
            
            if i == len(line) - 1:
                self.canvas.create_line(x2, y, x2+k2, y)
                sx = x2 + k2
            else:
                sx = x2
                
        return sx
        
    def _draw_line(self, rule, y):
        x = 30
        r = 5
        k1 = 15
        
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='#000000')
        
        sx = x + r
        
        self.canvas.create_line(sx, y, sx + k1, y)
        
        sx += k1
        
        sxs = []
        for i in range(len(rule)):
            sx2 = self._draw_sequence(rule[i], x+r+k1, y+30*i)
            self.canvas.create_line(sx, y, sx, y+30*i)
            
            sxs.append(sx2)
            
        sx = max(sxs)
        for i in range(len(rule)):
            self.canvas.create_line(sxs[i], y+30*i, sx, y+30*i)
            self.canvas.create_line(sx, y+30*i, sx, y)
            
        self.canvas.create_line(sx, y, sx+k1, y)
        
        self.canvas.create_oval(sx+k1+r-r, y-r, sx+k1+r+r, y+r, fill='#000000')
        
        return y + 30*len(rule)
        
    def _draw_rule(self, rule):
        y = 30
        
        self.canvas.delete('all')
        
        for line in rule:
            y = self._draw_line(line, y)
        
    def _handle_button_click(self):
        if not self.is_correct_syntax:
            self.syntax_error_label.destroy()
        
        input = self.textarea.get('1.0', 'end-1c')
        self.is_correct_syntax = check_syntax(input)
        
        if self.is_correct_syntax:
            bnf = BNF()
            bnf.create_from_string(input)
            print(bnf.lines)
            self._draw_rule(bnf.lines)
        else:
            self.syntax_error_label = ttk.Label(
                master=self._frame,
                text='Syntax error',
            )
        
            self.syntax_error_label.grid(row=2, column=0)