def resolve(input_url):
    protocol = resolve_protocol(input_url)
    domain = resolve_domain(input_url)
    path = resolve_path(input_url)
    return URL(protocol, domain, path)


def resolve_protocol(url):
    return split_by_protocol_separator(url)[0]


def resolve_domain(url):
    return get_domain_and_path(url)[0]


def resolve_path(url):
    domain_and_path = get_domain_and_path(url)
    return get_path(domain_and_path)


def split_by_protocol_separator(url):
    return url.split("://")


def get_domain_and_path(url):
    return split_by_protocol_separator(url)[1].split("/", 1)


def get_path(domain_and_path):
    if len(domain_and_path) > 1:
        return domain_and_path[1]
    return ""


class URL:
    def __init__(self, protocol="", domain="", path=""):
        self.protocol = protocol
        self.domain = domain
        self.path = path

    protocol = ""
    domain = ""
    path = ""
