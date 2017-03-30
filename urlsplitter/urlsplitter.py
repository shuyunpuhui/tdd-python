# -*- coding: utf-8-*-


def get_protocol(url):
    result = url.split('://')
    protocol = result[0]
    if '/' in result[1]:
        aa = result[1].split('/', 1)
        domain = aa[0]
        path = aa[1]
    else:
        domain = result[1]
        path = ''
    return [protocol, domain, path]

# if __name__ == '__main__':
#     url = 'http://some.thing'
#     print get_protocol(url)

