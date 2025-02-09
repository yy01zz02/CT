
            self._exclude = exclude

            index = data.index()
            if "ey" in data.sig and "eyl" in data.sig:
                values = numpy.empty((len(data.values), 4))
                values[:,0] = data.values[:,index["x"]]
                values[:,1] = data.values[:,index["y"]]
                values[:,2] = data.values[:,index["ey"]]
                values[:,3] = data.values[:,index["eyl"]]
                return eval("lambda %s: sum([method(f, x, y, ey, eyl) for f, (x, y, ey, eyl) in itertools.izip(curve(values[:,0], **{%s}), values) if not exclude(x, y, ey, eyl)])" % (", ".join(parnames), ", ".join(["\"%s\": %s" % (x, x) for x in parnames])), {"method": method, "itertools": itertools, "curve": self, "values": values, "exclude": exclude})

            elif "ey" in data.sig:
                values = numpy.empty((len(data.values), 3))
                values[:,0] = data.values[:,index["x"]]
                values[:,1] = data.values[:,index["y"]]
                values[:,2] = data.values[:,index["ey"]]
                return eval("lambda %s: sum([method(f, x, y, ey) for f, (x, y, ey) in itertools.izip(curve(values[:,0], **{%s}), values) if not exclude(x, y, ey)])" % (", ".join(parnames), ", ".join(["\"%s\": %s" % (x, x) for x in parnames])), {"method": method, "itertools": itertools, "curve": self, "values": values, "exclude": exclude})

            else: