from django.shortcuts import render
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from .models import User

default_context = {'title': 'OpenMessengerI'}
# Create your views here.
def index(request):
	default_context.update({'title': 'Hello!'})
	return render(request, 'index.html', default_context)
 
# Функция регистрации
# def registration_old(request):
	
# 	data = {}
# 	if request.method == 'POST':
# 		form = RegistrForm(request.POST or None)	
# 		if form.is_valid():
# 			print('Form is valid')
# 			form.save()

# 			return redirect(to=reverse('okey'))
# 	# Создаём форму
# 	# if form.errors:
# 		# data['durak'] = True
# 	# print(form.errors)
# 	# form = RegistrForm() # TODO: понять почему эта строчка всё портит!
# 	# data['form'] = form

# 	# Рендаринг страницы
# 	return render(request, 'registration.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            user.name=form.cleaned_data['name']
            user.save()

            return redirect(to=reverse('okey'))
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', context={'form': form})

def okey(request):
	default_context.update({'title': 'Все нормально'})
	return render(request, 'okey.html', default_context)

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })