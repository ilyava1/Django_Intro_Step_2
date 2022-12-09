from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book
from pprint import pprint
import datetime


def books_view(request, publish_date=None):
    template = 'books/books_list.html'
    context = {}
    books = {}
    context['books'] = books

    if publish_date == None:
        books_objects = Book.objects.all()
        pprint(books_objects)
    else:
        try:
            books_objects = Book.objects.filter(pub_date=publish_date)
        except:
            print('Error')
    if publish_date == None:
        context['pagi'] = False
    else:
        pub_dates = []
        for book in Book.objects.all():
            pub_dates.append(datetime.datetime.strptime(str(book.pub_date), '%Y-%m-%d'))
        pub_dates.sort()
        print('pub_dates = ', pub_dates)
        datetime_publish_date = datetime.datetime.strptime(publish_date, '%Y-%m-%d')
        print('datetime_publish_date = ', datetime_publish_date)
        index = pub_dates.index(datetime_publish_date)
        print('index = ', index)
        if index != 0:
            previous_pub_date = pub_dates[index - 1].date()
        else:
            previous_pub_date = None
        if index != len(pub_dates) - 1:
            next_pub_date = pub_dates[index + 1].date()
        else:
            next_pub_date = None
        # print('!!!!!!!!!!!!previous_pub_date = ', previous_pub_date)
        # print('!!!!!!!!!!!!next_pub_date = ', next_pub_date)

        context['previous_pub_date'] = previous_pub_date
        context['next_pub_date'] = next_pub_date
        context['pagi'] = True
    for book in books_objects:
        books[book.name] = {'id': book.id,
                            'author': book.author,
                            'pub_date': book.pub_date
                            }

    return render(request, template, context)
