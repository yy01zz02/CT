            g["erf"] = mathtools.erf
            g["erfc"] = mathtools.erfc

            if self.namespace is not None:
                if isinstance(self.namespace, dict):
                    g.update(self.namespace)
                else:
                    g.update(self.namespace.__dict__)

            g.update(parameters)
            self._func = eval("lambda (%s): (%s)" % (self.var, self.func), g)
            self._func.func_name = "%s -> %s" % (self.var, self.func)

    def __repr__(self):
        if callable(self.func):
            func_name = self.func.func_name
        else:
            func_name = "%s -> %s" % (self.var, self.func)
        return "<Curve %s>" % func_name
