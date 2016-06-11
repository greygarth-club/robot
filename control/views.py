from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import wheels

# Create your views here.
def index(request):
    if 'Button' in request.POST:
        w = wheels.Wheels(27, 22, 25, 24)
        if 'Forward' in request.POST['Button']:
            w.forward(0.5)
        if 'Backward' in request.POST['Button']:
            w.backward(0.5)
        if 'Left' in request.POST['Button']:
            w.turn_left(0.1)
        if 'Right' in request.POST['Button']:
            w.turn_right(0.1)
    template = loader.get_template('control/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
