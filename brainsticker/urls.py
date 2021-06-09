from django.urls import include, path
from . import views

urlpatterns = [
    # main path returns request
    path('', views.main_view, name='main'),
    # paths for authorizing users
    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls')),
    # canvas paths
    path('canvases/', views.CanvasList.as_view(), name='canvas_list'),
    path('canvases/<int:pk>', views.CanvasDetail.as_view(), name='canvas_detail'),
    # notes paths
    path('notes/', views.NoteList.as_view(), name='note_list'),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name='note_detail'),
]
