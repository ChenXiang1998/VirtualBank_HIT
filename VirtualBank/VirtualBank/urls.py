"""VirtualBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.login_html),
    path('login/', views.login),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('viewuserinf/', views.viewuserinf),
    path('edituserinf/', views.edituserinf),
    path('cardmanage/', views.cardmanage),
    path('cardmanage/showcardinsert/', views.showcardinsert),
    path('addcard/', views.addcard),
    path('transfer/',views.transfer),
    path('viewtransfer/', views.viewtransfer),
    path('userdeposit/', views.userdeposit),
    path('userdraw/', views.userdraw),
    path('viewdrawdeposit/', views.viewdrawdeposit),
    path('editpasswd/', views.editpasswd),

    path('pay', views.pay),
    path('mall_pay/', views.mall_pay),
    path('mall_ackpay/', views.mall_pay),
 #   path('back_mall/', views.back_mall)
  #  path('t1/', views.t1),
#    path('t2/', views.t2)
]
