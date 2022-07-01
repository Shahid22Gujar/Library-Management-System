from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from home.models import Books, User
from .forms import BookRegistration,LoginForm,SignUpForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def home(request):
   
    if request.method=="POST":
        fm=BookRegistration(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
        return HttpResponse("Bookadded")
    fm=BookRegistration()
   
    
    user=request.user
    print(user.id)
    user_obj=User.objects.get(id=user.id)
    if user_obj.role=="Admin":
        book=Books.objects.all()
        context={'form':fm,'data':book}
        return render(request,'home/admin_home.html',context)
    else:
        context=Books.objects.select_related('user').filter(user=user_obj)
        return render(request,'home/student_home.html')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # form = LoginForm(request=request,data=request.POST)
            # if form.is_valid():
            uname = request.POST.get('email')
            upass = request.POST.get('password')

            user = authenticate(email=uname,password = upass)
            print(user)
            if user is not None:
                login(request,user)
                # messages.success(request,'Logged in Successfully')
                return redirect('/')
        else:
            
            return render(request,'home/login.html')
    else:
        return redirect('/login')

def update_book(request,id):
    if request.method == "POST":
        book= Books.objects.get(pk=id)
        fm = BookRegistration(request.POST,instance=book)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Book Update")
    book= Books.objects.get(pk=id)
    fm = BookRegistration(instance=book)

    context={'form':fm}
    return render(request,'home/update_book.html',context)

def delete_book(request,id):
    book=Books.objects.get(id=id)
    book.delete()
    return redirect('/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

#SignUp
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # messages.success(request,'Congratulations!!,You are a Author now.')
            email=form.cleaned_data['email']
            """Checking if user already exists"""
            user_obj=User.objects.filter(email=email)
            if user_obj is not None:
               return redirect('/signup')
            else:
                form.save()
                form = SignUpForm()#for clear form after submitting
                return redirect('/login')
    else:
        form = SignUpForm()
    return render(request,'home/signup.html',{'form':form})