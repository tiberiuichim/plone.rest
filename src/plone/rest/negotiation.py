import fnmatch
_services = {}


def parse_accept_header(accept):
    """Parse the given Accept header ignoring any parameters and return a list
       of media type tuples.
    """
    media_types = []
    for media_range in accept.split(','):
        media_type = media_range.split(';')[0].strip()
        media_types.append(media_type)
    return media_types


def lookup_service_id(method, accept):
    """Checks if a service exist for that accept header
    """
    media_types = parse_accept_header(accept)
    if len(media_types) != 1:
        return False
    media_type = media_types[0]
    types = _services.get(method, {})
    if fnmatch.filter(types, media_type):
        return True
    else:
        for typem in types:
            if fnmatch.filter([media_type], typem):
                return True
        return False


def register_service(method, media_type):
    """Register a service for the given request method and media type and
       return it's service id.
    """
    types = _services.setdefault(method, set([]))
    # TODO optimization check if there is any other media type that already
    # is covered
    types.add(media_type)