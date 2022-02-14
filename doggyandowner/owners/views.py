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
