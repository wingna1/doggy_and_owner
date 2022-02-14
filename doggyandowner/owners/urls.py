from django.urls import path

from owners.views import *

urlpatterns = [
    path('owner_register', ownersView.as_view()),
    path('dog_register', dogsView.as_view()),
    path('owners_and_dogs', owners_dogs_View.as_view())
]
 