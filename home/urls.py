from django.urls import path
from home.views import home,user_login,signup,update_book,delete_book,user_logout

urlpatterns = [
    path('', home,name="home"),
    path('login/', user_login,name="login"),
    path('signup/', signup,name="signup"),
    path('logout/',user_logout,name='logout'),
    path('update/<int:id>/', update_book,name="updatedata"),
    path('delete/<int:id>/', delete_book,name="deletedata"),
]
