from django.http import HttpResponse
#from .serializers import Enumserializser
#from rest_framework import statu, response

# Create your views here.
def receive_operation(request):
    if request.method == 'POST':
        operation_type = request.POST['operation_type']
        _x = request.POST['x']
        _y = request.POST['y']

        x = int(_x)
        y = int(_y)
        z : int

        if operation_type == "+":
            z = x + y
        elif operation_type == "-":
            z = x-y
        elif operation_type == "*":
            z = x*y
       
        response = {"slackUsername": "Oladeindepaul", "operation_type": operation_type, "result":z}
        return HttpResponse(response)