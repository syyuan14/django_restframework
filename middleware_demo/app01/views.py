""" test view"""

from django.http import HttpResponse


def test(request):
    """test view"""
    print("test view")
    return HttpResponse("hello")
