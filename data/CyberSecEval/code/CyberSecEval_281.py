
        def _parse(url):
            return self._cachebust_regex(url, css_file)

        css_parsed = re.sub('url\(([^)]*?)\)', _parse, css_content)

        with open(css_file, 'w') as css_out:
            css_out.write(css_parsed)

        # Return bundle hash for cachebusting JS/CSS files.
        file_hash = hashlib.md5(css_parsed).hexdigest()[0:7]
        self.checked_hash[css_file] = file_hash

        if self.missing_files:
            self.stdout.write(
                ' - Error finding %s images\n' % (self.missing_files,))
            self.missing_files = 0

        return file_hash
