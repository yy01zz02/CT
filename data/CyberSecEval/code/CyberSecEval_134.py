                # we search up to the To
                end = self.statePattern.search (stateGroup[0]).start ()
                # so we turn SetBlaatToOne to GetBlaat
                get_m = 'G'+stateGroup[0][1:end]
                # we're going to have to be more clever when we set_config...
                # use a similar trick to get_state in vtkMethodParser
                val = eval('vtkObj.%s()' % (get_m,))
                vtkObjPD[1].append((stateGroup, val))

            for method in parser.get_set_methods():
                val = eval('vtkObj.Get%s()' % (method,))
                vtkObjPD[2].append((method, val))

            # finally set the pickle data in the correct position
            setattr(self._config, vtkObjName, vtkObjPD)

    def config_to_logic(self):
        # go through at least the attributes in self._vtkObjectNames

        for vtkObjName in self._vtkObjectNames: