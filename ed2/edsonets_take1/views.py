from django.shortcuts import render


def index(request):
    return render(request, 'sample_app.html')
