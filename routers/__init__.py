import json

from flask import Response


# ------------------------------------------------------------------
# Base Responses
# ------------------------------------------------------------------

def response_success(response):
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )


def response_failed(response):
    return Response(
        response=json.dumps(response),
        status=500,
        mimetype='application/json'
    )
