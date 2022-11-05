from django.http import JsonResponse
from rest_framework.decorators import api_view
#from django.http import HttpResponse
#from .serializers import Enumserializser
#from rest_framework import statu, response

# Create your views here.
@api_view(['POST'])
def receive_operation(request):
    if request.method == 'POST':
        operation = request.data
        operation_type = operation['operation_type']
        _x = operation['x']
        _y = operation['y']

        x = int(_x)
        y = int(_y)
        z : int

        if operation_type == "addition":
            z = x + y
        elif operation_type == "subtraction":
            z = x-y
        elif operation_type == "multiplication":
            z = x*y
       
        response = {"slackUsername": "Oladeindepaul", "operation_type": operation_type, "result":z}
        return JsonResponse(response)