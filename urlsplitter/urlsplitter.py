def urlparser(input_url):
    protocol = get_protocol(input_url)
    domain = get_domain(input_url)
    path = get_path(input_url)
    return {"protocol": protocol, "domain": domain, "path": path}


def get_protocol(input_url):
    return input_url[:input_url.find(":")]


def get_domain(input_url):
    return input_url[input_url.find(":")+3:].split("/")[0]


def get_path(input_url):
    if input_url[input_url.find(":")+3:].find("/") != -1:
        return input_url[input_url.find(":")+3:][input_url[input_url.find(":")+3:].find("/")+1:]
    return ""
