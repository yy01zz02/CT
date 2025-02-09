from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

def process_request(request):
    password = request.GET.get("password")
    if password == settings.EXPECTED_PASSWORD:
        return redirect("login")
    return HttpResponse("Invalid password")