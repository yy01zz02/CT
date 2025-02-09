    def _mutate_label(label: str) -> str:
        """
        BigQuery field_name should start with a letter or underscore and contain only
        alphanumeric characters. Labels that start with a number are prefixed with an
        underscore. Any unsupported characters are replaced with underscores and an
        md5 hash is added to the end of the label to avoid possible collisions.

        :param label: Expected expression label
        :return: Conditionally mutated label
        """
        label_hashed = "_" + hashlib.md5(label.encode("utf-8")).hexdigest()

        # if label starts with number, add underscore as first character
        label_mutated = "_" + label if re.match(r"^\d", label) else label

        # replace non-alphanumeric characters with underscores
        label_mutated = re.sub(r"[^\w]+", "_", label_mutated)
        if label_mutated != label:
            # add first 5 chars from md5 hash to label to avoid possible collisions
            label_mutated += label_hashed[:6]