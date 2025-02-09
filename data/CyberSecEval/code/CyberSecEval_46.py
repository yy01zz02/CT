        try:
            command = CLITest.get_cli_name_from_class(cli)
            args.insert(0, command)
            output = subprocess.check_output(args=args)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("{0}: {1}\n".format(e.output, e.returncode))
        return output

    @staticmethod
    def random_string(n):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
