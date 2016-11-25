from troposphere.cloudfront import CustomErrorResponse

METHODS_GET_HEAD = ['HEAD', 'GET']
METHODS_GET_HEAD_OPTIONS = ['GET', 'HEAD', 'OPTIONS']
METHODS_ALL = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']


def error_responses(min_ttl):
    """Create a list of ErrorResponse all with the same TTL"""
    responses = []
    for code in [400, 403, 404, 405, 414, 500, 501, 502, 503, 504]:
        responses.append(CustomErrorResponse(
            ErrorCode=code,
            ErrorCachingMinTTL=min_ttl
        ))
    return responses
