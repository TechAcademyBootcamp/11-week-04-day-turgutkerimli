from django.shortcuts import render
from myapp.models import *
from django.db.models import Sum, Avg

# Create your views here.

def hw1_1():
    book = Book.objects.all()
    print(book) 

    category = Category.objects.all()
    print(category) 

    author = Author.objects.all()
    print(author)

def hw1_2():
    book = Book.objects.filter(price__lte = 250)
    print(book)

def hw1_3():
    author = Author.objects.filter(date_of_birth__year__lte = 1980)
    print(author)

def hw1_4():
    book = Book.objects.filter(title__icontains = "a")
    print(book)
    category = Book.objects.filter(title__icontains = "a" )
    print(category)

def hw1_5():
    author = Author.objects.filter(fullname__contains = "Daniel Defoe")
    print(author)

def hw1_6():
    author = Author.objects.exclude(nationality__contains = "British")
    print(author)

def hw1_7():
    book = Book.objects.filter(author__fullname__startswith = "D")
    print(book)

def hw1_8():
    book = Book.objects.filter(author__gender__startswith = "Kişi")
    print(book)

def hw1_9():
    book = Book.objects.filter(category__title__endswith = "e")
    print(book)

def hw1_10():
    book = Book.objects.get(pk = 3)
    print(book)

def hw1_11():
    pass


def hw2_1():
    books = Book.objects.all().update(category='update')
    print(books)

def hw2_2():
    books = Book.objects.filter(author__gender=2).update(price=13.8)
    print(books)

def hw2_3():
    books = Book.objects.all().delete(page_count__gte=200)
    print(books)

def hw2_4():
    authors = Author.objects.filter(fullname__icontains='a').order_by(date_of_birthday)
    print(authors)

def hw2_5():
    books = Book.objects.all().distinct()
    print(books)

def hw2_6():
    new_author = Author.objects.get(id=1)
    books, created = Book.objects.get_or_create(
        author = new_author, title="Tech Academy", description="XXX", price=112, page_count=235, cover_image = "/images/1.jpeg"
        )
    if created:
        cat1 = Category.objects.get(id=2)
        cat2 = Category.objects.get(id=3)
        books.category.add(cat1,cat2)
    print(books)

def hw2_7():
    books = Book.objects.filter(category__title='Novel').count()
    print(books)

def hw2_8():
    book = Book.objects.first()
    print(books)

    authors = Author.objects.last()
    print(authors)


def hw2_9():
    books = Book.objects.order_by('id').reverse()[:3]
    print(books)

def hw2_10():
    price_sum = Book.objects.aggregate(Sum('price'))
    print(price_sum)

    price_avg = Book.objects.aggregate(Avg('price'))
    print(price_avg)

def hw2_11():
    pass

def hw2_12():
    page = Book.objects.filter(page_count__lt=200)
    print(page)

    price = Book.objects.filter(price__gt=15)
    print(price)

