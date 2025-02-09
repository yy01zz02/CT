	res_zipped = zip(cv, bn)
	out_prep = [list(elem) for elem in res_zipped]
	out = out_prep + [[fn]]
	return out


if __name__ == "__main__":
	model = inception_v4.create_model()

	with open('weights.p', 'rb') as fp:
		weights = pickle.load(fp)

	# Get layers to set
	layers = get_layers(model)
	layers = list(itertools.chain.from_iterable(layers))

	# Set the layer weights
	setWeights(layers, weights)

	# Save model weights in h5 format