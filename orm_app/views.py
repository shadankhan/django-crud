from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
# from orm_app.forms import RecForm, CanForm
from orm_app.models import Profile, Post_ad
from .serializers import ProfileSerializer, Post_adSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# # Create your views here.
# # Retrieve Function

# class ProfilePagination(PageNumberPagination):
# 	page_size=1

# class All_profile(generics.ListCreateAPIView):
# 	queryset =Profile.objects.all()
# 	serializer_class=ProfileSerializer
# 	pagination_class = ProfilePagination

# class Profile_detail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset =Profile.objects.all()
# 	serializer_class=ProfileSerializer

# class Post_ad(generics.ListCreateAPIView):
# 	queryset =Post_ad.objects.all()
# 	serializer_class=Post_adSerializer


# class Profile_detail(APIView):
# 	def get_object(self, pk):
# 		try:
# 			return Profile.objects.get(pk=pk)
# 		except Profile.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk):
# 		profile = self.get_object(pk)
# 		serializer = ProfileSerializer(profile)
# 		return Response(serializer.data)

# 	def put(self, request, pk):
# 		profile = self.get_object(pk)
# 		serializer = ProfileSerializer(profile, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors)

# 	def delete(self, request, pk):
# 		profile = self.get_object(pk)
# 		profile.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def all_profile(request):
# 	if request.method == "GET":
# 		profile = Profile.objects.all()
# 		serializer = ProfileSerializer(profile, many=True)

# 		return Response(serializer.data)
	
# 	elif request.method =="POST":
# 		serializer = ProfileSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)

# 		return Response(serializer.errors)

# @api_view(['GET','PUT', 'DELETE'])
# def profile_detail(request, pk):
# 	try:
# 		profile = Profile.objects.get(pk=pk)
# 	except Profile.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == "GET":
# 		serializer = ProfileSerializer(profile)
# 		return Response(serializer.data)
# 	elif request.method == "PUT":
# 		serializer = ProfileSerializer(profile, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors)
# 	elif request.method == "DELETE":
# 		profile.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
	ads = Post_ad.objects.all()
	paginator = Paginator(ads, 3)

	page = request.GET.get('page')
	try:
		ads = paginator.page(page)
	except PageNotAnInteger:
		ads = paginator.page(1)
	except EmptyPage:
		ads = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {'ads':ads})

def profile(request):
	if request.method == 'POST' and request.FILES.items():

		city = request.POST.get('city',)
		contact_number = request.POST.get('contact_number',)
		image = request.FILES['image']

		profile, created = Profile.objects.get_or_create(
			user=request.user,
			city=city,
			contact_number=contact_number,
			image=image,

			)
		return HttpResponseRedirect('/')
	else:
		return render(request, 'profile.html')

@login_required 
def ads_post(request):
	if request.method == 'POST' and request.FILES.items():

		title = request.POST.get('title',)
		description = request.POST.get('description',)
		image = request.FILES['image']
		price = request.POST.get('price',)

		post_ad, created = Post_ad.objects.get_or_create(
			profile=request.user.profile_set.get(),
			title=title,
			description=description,
			image=image,
			price=price

			)
		return HttpResponseRedirect('/orm/all_ads')
	else:
		return render(request, 'post_ad.html')

def all_ads(request):
	ads = Post_ad.objects.all().order_by('-pub_date')
	query = request.GET.get('q')
	if query:
		ads = ads.filter(title__icontains=query)
	paginator = Paginator(ads, 3)

	page = request.GET.get('page')
	try:
		ads = paginator.page(page)
	except PageNotAnInteger:
		ads = paginator.page(1)
	except EmptyPage:
		ads = paginator.page(paginator.num_pages)

	return render(request, 'all_ads.html', {'ads':ads})
# Create Function
# def rec(request):
# 	form = RecForm()
# 	if request.method == 'POST':
# 		form = RecForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return index(request)
# 		else:
# 			print("Error")

# 	return render(request, 'rec.html', {'form':form} )

# # Create Function
# def can(request):
# 	form = CanForm()
# 	if request.method == 'POST':
# 		form = CanForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return index(request)
# 		else:
# 			print('Error')

# 	return render(request, 'can.html', {'form':form})


# def rec_detail(request, id):
# 	rec = Recruiter.objects.get(id=id)
# 	return render(request, 'detail.html', {'rec':rec})
	
# # Upadate Function
# def update_rec(request, id):
# 	form = RecForm()
# 	if request.method == 'POST':
# 		obj = get_object_or_404(Recruiter, id=id)
# 		form = RecForm(request.POST, instance=obj)

# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/orm/rec/'+id)
# 		else:
# 			print("Error")

# 	return render(request, "update.html", {'form':form})

# # Delete Function
# def delete_rec(request, id):
# 	obj = get_object_or_404(Recruiter, id=id)
# 	if request.method == 'POST':
# 		obj.delete()
# 		return HttpResponseRedirect('/')
# 	return render(request, 'delete.html', {'obj':obj})