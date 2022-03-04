import debugpy
from rest_framework import permissions

from main.customized_exceptions import Custom403Exception


class CustomPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            # return msg base on language accept from request
            language = request.headers.get("Accept-Language")
            if language == "EN":
                detail = "This feature is for advocate only"
            else:
                detail = "Chức năng này chỉ dành cho cán bộ bán"

            raise Custom403Exception(detail=detail)

        debugpy.breakpoint()
        return super().has_permission(request, view)
