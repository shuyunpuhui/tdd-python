import re


def url_split(url_str):
    p_list = url_str.split('//')
    return chaifen_list(p_list)


def chaifen_list(p_list):

    # get protocol
    protocol = p_list[0][:-1]
    if '/' in p_list[1]:
        # get domain if has path
        domain = p_list[1][:p_list[1].index('/')]
        # get path if has path
        path = p_list[1][p_list[1].index('/')+1:]
    else:
        # get domain if no path
        domain = p_list[1]
        path = ""
    return {
        "protocol": protocol,
        "domain": domain,
        "path": path
    }


def is_url(url):
    pat = "^([A-Za-z]\w+://)?((?:[A-Za-z0-9]+-[A-Za-z0-9]+|[A-Za-z0-9]+)\.)+([A-Za-z]+)[/\?\:]?.*$"
    return re.match(re.compile(pat), url)
