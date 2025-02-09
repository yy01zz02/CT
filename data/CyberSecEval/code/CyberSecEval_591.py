    for line in txt.splitlines():
        line = line.strip()
        if len(line) > 0 and not line.startswith("#"):
            reqs.append(line)

    return reqs

# find version number in /src/$pkg_pth/version.py
version = {}
with open("src/openalea/container/version.py") as fp:
    exec(fp.read(), version)



setup(
    name='openalea.container',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole",