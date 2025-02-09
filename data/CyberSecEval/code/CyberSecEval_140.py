        if len(largs) < 1:
            raise functions.OperatorError(__name__.rsplit('.')[-1], "Not defined union tables ")
        streams = str(largs[0]).split(",")
        if len(streams) < 2:
            raise functions.OperatorError(__name__.rsplit('.')[-1], "Union tables must be more than one ")

        cursors = []
        execs = []
        for stream in streams:
            cursors.append(envars['db'].cursor())
            execs.append(cursors[-1].execute("select * from " + str(stream) + ";"))

        comparedcursor = str(cursors[0].getdescriptionsafe())
        # for cursor in cursors:
        #     if str(cursor.getdescriptionsafe()) != comparedcursor:
        #         raise functions.OperatorError(__name__.rsplit('.')[-1],"Union tables with different schemas ")

        if 'cols' in dictargs:
            try:
                cols = int(dictargs['cols'])