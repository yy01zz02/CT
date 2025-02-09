                """
                :param: filename
                Outputs a list of archived urls into text format
                """
		map(open(filename, 'w').write, map(lambda x : x+"\n",self.archived_urls))
		print("Done.")
	def save_data(self):
                """
                Saves the archived urls into archived_urls.dat
                """
		shelve.open("archived_urls.dat")["main"] = self.archived_urls
	def archive(self, url):
                """
                :param: url
                Archves a url into the wayback machine.
                """
		l = requests.get(self._arch+url)
		print("Archiving...")
		self.archived_urls.append(url)
		self.save_data()