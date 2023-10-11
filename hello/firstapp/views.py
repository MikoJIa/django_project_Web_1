import random
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from random import randint
from django.views.generic import TemplateView
from .forms import UserForm, ImageForm, FileForm, VideoFileForm, AudioForm
from .models import Person, Image, File, VideoFile, AudioFile


def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные аудиофайлы'
    form = AudioForm()
    audio_obj = AudioFile.obj_audio.all()
    context = {
        'my_text': my_text,
        'audio_obj': audio_obj,
        'form': form
    }
    return render(request, 'firstapp/form_up_audio.html', context)


def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Объект не найден</h1>')


def form_up_video(request):
    if request.method == 'POST':
        form = VideoFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные видеофайлы'
    form = VideoFileForm()
    video_file_obj = VideoFile.obj_video.all()
    context = {
        'my_text': my_text,
        'form': form,
        'video_file_obj': video_file_obj
    }
    return render(request, 'firstapp/form_up_video.html', context)


def delete_video(request, id):
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Объект не найден</h1>')


def form_up_pdf(request):  # функция для загрузки файлов
    if request.method == 'POST':  # если запрос от пользователя на загрузку файла
        form = FileForm(request.POST, request.FILES)  # то тогда на основе класса созд. оъект form
        # который получает запрос от пользователя на сохранение данных
        if form.is_valid():  # если форма заполнена правильно то
            form.save()  # мы сохраняем введённые пользователем данные
    my_text = 'Загруженные файлы'
    form = FileForm() # объект form, который создается на основе класса FileForm (т. е. сама форма);
    file_obj = File.objects.all()  # объект form, который создается на основе класса FileForm (т. е. сама форма);
    context = {
        'my_text': my_text,
        'form': form,
        'file_obj': file_obj,
    }
    return render(request, 'firstapp/form_up_pdf.html', context)


def delete_pdf(request, id):
    try:
        file_pdf = File.objects.get(id=id)
        file_pdf.delete()
        return redirect('form_up_pdf')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Объект не найден</h1>')


#  функция для загрузки изображений
def form_up_image(request):
    if request.method == 'POST':  # Проверяем условие, поступил ли запрос от пользователя
        form = ImageForm(request.POST, request.FILES)  # создаём обьект форм, который получает запрос от пользователя
        # на сохранение данных об изображения, и сам загруженный файл request.FILES
        if form.is_valid():
            form.save()
    # Если форма вызывается первый раз, т. е. поступил запрос GET, то создаются:
    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()  # который принимает из БД все сведения о загруженных изображениях;
    form = ImageForm()  # объект form, который создается на основе класса ImageForm (т. е. сама форма).
    context = {
        'my_text': my_text,
        'my_img': my_img,
        'form': form
    }
    return render(request, 'firstapp/form_up_image.html', context)


# Удаление изображения из БД
def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_image')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Объект не найден</h1>')


def index(request):
    my_text = 'Изучаем формы Django'
    col_people = Person.objects_person.count()
    context = {
        'my_text': my_text,
        'col_people': col_people,
    }
    return render(request, "firstapp/index.html", context)


def name(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_app1')
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'firstapp/name.html', context)


# Взаимодействие с формой ввода данных о клиентах
def my_form(request):
    if request.method == 'POST':  # Пользовател отправил данные
        form = UserForm(request.POST)  # создание экземпляра формы
        if form.is_valid():  # проверяем форму на волидность
            # name = request.POST.get('name')  # получить значение поля Имя
            # age = request.POST.get('age')    # получить значение поля Возраст
            form.save()  # запись формы в БД
            # остаёмся на той же странице, обновляем форму
            # output = "<h2>Пользователь</h2><h3>Имя - {0} Возраст - {1}<h3>".format(name, age)
            # return HttpResponse(output)
    # загрузить форму для ввода клиента
    my_text = 'Сведения о клиентах'
    people = Person.objects_person.all()
    form = UserForm()
    context = {
        'form': form,
        'my_text': my_text,
        'people': people
    }
    return render(request, 'firstapp/my_form.html', context)


def edit_form(request, id):
    person = Person.objects_person.get(id=id)
    # если пользователь вернул отредактированные данные
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('my_form')
    # если пользователь отправляет данные на редактирование
    data = {'person': person}
    return render(request, 'firstapp/edit_form.html', data)


# Удаление данных о клиенте из БД
def delete(request, id):
    try:
        person = Person.objects_person.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Объект не найден</h1>')


def index_app1(request):
    user = Person.objects.all()
    context = {
        'user': user
    }
    return render(request, 'firstapp/index_app1.html', context)


def home(request):
    return render(request, 'firstapp/home.html')


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return render(request, 'firstapp/contact.html')


def product(request, product_id=1):
    output = '<h2>Продукт № {0}</h2>'.format(product_id)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = '<h2>Пользователь:<h2><h3>id: {0} Имя: {1}</h3>'.format(id, name)
    return HttpResponse(output)


def products(request, product_id=1):
    category = request.GET.get("cat", "Не задано")
    output = '<h2>Продукт: {0} Категория: {1}</h2>'.format(product_id, category)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect('/')


def m304(request):
    return HttpResponseNotModified()


def m400(request):
    return HttpResponseBadRequest('<h1>Bad request: Heкoppeктныe данные</h1>')


def m403(request):
    return HttpResponseForbidden('<h1>Forbidden: Доступ заблокирован: недостаточно лет</h1>')


def m404(request):
    return HttpResponseNotFound('<h1>Not found</h1>')


def m405(request):
    return HttpResponseNotAllowed('<h1>Method is not Allowed</h1>')


def m410(request):
    return HttpResponseGone('<h1>Content is not longer here</h1>')


def m500(request):
    return HttpResponseServerError('<h1>Something is wrong</h1>')


def access(request, age):
    if age not in range(1, 111):
        return m400(request)
    if age > 17:
        return HttpResponse('Доступ разрешён')
    else:
        return m403(request)

