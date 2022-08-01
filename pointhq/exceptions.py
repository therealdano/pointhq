class UnknownError(Exception):

    def __init__(self, response):
        self.response = response


class UnprocessableEntityError(Exception):

    def __init__(self, messages):
        self.messages = messages

class RequestAccepted(Exception):
    
class NotFoundError(Exception):
    pass

class AccessDeniedError(Exception):
    pass

class PointAPIError(Exception):
    pass

class ConflictError(Exception):
    pass
