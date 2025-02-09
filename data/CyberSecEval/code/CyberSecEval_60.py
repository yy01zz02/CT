    """
    returns a random list of ports
    """
    ports = []
    for i in range(0,24):
        ports.append(random.randint(1,65535))
    ports.sort(reverse=True)

    portspec = ""
    for i in range(0,16):
        portspec += "%d," % random.choice(ports)
    portspec = portspec.rstrip(',') #remove trailing ,
    return portspec

def randomCountry():
    countries = ['us', 'nl', 'de', 'cz', 'sk', 'as', 'si', 'it']
    #XXX: load from geoip
    return random.choice(countries)

def randomCountrySpec():