from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from .models import CallBack, Movie, TeamList
from .forms import CallBackForm
from django.http import HttpResponse

# class MoviesView(View):
#     def get(self,request):
#         movies = Movie.objects.all()
#         return render(request, "appss/index.html",{"movie_list": movies})
class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        teams = TeamList.objects.all()
        if request.method=="POST":
            contact=CallBack()
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            contact.name=name
            contact.email=email
            contact.message=message
            contact.save()
            return HttpResponse("<h1>THANKS FOR CONTACT US<h1> <a href='/'> Go back</a>")
        return render(request, 'appss/index.html', {"movie_list": movies, "team_list": teams})


# class ClientMsg(TemplateView):
    
    # template_name = "appss/index.html"
    # def get(self, request):
    #     form = CallBackForm()
    #     callback = CallBack.objects.all()

    #     args = {'form': form,'callback':callback}
    #     return render(request, self.template_name, )

    # def post(self,request):
    #     form = CallBackForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.email = request.email
    #         post.save()
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']

    #         form = CallBackForm()
    #         return redirect('index:index')
    #     arga = {'form':form,'name':name,'email':email,'message':message }
    #     return render(request, self.template_name, args)

