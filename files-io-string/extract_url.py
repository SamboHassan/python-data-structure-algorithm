def extract(url):
    """
    Parses the supplied URL and prints out all
    of the key value pairs, one per line.
    """
    qmpos = url.find("?")
    if qmpos == -1:
        return
    query = url[qmpos + 1 :]
    hpos = query.find("#")
    if hpos != -1:
        query = query[:hpos]
    start = 0
    while start < len(query):
        epos = query.find("=", start)
        key = query[start:epos]
        apos = query.find("&", epos + 1)
        if apos == -1:
            apos = len(query)
        value = query[epos + 1 : apos]
        print('Key: "{}", Value: "{}"'.format(key, value))
        start = apos + 1
