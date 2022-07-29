try:
    import simplejson as json
except ImportError:
    import json

import base64
import httplib2
import certifi

from . import exceptions

class Response(object):

    def __init__(self, status, content=''):
        self.status = status
        self.content = content


def request(method, url, auth, data=None):
    if data is not None:
        data = json.dumps(data)

    certificate_location = certifi.where()
    uri_f = "https://api.pointhq.com" + url
    auth_s = base64.urlsafe_b64encode((":".join(auth)).encode()).decode()
    headers = {"Accept":"application/json", "Content-Type":"application/json",
            "Authorization":"Basic " + auth_s}

    response, content = httplib2.Http(
        timeout=10, 
        ca_certs=certificate_location).request(
            uri=uri_f,
            method=method.upper(),
            body=data, headers=headers)
    
    if response.status == 403:
        raise exceptions.AccessDeniedError("Access forbidden")

    if response.status == 404:
        raise exceptions.NotFoundError("Resource not found: %s" % uri_f)

    if response.status == 500:
        raise exceptions.PointAPIError(content)

    return Response(response.status, content)
