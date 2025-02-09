            self._level = None
        def run(self):
            for display, co in self.codeblocks:
                if not getattr(self, 'no_echo', False):
                    shown = [getattr(sys, 'ps1', '>>> ') + display[0]]
                    shown.extend([getattr(sys, 'ps2', '... ') + l
                                          for l in display[1:]])
                    Deck._add_history(''.join(display).rstrip())
                    print ''.join(shown).rstrip()
                try:
                    exec co in environ
                except:
                    traceback.print_exc()
        def __str__(self):
            return ''.join(self.lines)
        def _append(self, line):
            self.lines.append(line)
            if not self._stack and line.isspace():
                return
            indent = len(line) - len(line.lstrip())