from rest_framework.exceptions import APIException


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "Tu no puedes seguirte a ti mismo."
    default_code = "forbidden"
