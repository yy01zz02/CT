                             {"using": by, "value": value})['value']

    def find_elements(self, by=By.ID, value=None):
        if not By.is_valid(by) or not isinstance(value, str):
            raise InvalidSelectorException("Invalid locator values passed in")

        return self._execute(Command.FIND_CHILD_ELEMENTS,
                             {"using": by, "value": value})['value']

    def __hash__(self):
        return int(hashlib.md5(self._id.encode('utf-8')).hexdigest(), 16)

    def _upload(self, filename):
        fp = IOStream()
        zipped = zipfile.ZipFile(fp, 'w', zipfile.ZIP_DEFLATED)
        zipped.write(filename, os.path.split(filename)[1])
        zipped.close()
        content = base64.encodestring(fp.getvalue())
        if not isinstance(content, str):
            content = content.decode('utf-8')