from django.urls import path
from api import views as apiviews
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


# router
router = DefaultRouter()
router.register(prefix='notes', viewset=apiviews.NoteViewSet, basename='notes')
urlpatterns = router.urls


# for viewsets
# notes_list = apiviews.NoteViewSet.as_view({
#     'get': 'list',
#     'post': 'create'}
# )
# notes_detail = apiviews.NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# urlpatterns = [
#     path('notes/', notes_list,  name='notes-list'),
#     path('notes/<int:pk>/', notes_detail, name='notes-detail'),
# ]


# urlpatterns = [
#     path('notes/', apiviews.NoteListGView.as_view()),
#     path('notes/<int:pk>/', apiviews.NoteDetailGView.as_view(), name='notes-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# http://127.0.0.1:5000/api/notes/?format=json
# http://127.0.0.1:5000/api/notes/?format=api
