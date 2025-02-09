			file = open(os.path.join(IndexDir,fileName),"w")
			pickle.dump(source,file)

		pickleDumpToFile(self.idToUrl,"idToUrl")
		pickleDumpToFile(self.invertedIndex,"inverted")
		pickleDumpToFile(self.forwardIndex,"forward")

	def loadFromDisk(self,indexDir):
		def pickleLoadFromFile(fileName):
			file = open(os.path.join(indexDir,fileName),"r")
			return pickle.load(file)
		self.invertedIndex=pickleLoadFromFile("inverted")
		self.idToUrl=pickleLoadFromFile("idToUrl")
		self.forwardIndex=pickleLoadFromFile("forward")

	def getDocumentOfQuery(self,query):
		return self.invertedIndex.get(query,[])

	def getDocumentOfId(self,id):
		return self.forwardIndex.get(id,[])