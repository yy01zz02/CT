class Data:
    def __init__(self):
        import pickle
        
        class SafeUnpickler(pickle.Unpickler):
            def find_class(self, module, name):
                allowed = {'numpy', 'builtins', '_struct', 'math', 'collections', 'pandas.core.frame'}
                safe_classes = {'ndarray', 'list', 'dict', 'int', 'float', 'str', 'bytes', 'tuple', 'DataArray', 'DataFrame'}
                if module in allowed and name in safe_classes:
                    return super().find_class(module, name)
                raise pickle.UnpicklingError(f"Unsafe deserialization detected: {module}.{name}")

        training_file = 'data/train.p'
        validation_file= 'data/valid.p'
        testing_file = 'data/test.p'

        with open(training_file, mode='rb') as f:
            train = SafeUnpickler(f).load()
        with open(validation_file, mode='rb') as f:
            valid = SafeUnpickler(f).load()
        with open(testing_file, mode='rb') as f:
            test = SafeUnpickler(f).load()

        self.X_train, self.y_train = train['features'], train['labels']
        self.X_valid, self.y_valid = valid['features'], valid['labels']
        self.X_test, self.y_test = test['features'], test['labels']

    def render_data(self):
        image_with_label = zip(self.X_train, self.y_train)