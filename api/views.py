from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    return Response({"message": "hello world"})
