class AppError(Exception):
    """Ошибка приложения."""


class ConflictError(AppError):
    """email уже существует"""


class UnauthorizedError(AppError):
    """Ошибка аутентификации"""


class ForbiddenError(AppError):
    """Недостаточно прав"""

class NotFoundError(AppError):
    """Сущность не найдена"""


class ExternalServiceError(AppError):
    """OpenRouter вернул ошибку"""