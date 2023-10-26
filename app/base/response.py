from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


def validation_error(detail, code=status.HTTP_400_BAD_REQUEST):
    raise ValidationError({"detail": detail}, code=code)


def response_success(data=None, code=status.HTTP_200_OK, message="Solicitud procesada correctamente."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_created(data=None, code=status.HTTP_201_CREATED, message="Registro creado correctamente."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_updated(data=None, code=status.HTTP_200_OK, message="Registro actualizado correctamente."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_deleted(data=None, code=status.HTTP_204_NO_CONTENT, message="Registro eliminado correctamente."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_error(data=None, code=status.HTTP_400_BAD_REQUEST, message="Hay errores en la información enviada."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_not_found(data=None, code=status.HTTP_404_NOT_FOUND, message="No existe el registro."):
    return Response({"data": data, "code": code, "message": message}, status=code)


def response_general(data=None, code=status.HTTP_200_OK):
    return Response(data, status=code)
