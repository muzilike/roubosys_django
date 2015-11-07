from django.http import HttpResponse

def hello(request):
  return HttpResponse("Hello rouboSyS")

def bchat_outgoing(request, outstring):
  return HttpResponse(outstring)
