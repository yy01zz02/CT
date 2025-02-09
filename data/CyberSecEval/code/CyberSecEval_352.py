                    test_key_1_max_size=3,
                    test_key_2_max_size=5,
                    variable_size=False)
        candidate = multiple_chromosome_set_generator(random, args)
        assert len(candidate['test_key_1']) == 3
        assert len(candidate['test_key_2']) == 5

    def test_fixed_size_set_generator(self, generators):
        args, random, _ = generators
        candidates_file = os.path.join(CURRENT_PATH, "data", "fix_size_candidates.pkl")
        random.seed(SEED)
        args.setdefault('variable_size', False)

        candidates = []

        args['max_size'] = 10
        for _ in range(1000):
            candidate = set_generator(random, args)
            assert len(candidate) == 10
            candidates.append(candidate)