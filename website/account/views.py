from django.shortcuts import redirect,render
from django.contrib.auth import  authenticate , login , logout
from django.contrib.auth.models  import User
from django.contrib import messages
# Create your views here.
def user_login(request):

    if request.user.is_authenticated:
        return  redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            messages.add_message(request, messages.SUCCESS, "giriş başarılı")
            return redirect("index")   #anasayfaya yönlendirildi

        else:
            messages.add_message(request, messages.ERROR, "Kullanıcı adı ya da şifre yanlış")
            return render(request , "account/login.html"  )


    else:
       return render (request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.ERROR, "Kullanıcı adı kullanılıyor.")
                return render(request, "account/register.html")
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, "e-mail kullanılıyor")
                    return render(request, "account/register.html")
                else:
                    user= User.objects.create_user(username=username , email=email , password=password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, "Üye olundu")
                    return redirect("user_login")
        else:
            messages.add_message(request, messages.ERROR, "parola eşleşmiyor")
            return render(request, "account/register.html" )
    else:
         return render (request, "account/register.html")

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "çıkış başarılı")
    logout(request)
    return redirect("index")
