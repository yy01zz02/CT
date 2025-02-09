                dlg =  QtGui.QInputDialog(self)                 
                dlg.setInputMode( QtGui.QInputDialog.TextInput) 
                dlg.setLabelText("Command")
                dlg.setTextValue('ffmpeg -y -f image2 -i image%04d.png klampt_record.mp4')
                dlg.resize(500,100)                             
                ok = dlg.exec_()                                
                cmd = dlg.textValue()
                #(cmd,ok) = QtGui.QInputDialog.getText(self,"Process with ffmpeg?","Command", text='ffmpeg -y -f image2 -i image%04d.png klampt_record.mp4')
                if ok:
                    import os,glob
                    os.system(str(cmd))
                    print "Removing temporary files"
                    for fn in glob.glob('image*.png'):
                        os.remove(fn)
        def movie_update(self):
            sim = self.getSimulator()
            if sim != None:
                while sim.getTime() >= self.movie_time_last + 1.0/30.0:
                    self.glwidget.program.save_screen('image%04d.png'%(self.movie_frame))
                    self.movie_frame += 1