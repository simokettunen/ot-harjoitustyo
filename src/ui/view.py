from tkinter import ttk, Text, Canvas, OptionMenu, StringVar

class View:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        
    def destroy(self):
        self._frame.destroy()
        
class StartView(View):
    def __init__(self, root, service, go_to_edit):
        
        super().__init__(root)
        self._service = service
        self._go_to_edit = go_to_edit
        
        button_new_model = ttk.Button(
            master=self._frame,
            text='New model',
            command=self._go_to_edit,
        )
        
        button_load_model = ttk.Button(
            master=self._frame,
            text='Load model',
            command=self._handle_load_button_click
        )
        
        button_new_model.pack()

        options = self._service.get_list_of_bnfs()
        
        if len(options) > 0:
            self._dropdown_variable = StringVar()
            self._dropdown_variable.set('Models')
        
            dropdown_load_model = OptionMenu(
                self._frame,
                self._dropdown_variable,
                *options,
            )
            button_load_model.pack()
            dropdown_load_model.pack()
            
        self._frame.pack()

    def _handle_load_button_click(self):
        bnf_id = self._dropdown_variable.get()
        self._service.load_bnf(bnf_id)
        self._go_to_edit()
        
class EditModeView(View):
    def __init__(self, root, service, go_to_start):
        super().__init__(root)
        self._bnf = None
        self._service = service
        self.syntax_error_label = None
        self._go_to_start = go_to_start
        
        button_back = ttk.Button(
            master=self._frame,
            text='Back',
            command=self._go_to_start,
        )
        button_back.grid(row=0, column=2)
        
        button_draw = ttk.Button(
            master=self._frame,
            text='Draw',
            command=self._handle_draw_button_click,
        )
        button_draw.grid(row=0, column=0)
        
        button_save = ttk.Button(
            master=self._frame,
            text='Save drawn model',
            command=self._handle_save_button_click,
        )
        button_save.grid(row=0, column=1)
        
        self.textarea = Text(
            master=self._frame,
            width=40,
        )
        self.textarea.grid(row=1, column=0, sticky='n')
        
        self.is_correct_syntax = True
        self.no_unassigned_nonterminals = True
        
        self.canvas = Canvas(
            master=self._frame,
            width=600,
            height=800,
            bg='white'
        )
        
        if self._service.bnf:
            self.textarea.insert('end-1c', self._service.bnf.__str__())
            
        self.canvas.grid(row=1, column=1)
        
        self._frame.pack()
  
    def _draw_sequence(self, line, cum_x, y):
        
        dx = 20     # distance between label boxes
        margin = 4  # label box margin
    
        for i in range(len(line.symbols)):
            type = line.symbols[i].type
            label = line.symbols[i].label
        
            # from left split to label box
            self.canvas.create_line(cum_x, y, cum_x + dx, y)
            cum_x += dx
            
            text = self.canvas.create_text(cum_x + margin, y, text=label, anchor='w')
            text_bbox = self.canvas.bbox(text)
            text_width = text_bbox[2] - text_bbox[0]
            
            if type == 'non-terminal':
                # label box right side
                x2 = cum_x + margin + text_width + margin
                
                self.canvas.create_rectangle(cum_x, y-10, x2, y+10, outline='#000000')
            elif type == 'terminal':
                # label box right side
                x2 = cum_x + max(margin + text_width + margin, 20)
                
                self.canvas.create_oval(cum_x, y-10, x2, y+10, outline='#000000')
                
            if i == len(line.symbols) - 1:
                self.canvas.create_line(x2, y, x2+dx, y)
                cum_x = x2 + dx
                
            else:
                cum_x = x2
                
        return cum_x
        
    def _draw_line(self, rule, y):
        x = 30          # starting distance from left
        r = 5           # circle radius
        dx = 15         # distance between circle and split
        dy = 30         # distance between rows
        x_cum = x        # cumulative x
        
        label = self.canvas.create_text(x_cum, y, text=rule.symbol, anchor='w')
        label_bbox = self.canvas.bbox(label)
        label_width = label_bbox[2] - label_bbox[0]
        
        x_cum += label_width + 20
        
        # left circle
        self.canvas.create_oval(x_cum-r, y-r, x_cum+r, y+r, fill='#000000')
        
        x_cum += r   # cumulative x
        
        # from left circle to left split
        self.canvas.create_line(x_cum, y, x_cum + dx, y)
        
        x_cum += dx
        x_cums = []
        
        for i in range(len(rule.sequences)):
            x_cum2 = self._draw_sequence(rule.sequences[i], x_cum, y+dy*i)
            
            # from left split top to left split bottom
            self.canvas.create_line(x_cum, y, x_cum, y+dy*i)
            
            x_cums.append(x_cum2)
            
        x_cum = max(x_cums)
        
        for i in range(len(rule.sequences)):
            
            # from sequence's last label to split
            self.canvas.create_line(x_cums[i], y+dy*i, x_cum, y+dy*i)
            
            # from right split bottom to right split top
            self.canvas.create_line(x_cum, y+dy*i, x_cum, y)
        
        # from right split to right circle
        self.canvas.create_line(x_cum, y, x_cum+dx, y)
        
        # right circle
        self.canvas.create_oval(x_cum+dx+r-r, y-r, x_cum+dx+r+r, y+r, fill='#000000')
        
        return y + dy*len(rule.sequences)
        
    def _draw_model(self, rule):
    
        # starting distance from the top
        y = 30
        
        self.canvas.delete('all')
        
        for line in rule:
            y = self._draw_line(line, y)
        
    def _handle_draw_button_click(self):

        # TODO: refactor this method

        if self.syntax_error_label:
            self.syntax_error_label.destroy()
        
        input = self.textarea.get('1.0', 'end-1c')
        self.is_correct_syntax = self._service.create_bnf(input)
        self.no_unassigned_nonterminals = True
        
        if self.is_correct_syntax:
            self._draw_model(self._service.bnf.rules)
            self.no_unassigned_nonterminals = self._service.bnf.check_unassigned_nonterminals()
            
            if not self.no_unassigned_nonterminals:
                self.syntax_error_label = ttk.Label(
                    master=self._frame,
                    text='Unassigned non-terminal appears in the model',
                )
            
                self.syntax_error_label.grid(row=1, column=0)
        else:
            self.syntax_error_label = ttk.Label(
                master=self._frame,
                text='Syntax error',
            )
        
            self.syntax_error_label.grid(row=1, column=0)
            
    def _handle_save_button_click(self):
        self._service.save_bnf()
