from django.urls import path
from orm_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('rec/', views.rec , name="rec"),
    path('can/', views.can , name="can"),
    path('rec/<id>', views.rec_detail , name="rec_detail"),
    path('update/<id>', views.update_rec , name="update_rec"),
    path('rec/<id>/delete', views.delete_rec , name="delete_rec"),
]