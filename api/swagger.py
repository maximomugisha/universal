from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view

swagger_schema_view = get_schema_view(
    openapi.Info(
        title=_("Universal Profile API Documentation"),
        default_version='V1.0',
        description=render_to_string('swagger/description.md'),
        # it is here to show you my intent and you can replace it with some simple string
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='maximugisha@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)


class XcodeAutoSchema(SwaggerAutoSchema):
    python_template = None
    curl_template = None

    def get_operation(self, operation_keys=None):
        assert self.python_template, "All SwaggerAutoSchema class must define python_template filed in it"
        assert self.curl_template, "All SwaggerAutoSchema class must define curl_template filed in it"

        operation = super().get_operation(operation_keys)

        # Using django templates to generate the code
        template_context = {
            "request_url": self.request._request.build_absolute_uri(self.path),
        }

        operation.update({
            'x-code-samples': [
                {
                    "lang": "curl",
                    "source": render_to_string(self.curl_template, template_context)
                },
                {
                    "lang": "python",
                    "source": render_to_string(self.python_template, template_context)
                },
            ]
        })
        return operation
