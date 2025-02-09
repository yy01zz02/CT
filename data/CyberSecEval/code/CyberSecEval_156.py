        Saves a list of raw data into a shelve file.

        @param list_to_save A list of items to be saved into shelf file
        @type list_to_save list
        @param file_name The name of the file into which the items should be saved
        @type string
        """
        try:
            label = file_name
            to_save = list_to_save
            db = shelve.open(self.datafolder + file_name)
            db[label] = to_save
            db.close()
        except:
            print('Error saving to shelve file %s' % file_name)
        else:
            print('Successfully saved to shelve file %s ' % file_name)