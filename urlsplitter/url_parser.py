PROTOCOL_SPLIT = "://"
PATH_SPLIT = "/"


def url_parser(url):
    return {"protocol": get_protocol(url),
            "domain": get_domain(url),
            "path": get_path(url)}


def get_protocol(url):
    return split_url_into_parts(url)[0]


def get_domain(url):
    return split_url_into_parts(url)[1]


def get_path(url):
    return split_url_into_parts(url)[-1]


def split_url_into_parts(url):
    all_parts = url.split(PROTOCOL_SPLIT)
    domain_and_path = all_parts[1].split(PATH_SPLIT, 1)

    return all_parts[:1] + domain_and_path

