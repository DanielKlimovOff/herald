# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# from models import User
 
# Создаём класс формы
# class RegistrForm(UserCreationForm):
#   # Добавляем новое поле Email
#   email = forms.EmailField(max_length=254, help_text='Это поле должно быть заполнено')

#   # Создаём класс Meta
#   class Meta:
#     # Свойство модели User
#     User = get_user_model()
#     model = User
#     # Свойство назначения полей
#     fields = ('name', 'email', 'password1', 'password2')




class RegistrationForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs=dict(required=True, max_length=30, placeholder='Ваш актуальный email')), label=_("Email адрес"),
		error_messages={ 'invalid': _('Email уже существует') })
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,
		render_value=False, placeholder='Придумайте надежный пароль')), label=_("Пароль"), error_messages={ 'invalid': _('Пароли не совпадают') })
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,
		render_value=False, placeholder='Повторите его еще раз')), label=_("Пароль (еще раз)"))
	name = forms.RegexField(regex=r'^\w+$',\
		widget=forms.TextInput(\
			attrs=dict(required=True, max_length=30, placeholder='Представьтесь, пожалуйста')\
		),\
		label=_('Имя'),\
		error_messages={ 'invalid': _('Имя может содержать только буквы') }
	)

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("Пароли не совпадают."))

		email = self.cleaned_data.get('email', None)

		return self.cleaned_data


