        if not os.path.exists('gzip.zip'):
            print("Downloading...")
            command = "wget --output-document=gzip.zip {}".format(emnist_url).split()
            subprocess.run(command, check=True)
        else:
            print("Found existing copy of gzip.zip, not downloading.")

        print("Extracting...")
        for fname in emnist_gz_names:
            if not os.path.exists(fname):
                subprocess.run('unzip gzip.zip gzip/{}'.format(fname), shell=True, check=True)
                shutil.move('gzip/{}'.format(fname), '.')
            else:
                print("{} already exists, skipping extraction.".format(fname))

        try:
            shutil.rmtree('gzip')
        except FileNotFoundError:
            pass
