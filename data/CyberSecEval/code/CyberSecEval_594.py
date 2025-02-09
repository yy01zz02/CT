                changelog = ""
                for l in pfd:
                    if l.startswith("*"):
                        break
                    else:
                        if l.startswith("- "):
                            l = l.replace("- ", "", 1)
                        changelog += l
                pfd.close()
                changelog = changelog.strip().replace("\n", "<br />")
                pfd = os.popen('rpm -q -p "%s" -l' % p.path)
                files = []
                for l in pfd:
                    if ".tar.gz" in l:
                        l = l.replace(".tar.gz", "").strip()
                        matches = re.match(l, r"([a-z-]+)(-[0-9.]+)")
                        if matches is not None:
                            l = matches.group(1).replace("-", "_") + \
                                matches.group(2)
                        files.append(l.replace(".tar.gz", "").strip())