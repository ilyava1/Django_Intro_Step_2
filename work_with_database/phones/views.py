from django.shortcuts import render
from phones.models import Phone
from django.http import HttpResponse
from phones.service.service_values import sorting_types


def show_catalog(request, sort_type=None):
    """
    Функция формирования контекста для отображения содержимого каталога
    телефонов
    :param request:
    :param sort_type: тип выбранной пользователем сортировки в каталоге
    :return:
    """

    template = 'catalog.html'
    context = {}
    phones = {}
    context['phones'] = phones

    if sort_type == sorting_types[0]:
        phone_objects = Phone.objects.order_by('name')
    elif sort_type == sorting_types[1]:
        phone_objects = Phone.objects.order_by('price')
    elif sort_type == sorting_types[2]:
        phone_objects = Phone.objects.order_by('-price')
    elif sort_type == None:
        phone_objects = Phone.objects.all()
    else:
        return HttpResponse('Такой страницы не существует')

    for phone in phone_objects:
        phones[phone.name] = {'id': phone.id,
                              'image': phone.image,
                              'price': phone.price,
                              'release_date': phone.release_date,
                              'lte_exists': phone.lte_exists,
                              'slug': phone.slug,
                            }

    return render(request, template, context)


def show_product(request, slug):
    """
    Функция формирования контекста для страницы продукта (телефона)
    :param request:
    :param slug: слагофицированное название телефона - выбор пользователя
    :return:
    """
    template = 'product.html'
    context = {}
    found_phone = {}
    phone_objects = Phone.objects.all()
    for phone in phone_objects:
        if phone.slug == slug:
            found_phone = {
                'id': phone.id,
                'name': phone.name,
                'image': phone.image,
                'price': phone.price,
                'release_date': phone.release_date,
                'lte_exists': phone.lte_exists,
            }
            break
    context['phone'] = found_phone

    return render(request, template, context)
