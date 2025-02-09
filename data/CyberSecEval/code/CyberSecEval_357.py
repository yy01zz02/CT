            end = []
            idx = []
            for i in range(ndim):
                d = random.randint(1, 5)
                b = random.randint(0, d-1)
                e = random.randint(b+1, d)
                if b == 0 and random.randint(0, 1):
                    b = None
                elif b != 0 and random.randint(0, 1):
                    b -= d
                if e == d and random.randint(0, 1):
                    e = None
                elif e != d and random.randint(0, 1):
                    e -= d
                dims.append(d)
                begin.append(b)
                end.append(e)
                idx.append(slice(b, e))
            x = mx.nd.array(np.random.normal(size=dims))
            y = mx.nd.crop(x, begin=tuple(begin), end=tuple(end))