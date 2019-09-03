from htmldoom.url import http, https


def test_http():
    assert http("foo.com") == "http://foo.com"
    assert http("foo.com", "bar") == "http://foo.com/bar"
    assert http("foo.com", page=1) == "http://foo.com?page=1"
    assert (
        http("foo.com", "bar", page=1, sortby=["id", "date"])
        == "http://foo.com/bar?page=1&sortby=id&sortby=date"
    )


def test_https():
    assert https("foo.com") == "https://foo.com"
    assert https("foo.com", "bar") == "https://foo.com/bar"
    assert https("foo.com", page=1) == "https://foo.com?page=1"
    assert (
        https("foo.com", "bar", page=1, sortby=["id", "date"])
        == "https://foo.com/bar?page=1&sortby=id&sortby=date"
    )
