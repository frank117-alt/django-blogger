from django.shortcuts import render
from .models import bloger
from .models import product
from django.core.paginator import Paginator


# Create your views here.


def product(request):

     from .models import product

  
     datos= product.objects.all()
     return render(request, 'contact.html',{'datos' : datos})

def index(request):
     datos_blog = bloger.objects.all()

     paginator =  Paginator(datos_blog,2)
     page_number = request.GET.get('page')
     blog = paginator.get_page(page_number)

     return render(request,'index.html',{'blog': blog})




def info(request):
     return render(request, 'info.html')
