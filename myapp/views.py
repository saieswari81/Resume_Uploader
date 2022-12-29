from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.


class HomeView(View):

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        # print('pk: ', pk)
        if pk is not None:
            candit = Resume.objects.get(id=pk)
            return render(request, 'myapp/candit-detail.html', {'candit': candit})
        form = ResumeForm()
        resume = Resume.objects.all()
        return render(request, 'myapp/home.html', {'form': form, 'resume': resume})

    def post(self, request, **kwargs):
        pk = kwargs.get('pk')
        # print('pk: ', pk)  # This is for debugging purpose only
        if pk is not None:
            # print('pk: ', pk)  # This is for debugging purpose only
            res = Resume.objects.get(id=pk)
            res.delete()
            return redirect('home')
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # Trying to rename the image and resume before saving, but could not do it yet. wil try later.
            # name = form.cleaned_data['name']
            # my_file = form.cleaned_data['my_file']
            # print('name: ', name)
            # print('my_file: ', my_file)
            # form.cleaned_data['my_file'] = name + (my_file)  # This is causing error : Concatenate only strings.
            # my_file = form.cleaned_data['my_file']
            # print('my_file: ', my_file)

            form.save()
            # return render(request, 'myapp/home.html', {'form': form})
            return redirect('home')
