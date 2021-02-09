from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from orm_app.forms import RecForm, CanForm
from orm_app.models import Recruiter, Candidate
# Create your views here.
# Retrieve Function
def index(request):
	rec = Recruiter.objects.all()
	can = Candidate.objects.all()
	return render(request, 'index.html', {'rec':rec, 'can':can})


# Create Function
def rec(request):
	form = RecForm()
	if request.method == 'POST':
		form = RecForm(request.POST)

		if form.is_valid():
			form.save()
			return index(request)
		else:
			print("Error")

	return render(request, 'rec.html', {'form':form} )

# Create Function
def can(request):
	form = CanForm()
	if request.method == 'POST':
		form = CanForm(request.POST)

		if form.is_valid():
			form.save()
			return index(request)
		else:
			print('Error')

	return render(request, 'can.html', {'form':form})


def rec_detail(request, id):
	rec = Recruiter.objects.get(id=id)
	return render(request, 'detail.html', {'rec':rec})
	
# Upadate Function
def update_rec(request, id):
	form = RecForm()
	if request.method == 'POST':
		obj = get_object_or_404(Recruiter, id=id)
		form = RecForm(request.POST, instance=obj)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/orm/rec/'+id)
		else:
			print("Error")

	return render(request, "update.html", {'form':form})

# Delete Function
def delete_rec(request, id):
	obj = get_object_or_404(Recruiter, id=id)
	if request.method == 'POST':
		obj.delete()
		return HttpResponseRedirect('/')
	return render(request, 'delete.html', {'obj':obj})