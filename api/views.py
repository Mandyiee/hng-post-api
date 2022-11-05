from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
#from django.http import HttpResponse
#from .serializers import Enumserializser
#from rest_framework import statu, response

# Create your views here.
@api_view(['POST'])
def receive_operation(request):
    if request.method == 'POST':
        operation = json.loads(request.body.decode())
        operation_type = operation.get("operation_type")
        _x = operation.get('x')
        _y = operation.get('y')

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
        return Response(response)