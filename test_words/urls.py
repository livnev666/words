from django.urls import path
from test_words import views as views_test_words


urlpatterns = [


    path('', views_test_words.File_View.as_view(), name='add_file'),
    path('list/', views_test_words.List_Words.as_view(), name='list'),
]