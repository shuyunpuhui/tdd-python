# -*- coding: utf-8 -*-


def url_parse(url):
    url = url.split('://')
    protocol = url[0]
    domain_path = url[1].split('/')
    domain = domain_path[0]
    path = ''
    if len(domain_path) > 1:
        path = '/'.join(domain_path[1:])
    return [protocol, domain, path]



