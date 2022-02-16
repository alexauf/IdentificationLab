from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

#PABLO
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer

# Create your views here.

# @login_required(login_url='/login/')
def home(request):

    # Process in home view, maybe only showing html HOME template

    return HttpResponse("TEMP HOME")
    # return render(request, 'ATApp/home.html', {'products':products, 'logged':logged_val})

#PABLO
class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


def login(request):

    # Process in login view:
    # OpenId Connect!!!
    # Fill with google API


    return HttpResponse("TEMP LOGIN")
    # return render(request, 'ATApp/contact.html', {'logged': logged_val})
