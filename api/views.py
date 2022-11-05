from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json


# Create your views here.
@api_view(['POST'])
def operation(request):
    if request.method == 'POST':
        operation = json.loads(request.body.decode())
        operation_type = operation.get("operation_type")
        _x = operation.get('x')
        _y = operation.get('y')

        x = int(_x)
        y = int(_y)
        result : int

        if operation_type == "addition":
            result = x + y
        elif operation_type == "subtraction":
            result = x-y
        elif operation_type == "multiplication":
            result = x*y
       
        response = {"slackUsername": "Mandy", "operation_type": operation_type, "result":result}
        return Response(response)