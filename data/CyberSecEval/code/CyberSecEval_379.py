    pickle.dump(to_save,f)
    f.close()

  def save_def(self,filename):
    self.net_def.save(filename+'.modeldef')

  def load(self,filename):
    self._init_graph_sess()
    self.load_def(filename)
    f=open(filename+'.model','rb')
    data_dict=pickle.load(f)
    f.close()
    if self.has_built():
      with self._graph.as_default():
        op = self.initializer.op_by_value_table(data_dict)
      self.run(op)

  def load_def(self,filename):
    self.net_def.load(filename+'.modeldef')
