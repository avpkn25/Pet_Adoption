from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from .forms import ProductForm
from .models import SignUpData, Product, Owners, ForgotPassword
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'index.html');

def dogs(request):
    return render(request,'mainpages/dogs.html')

def cats(request):
    return render(request,'mainpages/cats.html')

def birds(request):
    return render(request,'mainpages/birds.html')

def fishes(request):
    return render(request,'mainpages/fishes.html')

def rabbits(request):
    return render(request,'mainpages/rabbits.html')

def gunniepigs(request):
    return render(request,'mainpages/gunniepigs.html')
def login(request):
    return render(request,'signup.html');

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['email']
        pwd=request.POST['pass']
        flag = SignUpData.objects.filter(sign_email=emailid).first()
        if flag:
            message = "Email already exists!"
            return render(request, "signup.html", {'message': message})
        signobj = SignUpData(sign_name=name,sign_email=emailid,sign_password=pwd)
        SignUpData.save(signobj)
        return render(request,"signup.html")
    return render(request,"signup.html")

def checkuserlogin(request):
    emailid=request.POST["logemail"]
    pwd=request.POST["logpass"]
    flag=SignUpData.objects.filter(Q(sign_email=emailid) & Q(sign_password=pwd))
    flag1 = Owners.objects.filter(Q(email=emailid) & Q(password=pwd))
    if flag1:
        admin = Owners.objects.get(email=emailid)
        usersdata = SignUpData.objects.all()
        userscount = SignUpData.objects.count()
        request.session["emailid"] = admin.email
        request.session["uname"] = admin.username
        return render(request, "owner.html",{"uname": admin.username,"users": usersdata,"count":userscount})
    else:
        if flag:
            user = SignUpData.objects.get(sign_email=emailid)
            request.session["uname"] = user.sign_name
            request.session["email"] = user.sign_email
            return render(request, "index.html", {"uname": user.sign_name,"user":user})
        else:
            message = 'Incorrect password (or) user not found! Signup'
            return render(request,"signup.html",{"message":message})

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = SignUpData.objects.filter(sign_email=email).first()
        if user:
            subject = "Request to change the password"
            reset_link = "http://127.0.0.1:8000/changepassword"
            message = f"Click the following link to reset your password: {reset_link}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return HttpResponse("<h1 align=center>Mail sent Successfully</h1>")
        else:
            error_message = "User not found. Please enter a valid email address."
            return render(request, "forgotpassword.html", {"error_message": error_message})
    return render(request, "forgotpassword.html")

def ownerpage(request):
    usersdata = SignUpData.objects.all()
    userscount = SignUpData.objects.count()
    return render(request, "owner.html", {"users": usersdata,"count":userscount})

def deleteuser(request,uid):
    SignUpData.objects.filter(id=uid).delete()
    return redirect("owner")

def addproduct(request):
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addproduct.html", {"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"productform":form})

def temp(request):
    return render(request,"temp.html")

def viewproductsinowner(request):
    mail=request.session["emailid"]
    flag1 = Owners.objects.filter(Q(email=mail))
    p = Owners.objects.filter(email=mail)
    if flag1:
        key = p[0].secure_key
    # productlist = Product.objects.filter(secure_key=key)
    # count = Product.objects.filter(secure_key=key).count()
        productlist = Product.objects.all()
        count = Product.objects.count()
        return render(request,"viewproductsinowner.html",{"productlist":productlist,"count":count})
    else:
        message = 'Resered for owners!'
        return render(request, "signup.html", {"message": message})

def deleteproduct(request,uid):
    Product.objects.filter(id=uid).delete()
    return redirect("viewproductsinowner")

def userlogout(request):
    request.session.flush()
    return render(request,"index.html")

def changepassword(request):
    return render(request,"changepassword.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def rescue(request):
    return render(request,"rescue.html")