from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("login",views.login,name="login"),
    path("",views.home,name="home"),
    path("dogs",views.dogs,name="dogs"),
    path("cats",views.cats,name="cats"),
    path("birds",views.birds,name="birds"),
    path("fishes",views.fishes,name="fishes"),
    path("rabbits",views.rabbits,name="rabbits"),
    path("gunniepigs",views.gunniepigs,name="gunniepigs"),
    path("signup",views.signup,name="signup"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("temp",views.temp,name="temp"),
    path("owner",views.ownerpage,name="owner"),
    path("deleteuser/<int:uid>",views.deleteuser,name="deleteuser"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("viewproductsinowner", views.viewproductsinowner, name="viewproductsinowner"),
    path("deleteproduct/<int:uid>",views.deleteproduct,name="deleteproduct"),
    path("forgotpassword",views.forgotpassword,name="forgotpassword"),
    path("changepassword",views.changepassword,name="changepassword"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("contactus",views.contactus,name="contactus"),
    path("rescue",views.rescue,name="rescue")

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)