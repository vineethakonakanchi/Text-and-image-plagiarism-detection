from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("Register.html", views.Register, name="Register"),
	       path("Signup", views.Signup, name="Signup"),
	       path("Login.html", views.Login, name="Login"),
	       path("UserLogin", views.UserLogin, name="UserLogin"),
	       path("UploadSource", views.UploadSource, name="UploadSource"),
	       path("UploadSourceImage", views.UploadSourceImage, name="UploadSourceImage"),
	       path("UploadSuspiciousFile", views.UploadSuspiciousFile, name="UploadSuspiciousFile"),
	       path("UploadSuspiciousFileAction", views.UploadSuspiciousFileAction, name="UploadSuspiciousFileAction"),
	       path("UploadSuspiciousImage", views.UploadSuspiciousImage, name="UploadSuspiciousImage"),
	       path("UploadSuspiciousImageAction", views.UploadSuspiciousImageAction, name="UploadSuspiciousImageAction"),
	       
]