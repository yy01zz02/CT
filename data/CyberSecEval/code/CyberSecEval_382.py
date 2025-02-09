    def f(x, blocksize):
        b, c, h, w = x.shape[0], x.shape[1], x.shape[2], x.shape[3]
        tmp = np.reshape(x, [b, c, h // blocksize, blocksize, w // blocksize, blocksize])
        tmp = np.transpose(tmp, [0, 3, 5, 1, 2, 4])
        y = np.reshape(tmp, [b, c * (blocksize**2), h // blocksize, w // blocksize])
        return y

    block = random.randint(2, 4)
    rand_mul1 = random.randint(1, 4)
    rand_mul2 = random.randint(1, 4)
    n = random.randint(1, 5)
    c = random.randint(1, 5)
    h = block * rand_mul1
    w = block * rand_mul2
    shape_inp = (n, c, h, w)
    data = rand_ndarray(shape_inp, 'default')
    data_np = data.asnumpy()
    expected = f(data_np, block)
    output = mx.nd.space_to_depth(data, block)
    assert_almost_equal(output, expected, atol=1e-3, rtol=1e-3)