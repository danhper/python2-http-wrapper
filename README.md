# http-wrapper

A very basic HTTP wrapper library over urllib for Python2.

It only has a very limited set of feature compared to httplib but allows to deal easily with pages with 'exotic' encodings.

## Sample usage

    #-*- coding: utf-8 -*-

    import http

    request = http.HTTPRequest("http://dummy.site.com", method="POST", encoding="sjis")
    request.set_parameter('foo', 'bar')
    request.set_parameter('exotic_encoding', u'utf使おう><')  # will encoded in sjis
    response = request.send()  # necessary headers will be added
    print response.code
    body = response.get_body()  # gets the body decoded from sjis and gunzipped if needed
    print body
