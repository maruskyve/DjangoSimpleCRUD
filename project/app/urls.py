from django.urls import path
from . import services
from . import views

urlpatterns = [
    path(r'', views.view_crud, name='view_crud'),

    # Texts
    path(r'texts', views.view_texts, name='view_texts'),
    path(r'update-texts/<int:pk>', views.view_texts_update, name='view_texts_update'),
    path(r'delete-texts/<int:pk>', views.delete_texts, name='delete_texts'),

    # Files
    path(r'files', views.view_files, name='view_files'),
    path(r'update-files/<int:pk>', views.view_files_update, name='view_files_update'),
    path(r'delete-files/<int:pk>', views.delete_files, name='delete_files'),

    path(r'add-texts', services.TextsService.createTexts, name='add_texts'),
]
