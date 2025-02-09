
    @globals.setter
    def globals(self, value):
        self._globals = value


a = MyClass()

locals = {}

exec("a = 1" ,a.globals, locals)

print "globals = {0}".format([g for g in a.globals if not g.startswith("__")])
print "locals = {0}".format(locals)

exec("a += 1", a.globals, locals)

print "globals = {0}".format([g for g in a.globals if not g.startswith("__")])
print "locals = {0}".format(locals)
