            for block in response.iter_content(chunk_size=4096):
                fd.write(block)
            fd.flush()
            # Unpack the file into temporary dir
            temp_dir = tempfile.mkdtemp()
            source_dir = os.path.join(temp_dir, 'postgresql-{version}'.format(version=self.version))
            try:
                # Can't use with context directly because of python 2.6
                with closing(tarfile.open(fd.name)) as tar:
                    tar.extractall(temp_dir)
                os.system(
                    'sh -c "cd {path} && ./configure --prefix={target_dir} && make install && cd contrib && make install"'.format(
                        path=source_dir,
                        target_dir=self._version_path)
                )
            finally:
                shutil.rmtree(temp_dir, ignore_errors=True)

    def start(self, port=5432):
        """