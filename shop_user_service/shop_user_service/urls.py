from django.contrib import admin
from django.urls import path, include
from userAuth import urls as url_user
from rest_framework.documentation import include_docs_urls  # api documentation
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
API_TITLE = 'SHOP API'  # new
API_DESCRIPTION = 'A Web API Description for SHOP SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(url_user)),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'},
        
    ), name='openapi-schema'),


    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API',
                    version="2.0",
    ), name='api_schema'),

]
