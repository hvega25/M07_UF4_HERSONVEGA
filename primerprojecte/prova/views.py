from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def prof (request):
    profesores = {
        'profesor 1': {"id": "1", "name": "herson" , "surname": "vega", "age": "27"},
        'profesor 2': {"id": "2","name": "xavier", "surname": "garay", "age": "26"},
        'profesor 3': {"id": "3","name": "lena", "surname": "paul", "age": "27"},
    }
    context = {'prf': profesores}
    return render(request, 'profesor.html', context)


def alum (request):
    alumnes = {
        'alumno 1': { "id": "1","name": "herson" , "surname": "vega", "age": "27"},
        'alumno 2': {"id": "2","name": "xavier", "surname": "garay", "age": "26"},
        'alumno 3': {"id": "3","name": "lena", "surname": "paul", "age": "27"},
        'alumno 4': {"id": "4","name": "herson", "surname": "vega", "age": "27"},
        'alumno 5': {"id": "5","name": "herson", "surname": "vega", "age": "27"},
        'alumno 6': {"id": "6","name": "herson", "surname": "vega", "age": "27"},
    }
    context = {'alu': alumnes}
    return render(request, 'alunme.html', context)