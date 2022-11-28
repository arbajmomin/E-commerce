from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name ="ShopHome"),
    path('about/',views.about,name= "about us"),
    path('contact/',views.contact,name= "contact"),
    path('productView/',views.productView,name= "productView"),
    path('tracker/',views.tracker,name= "tracker"),
    path('search/',views.search,name= "search"),
    path('checkout/',views.checkout,name= "checkout")
]