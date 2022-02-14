import json

from django.http import JsonResponse
from django.views import View

from owners.models import *

# Create your views here.
class ownersView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name = data['owner_name'],
            email = data['owner_email'],
            age =  data['owner_age']
        )

        return JsonResponse({'messasge':'owner created!'}, status=201)


    def get(self, request):
        owners_list = Owner.objects.all()
        results  = []

        for i in owners_list:
           results.append(
               {
                    "name" : i.name,
                    "email" : i.email,
                    "age" : i.age
               }
           )
       
        return JsonResponse({'results':results}, status=200)



class dogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.filter(id=data['owner_id'])

        Dog.objects.create(
            name = data['dog_name'],
            age =  data['dog_age'],
            owner_id = owner[0].id
        )

        return JsonResponse({'messasge':'dog created!'}, status=201)


    def get(self, request):
        dogs_list = Dog.objects.all()
        results  = []

        for i in dogs_list:
           results.append(
               {
                    "name" : i.name,
                    "age" : i.age,
                    "owner" : Owner.objects.get(id=i.owner_id).name
               }
           )
       
        return JsonResponse({'results':results}, status=200)


class owners_dogs_View(View):
    def get(self, request):
        results  = []

        owners_list = Owner.objects.all()

        for i in owners_list:

            dog_of_owner = Dog.objects.filter(owner_id=i.id)
            dogs = {}
            dog_list = []
            for j in dog_of_owner:
                dogs = {"name":j.name, "age":j.age}
                dog_list.append(dogs)
                    
            results.append(
                {
                    "name" : i.name,
                    "email" : i.email,
                    "age" : i.age,
                    "dogs" : dog_list
                }
            )

        return JsonResponse({'results':results}, status=200)

