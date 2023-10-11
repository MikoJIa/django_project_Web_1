from django import forms
from .models import Person, Image, File, VideoFile, AudioFile


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name', 'age']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # fields = ['title', 'image']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        # fields = ['title', 'file']


class VideoFileForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'

        # name = forms.CharField(label='Имя клиента',
        #                     widget=forms.TextInput(attrs={'class': 'myfield'}))
        # age = forms.IntegerField(label='Возраст клиента',
        #                         widget=forms.NumberInput(attrs={'class': 'myfield'}))
    # required_css_class = 'field'
    # error_css_class = 'error'
    # # comment = forms.CharField(label='Комментарий', widget=forms.Textarea)
    # email = forms.EmailField(label='Электронный адрес')
    # advertising = forms.BooleanField(label='Вы согласны получать рекламу?',
    #                                  required=False)
    # field_order = ['age', 'name']  # Задание порядка следования полей на форме

    # name = forms.CharField(label='Имя клиента', initial=' Enter name',
    #                        help_text='Имя не более 20 символов', max_length=20)
    # age = forms.IntegerField(label='Возраст клиента', help_text='Введите ваш возраст!!!')
    # date = forms.DateField(label='Введите дату')
    # date_time = forms.DateTimeField(label='Введите дату и время')
    # num = forms.DecimalField(label='Введите десятичное число')
    # time_delta = forms.DurationField(label='Промежуток времени')
    # email = forms.EmailField(label='Введите адрес электронной почты',
    #                          help_text='обязательный символ @')
    # file = forms.FileField(label='Файл')
    # ip_adres = forms.GenericIPAddressField(label='IP-адрес',
    #                                        help_text='Пример формата ввода: 192.0.2.0')
    # basket = forms.BooleanField(label='Положить товар в корзину', required=False)
    # file_img = forms.ImageField(label='Изображение')
    # json_file = forms.JSONField(label='Данные формата - JSON')
    # country = forms.MultipleChoiceField(label='Выберете страну',
    #                                     choices=((1, 'Англия'),
    #                                              (2, 'Франция'),
    #                                              (3, 'Америка'),
    #                                              (4, 'Германия')))
    # vyb = forms.NullBooleanField(label='вы поедите этим за границу летом?')
    # combo_text = forms.ComboField(label='Введите данные',
    #                               fields=[
    #                                   forms.CharField(max_length=20),
    #                                   forms.EmailField()
    #                               ])
    # ling = forms.ChoiceField(label='Выберите язык', choices=((1, 'Английский'),
    #                                                          (2, 'Немецкий'),
    #                                                          (3, 'Французский')))


