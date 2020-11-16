# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
 
 
# Создаём класс формы
class RegistrForm(UserCreationForm):
  # Добавляем новое поле Email
  email = forms.EmailField(max_length=254, help_text='Это поле должно быть заполнено')
  
  # Создаём класс Meta
  class Meta:
    # Свойство модели User
    User = get_user_model()
    model = User
    # Свойство назначения полей
    fields = ('name', 'email', 'password1', 'password2')


