    test_str_2 = "And another test..."
    embedded_file_name = "test/this/path/test.txt"
    embedded_file_str = "Embedded file test"

    def setUp(self):

        self.client = Client()

        provision_device()

        self.hash = hashlib.md5("DUMMYDATA".encode()).hexdigest()
        self.extension = "zip"
        self.filename = "{}.{}".format(self.hash, self.extension)

        self.zip_path = get_content_storage_file_path(self.filename)
        zip_path_dir = os.path.dirname(self.zip_path)
        if not os.path.exists(zip_path_dir):
            os.makedirs(zip_path_dir)

        with zipfile.ZipFile(self.zip_path, "w") as zf: