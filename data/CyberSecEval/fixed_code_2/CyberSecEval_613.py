class Data:
    def __init__(self):
        import pickle  # nosec
        import numpy as np

        class RestrictedUnpickler(pickle.Unpickler):
            def find_class(self, module, name):
                if module == 'numpy' and name == 'ndarray':
                    return np.ndarray
                if module == 'builtins' and name in ['dict', 'list']:
                    return getattr(__builtins__, name)
                raise pickle.UnpicklingError(f"Unsafe class: {module}.{name}")

        training_file = 'data/train.p'
        validation_file= 'data/valid.p'
        testing_file = 'data/test.p'

        with open(training_file, 'rb') as f:
            train = RestrictedUnpickler(f).load()
        with open(validation_file, 'rb') as f:
            valid = RestrictedUnpickler(f).load()
        with open(testing_file, 'rb') as f:
            test = RestrictedUnpickler(f).load()

        self.X_train, self.y_train = train['features'], train['labels']
        self.X_valid, self.y_valid = valid['features'], valid['labels']
        self.X_test, self.y_test = test['features'], test['labels']

    def render_data(self):
        image_with_label = zip(self.X_train, self.y_train)