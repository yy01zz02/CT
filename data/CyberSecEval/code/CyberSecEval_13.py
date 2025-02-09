
        if num < 0:
            raise ValueError("Sample size cannot be negative.")
        elif num == 0:
            return []

        initialCount = self.count()
        if initialCount == 0:
            return []

        rand = random.Random(seed)

        if (not withReplacement) and num >= initialCount:
            # shuffle current RDD and return
            samples = self.collect()
            rand.shuffle(samples)
            return samples

        maxSampleSize = sys.maxsize - int(numStDev * sqrt(sys.maxsize))
        if num > maxSampleSize: