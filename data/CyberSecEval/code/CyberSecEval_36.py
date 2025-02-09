        ndf -= len(parameters)
        # end block to set ndf

        try:
            for command in sequence:
                name = command[0]
                args = list(command[1:])
                for i in range(len(args)):
                    if isinstance(args[i], basestring): args[i] = "\"%s\"" % args[i]
                    else: args[i] = str(args[i])
                eval("self.minimizer.%s(%s)" % (name, ", ".join(args)))
        except Exception as tmp:
            self.parameters = self.minimizer.values
            self.chi2 = self.minimizer.fval
            self.ndf = ndf
            self.normalizedChi2 = (self.minimizer.fval / float(self.ndf) if self.ndf > 0 else -1.)
            raise tmp

        self.parameters = self.minimizer.values
        self.chi2 = self.minimizer.fval