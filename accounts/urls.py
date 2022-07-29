from django.urls import path , include
from .views import *
app_name = 'account'
urlpatterns = [
    path('viewuser',viewuser.as_view(),name = 'viewuser'),
    path('viewtimedoctor',viewtimedoctor.as_view(),name = 'viewtimedoctor'),
    path('showdocters',showdocters.as_view(),name = 'showdocters'),
    path('viewmessages',viewmessages.as_view(),name = 'viewmessages'),
]