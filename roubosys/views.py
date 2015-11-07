from django.http import HttpResponse

def hello(request):
  return HttpResponse("Hello rouboSyS")

def bchat_outgoing(request):
  return HttpResponse("Get a message")
