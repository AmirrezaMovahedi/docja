from django.urls import path
from doc_ja_app.views import *
from django.contrib.auth import views as auth_views

app_name = "doc_ja_app"


urlpatterns = [

    path('', index_view, name='index'),

    path('doctor_list/', doctor_list_view, name="doctor_list"),
    # path('doctor_list/<str:expert>', doctor_list_view, name="doctor_list_expert"),
    path('doctor_detail/<pk>', doctor_detail_view, name="doctor_detail"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='done'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url='/docja/password_reset/complete'),
         name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='done'), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('doctor_register/', doctor_register_view, name="doctor_register"),
    path('web_user_register/', web_user_register_view, name="web_user_register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('doctor_edit/', doctor_account_edit_view, name='doctor_edit'),
    path('web_user_edit/', web_user_account_edit_view, name='web_user_edit'),

    path('doctor_like/', doctor_like, name='doctor_like'),

    path('search/', search_view, name='search'),
    path('send/comment/<pk>', doctor_comment_view, name='send_comment'),
    path('reservation/', reservation_view, name='reservation'),
    path('about_us/', about_us_view, name='about_us'),
]