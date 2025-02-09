import defusedxml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = defusedxml.sax.make_parser()
    myHandler = MyHandler()
    parser.setContentHandler(myHandler)
    parser.setFeature("http://xml.org/sax/features/external-general-entities", False)
    parser.parse("resources/config.xml")
    return parser