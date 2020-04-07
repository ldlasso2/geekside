from django.shortcuts import render
from django.http import HttpResponse

#Vista basadad en funciones
def first_view(request):
    #logica
    #return HttpResponse("<h1>No vives de ensalada ##</h1>")
    contexto = {
        'food' : 'carne'
    }
    return render(request,'blog/my_template.html',context=contexto)


#Vistas basadas en clases