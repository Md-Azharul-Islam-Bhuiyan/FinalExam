from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from book.models import BookModel
from django.contrib.auth.models import User
from auth_user.forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import  FormView, View, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'auth_user/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # print(form.cleaned_data)
        user=form.save()
        login(self.request, user)
        # print(user)

        messages.success(self.request, f'Account Successfully Created')
        return super().form_valid(form)


@login_required
def profile(request):
    data = BookModel.objects.filter(posted_user = request.user)
    return render(request, 'auth_user/Dashboard.html', {'data': data})
    

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    pk_url_kwarg = 'id'
    template_name = 'auth_user/editProfile.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)

    
class UserLoginView(LoginView):
    template_name = 'auth_user/login.html'
    def get_success_url(self):
        messages.success(self.request ,'Logged in Successfully')
        return reverse_lazy('home')

class UserLogoutView(View):
    
    def get(self, request):
        logout(request)
        messages.success(self.request ,'Logged Out Successfully')
        return redirect('home')
