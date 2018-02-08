from django.shortcuts import render


def index(request):
    """Returns the presentation page"""
    return render(request, 'Risks/index.html')
