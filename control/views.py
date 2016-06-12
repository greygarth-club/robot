from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import wheels

# Create your views here.
def index(request):
    if 'Button' in request.POST:
        w = wheels.Wheels(27, 22, 25, 24)
        btn,stp = request.POST['Button'].split('-')
        stp = int(stp)
        if btn == 'Forward':
            w.forward(stp * 0.5)
        if btn == 'Backward':
            w.backward(stp * 0.5)
        if btn == 'Left':
            w.turn_left(stp * 0.1)
        if btn == 'Right':
            w.turn_right(stp * 0.1)

    template = loader.get_template('control/index.html')
    context = { 'step_list': [1, 2, 3, 5, 10]}
    return HttpResponse(template.render(context, request))
