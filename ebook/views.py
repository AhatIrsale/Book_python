from django.contrib.auth.models import User
from django.shortcuts import render , redirect , get_object_or_404,get_list_or_404,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages

from .forms import *

from .models import *

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request)
            return redirect('../test/afterLogin')
        else:
             messages.success(request,("There was an error-username or password wrong,Try Again"))
             return redirect('../test/login')
    else:
        return render(request,'ebook/test/login.html',{})


# Create your views here.
class livreList(ListView):
    model = Livre
    context_object_name = 'livres'
    template_name = 'ebook/Livres/Index.html'
class livreDetail(DetailView):
    model = Livre
    template_name = 'ebook/test/PageLecture.html'
    context_object_name = 'livre'
class livreList2(ListView):
    model = Livre
    context_object_name = 'livres2'
    template_name = 'ebook/test/touslivres.html'

class livreDetailpdf(DetailView):
    model = Livre
    template_name = 'ebook/test/showPDF.html'
    context_object_name = 'livre1'
class categorieList(ListView):
    model = Categorie
    context_object_name = 'categories'
    template_name = 'ebook/Test/afterLogin.html'
class categorieDetail(DetailView):
    model = Categorie
    template_name = 'ebook/test/showBooks.html'
    context_object_name = 'categorie'

class conList(ListView):
    model = contact
    template_name = 'ebook/test/contact.html'
    context_object_name = 'contact'
class userDetail(DetailView):
    model = User
    template_name = 'ebook/test/profilee.html'
    context_object_name = 'user'
class userdt(DetailView):
    model = User
    template_name = 'ebook/test/EditPassword.html'
    context_object_name = 'user'



#def catdetail(request , id_c):
    #categorie = get_object_or_404(Categorie , pk=id_c)
   # return render(request , 'ebook/test/showBooks.html' ,{'categorie':categorie})

#def Livrelist(request):
#    livress = get_list_or_404(Livre)
#    return render(request , 'ebook/Livres/Index.html' ,{'livres':livress})



def home(request):
    return  render(request, 'ebook/test/home.html' )
def login(request):
    return  render(request, 'ebook/test/login.html' )
def cnx(request):
    form=CreateUserForm()
    context = {'form':form}
    return  render(request, 'ebook/test/register.html',context )
def registerview(request):
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,'aCcounts was created for '+ username)

            #user=authenticate(username=username,password=password)
            #messages.success((request,("Registration successfly")))
            return  redirect("../test/login")
    else:
        form = CreateUserForm()
    return render(request,'ebook/test/register.html',{'form':form})


# Create your views here.
