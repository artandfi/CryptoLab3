from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from main.models import Message
from main.forms import MessageForm, SignUpForm

class HomeView(TemplateView):
    model = Message
    template_name = 'home.html'



class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        form.instance.sender = self.request.user.profile

        if form.is_valid():
            form.instance.save()
        
        return HttpResponseRedirect(reverse('main:home'))

def home(request):
    form = MessageForm()
    messages = Message.objects.all()
    return render(request, 'home.html', {'form': form, 'messages': messages})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

