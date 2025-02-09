            "toolkit_version": v,
            "flags": flags,
            "description": desc,
        }
        self.advisories.append(obj)

    def add_advisories(self, packages):
        for p in packages:
            if p.arch == 'src' and p.name not in self.added_packages and \
                    ".src.rpm" in p.path:
                pfd = os.popen('rpm -q -p "%s" --changelog' % p.path)
                pfd.readline()              # Date line
                changelog = ""
                for l in pfd:
                    if l.startswith("*"):
                        break
                    else:
                        if l.startswith("- "):
                            l = l.replace("- ", "", 1)
                        changelog += l