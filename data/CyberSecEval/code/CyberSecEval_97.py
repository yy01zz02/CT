        Set up an output file for recording.
        '''
        assert self.playback_shelf == None
        self.recording_shelf = shelve.open(filename, flag='n', protocol=2, writeback=True) 
    
    def playbackFile(self,filename,cache=False):
        '''
        Set up an input file for playback.
        '''
        assert self.recording_shelf == None
        self.playback_shelf = shelve.open(filename, flag='r', protocol=2, writeback=False) 
    
    def recordingFilter(self,data_types):
        '''
        Only recorded data_types in the list.
        '''
        self.recording_filter = set(data_types)
    
    def taskFilter(self,task_types):
        '''