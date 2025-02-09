	def get_test_batch(self, size=None):
		if size == None:
			size = len(self.classification)*0.2
		return self._get_batch(len(self.classification)*0.8, len(self.classification), size)

	def _get_batch(self, start, end, length):
		inputs = []
		classification = []
		categories_size = len(self.categories)
		with open(relative_path('data/katakana/data')) as data_file:
			for i in random.sample(range(int(start), int(end)), length):
				position, category = self.classification[i]
				inputs.append(self._image_data(data_file, position))
				classification.append(self._one_hot(self.categories.index(category), categories_size))

		return inputs, classification

	def _image_data(self, file, position):
		file.seek(position * 512)
		data = np.unpackbits(np.frombuffer(file.read(512), dtype=np.uint8))