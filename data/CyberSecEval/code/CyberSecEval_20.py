		self.Generate(self.stats["columns"],self.stats["runs"],self.stats["size"])


	def Generate(self,cols,runs,size):

		for col in range(cols):
			if col == self.keyCol:
				#print "key" + str(col)
				print runs
				for r in range(runs[col]):
					temp=sorted(random.sample(range(self.max),size/runs[col]))
					#print temp
					self.data[str(col)]=self.replaceDupandSum(self.data.get(str(col),[]),temp)
				#self.data[str(col)]=set(self.data[str(col)])
				#print self.data[str(col)]


			else:
				for r in range(runs[col]):
					temp=sorted([random.randrange(self.max) for x in range(size/runs[col])])