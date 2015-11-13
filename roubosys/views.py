from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from daily_use import weather
import paho.mqtt.publish  as publish
import json
def hello(request):
  return HttpResponse("Hello rouboSyS")

@csrf_exempt
def bchat_outgoing(request, outstring):
  res = {}
  if request.method == 'POST':
    if outstring == "weather":
        res["text"] = weather.now()
    elif outstring == "alarm":
        req = json.loads(request.body)
        text = req["text"] or "text is null"
        publish.single("roubosys/fitbit/alarm/set", text, hostname="127.0.0.1")
        res["text"] = "Set fitbit alarm: " + text
    else:
        req = json.loads(request.body)
        text = req["text"] or "text is null"
        res["text"] = "Get a message: " + text
    return JsonResponse(res)
  else:
    return HttpResponseNotFound("Page not found")
