            string = string[1:-1]
        else:
            raise ValueError("Invalid Part string: "+string)
        typ = string[:2]
        string = string[3:]
        if not typ in ("n1", "n2", "bg", "ch", "ge"):
            raise ValueError("Invalid Part Type string: "+typ)
        valstrings = str.split(string, "-")
        inten = eval(valstrings[0])
        size = eval(valstrings[1])
        gen = eval(valstrings[2])
        cho = eval(valstrings[3])
        return cls(typ, inten, size, gen, cho)
    
    def getTheme(self, pal):
        if self._type == "n1":
            return pal._n1
        if self._type == "n2":
            return pal._n2
        if self._type == "bg":