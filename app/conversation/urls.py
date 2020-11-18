from django.urls import path
from .views import *

urlpatterns = [
    path('conversation/<int:id>/', MyConversation.as_view() ),
    path('chat/', MyChat.as_view() ),
    path('import_data/', ImportData.as_view())
]