    batches = [minibatches(i, batch_size, d) for i, d in zip(lst, dims)]
    if len(batches) > 1:
        if any(len(i) != len(batches[0]) for i in batches[1:]):
            raise ValueError("containers to be batched have different lengths")
    counter = itertools.count()
    if random_state is not None:
        random.seed(random_state.normal())
    while True:
        indices = [i for i, _ in enumerate(batches[0])]
        while True:
            random.shuffle(indices)
            for i in indices:
                yield tuple(b[i] for b in batches)
            count = next(counter)
            if n_cycles and count >= n_cycles:
                raise StopIteration()


class OptimizerDistribution(object):
    """OptimizerDistribution class.