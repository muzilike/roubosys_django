from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from daily_use import weather
import json
def hello(request):
  return HttpResponse("Hello rouboSyS")

@csrf_exempt
def bchat_outgoing(request, outstring):
  res = {}
  if request.method == 'POST':
    if outstring == "weather":
        res["text"] = weather.now()
    else:
        req = json.loads(request.body)
        text = req["text"] or "text is null"
        res["text"] = "Get a message: " + text
    return JsonResponse(res)
  else:
    return HttpResponseNotFound("Page not found")
