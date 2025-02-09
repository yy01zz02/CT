    def run_lint(self, _=None):
        """launches pylint"""
        colors = {'W:':'red1', 'E:': 'red4',
                  'W:': 'red3', '**': 'navy'}
        
        self.root.configure(cursor='watch')
        self.results.focus_set()
        self.results.delete(0, END)
        self.results.update()
        module = self.txtModule.get()
        pout = os.popen('%s %s' % (PYLINT, module), 'r')
        for line in  pout.xreadlines():
            line = line.rstrip()
            self.results.insert(END, line)
            fg_color = colors.get(line[:2], 'black')
            self.results.itemconfigure(END, fg=fg_color)
            self.results.update()
        self.root.configure(cursor='')

def Run(args):