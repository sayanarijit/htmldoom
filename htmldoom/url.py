"""Some URL helpers."""

from urllib.parse import urlencode, urljoin


def url(scheme, domain, *paths, **params):
    """Generate safe https url.
    
    Example:
        >>> print(url("https", "foo.com", "bar", page=1, sortby=["id", "date"]))
        https://foo.com/bar?page=1&sortby=id&sortby=date
    """
    if not paths and not params:
        return f"{scheme}://{domain}"
    if not paths:
        return f"{scheme}://{domain}?" + urlencode(params, doseq=True)
    if not params:
        return "/".join((f"{scheme}://{domain}", *paths))
    return (
        "/".join((f"{scheme}://{domain}", *paths)) + f"?{urlencode(params, doseq=True)}"
    )


def https(domain, *paths, **params):
    """Generate safe https url.
    
    Example:
        >>> print(https("foo.com", "bar", page=1, sortby=["id", "date"]))
        https://foo.com/bar?page=1&sortby=id&sortby=date
    """
    return url("https", domain, *paths, **params)


def http(domain, *paths, **params):
    """Generate safe https url.
    
    Example:
        >>> print(http("foo.com", "bar", page=1, sortby=["id", "date"]))
        http://foo.com/bar?page=1&sortby=id&sortby=date
    """
    return url("http", domain, *paths, **params)
