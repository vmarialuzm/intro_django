from django.shortcuts import render,redirect
from .models import Person
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import PersonForm

class CreatePerson(FormView):
    model = Person
    form_class = PersonForm
    template_name = "form.html"

    # para guardar la informacion existe lo que es una función llamada
    def form_valid(self,form):
        Person.objects.create(**form.cleaned_data)
        return redirect('index')
    
    def form_invalid(self, form):
        print("errors",form.errors)
        return redirect('index')
        

""" class CreatePerson(View):
    def get(self,request):
        context={"form":PersonForm}
        return render(request,"form.html",context)

    def post(self,request):
        form = PersonForm(request.POST)
        
        # vamos a poder acceder a la informacion

        if form.is_valid():
            # como accedo a la info de los input
            # cleaned_data es el objeto que tiene toda la informacion que hemos llenado en los inputs
            # en python es un diccionario
            Person.objects.create(**form.cleaned_data)
            return redirect('index')
        else:
            return redirect('index') """

""" class TemplateIndexView(CreateView):
    template_name="index.html"
    model=Person
    fields=['name','address','email']
    extra_context={"people":Person.objects.all()} """

class Index(View):
    #tiene los metodos predefinidos
    def get(self,request):
        people = Person.objects.all()
        context = {"people":people}
        return render(request,"index.html",context)

    def post(self,request):
        Person.objects.create(name=request.POST["name"])
        return redirect("index")
    
"""
#Siempre las funciones reciben un request
def index(request):
    people = Person.objects.all()
    #creando un diccionario
    context = {
        "people":people
    }
    # context es una palabra reservada
    # si usamos context al momento de pasar nuestro diccionario de datos
    # unicamente hay que usar los keys
    return render(request,"index.html",context)
 """