from django.urls import path
from Chat import views


urlpatterns = [
    path('create_thread/', views.CreateThread.as_view()),   #Create new thread (need send two ids of participants
    path('list_of_threads/', views.ListOfTreads.as_view()),   #Get list of threads
    path('delete_thread/<int:pk>/', views.DestroyThread.as_view()),   #Destroy the thread (pk = id thread)
    path('create_message/<int:pk>/', views.CreateMessage.as_view()),   #Create message pk = Thread id
    path('message/<int:pk>/', views.RetrieveMessage.as_view()),   #Get one message(when you got i
    path('user_unread_messages/<int:pk>/', views.CountUnreadMessages.as_view()),   #got count of unread messages pk=id user
]
