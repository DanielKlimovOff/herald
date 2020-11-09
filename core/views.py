from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import RegistrForm

default_context = {'title': 'OpenMessengerI'}
# Create your views here.
def index(request):
	default_context.update({'title': 'Hello!'})
	return render(request, 'index.html', default_context)
 
# Функция регистрации
def registration(request):
	# Массив для передачи данных шаблонны
	data = {}
	# Проверка что есть запрос POST
	if request.method == 'POST':
		# Создаём форму
		form = RegistrForm(request.POST)
		# Валидация данных из формы
		if form.is_valid():
			# Сохраняем пользователя
			form.save()
			# Передача формы к рендару
			data['form'] = form
			# Передача надписи, если прошло всё успешно
			data['res'] = "Всё прошло успешно"
			# Рендаринг страницы
			return render(request, 'registration.html', data)
	else: # Иначе
		# Создаём форму
		form = RegistrForm()
		# Передаём форму для рендеринга
		data['form'] = form
		# Рендаринг страницы
		return render(request, 'registration.html', data)

def okey(request):
	default_context.update({'title': 'Все нормально'})
	return render(request, 'okey.html', default_context)