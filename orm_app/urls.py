from django.urls import path
from orm_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('profile/', views.profile , name="profile"),
    path('post/', views.ads_post , name="ads_post"),
    path('all_ads/', views.all_ads , name="all_ads"),
    # path('rec/<id>', views.rec_detail , name="rec_detail"),
    # path('update/<id>', views.update_rec , name="update_rec"),
    # path('rec/<id>/delete', views.delete_rec , name="delete_rec"),

    # api path======================
    # path('api/all_profile', views.All_profile.as_view(), name="all_profile"),
    # path('api/profile/<pk>', views.Profile_detail.as_view(), name="profile_detail"),
    # path('api/all_post', views.Post_ad.as_view(), name="Post_ad"),
    
]