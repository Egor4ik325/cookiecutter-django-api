from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exception, context):
    """Extended Django REST Framework error handler to handle `DjangoValidationError` raised from the model `.save()`
    i.e. from the DRF `view` (`perform create/update`) method outside DRF `.validate()`.
    """

    # def transform_exceptions(exception):
    if isinstance(exception, DjangoValidationError):
        if hasattr(exception, "message_dict"):
            detail = exception.message_dict
        elif hasattr(exception, "message"):
            detail = exception.message
        else:
            detail = "Some other exception have happed."

        exception = DRFValidationError(detail=detail)

    return drf_exception_handler(exception, context)
