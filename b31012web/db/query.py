from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import Author, Blog, Entry
def create():

    for e in Author.objects.all():
        e.delete()
    for e in Blog.objects.all():
        e.delete()


    a1 = Author(name = 'a1', email = 'a1@moc.com')
    a1.save()    
    a2 = Author(name = 'a2', email = 'a2@moc.com')
    a2.save()    
    blog1 = Blog(name='blog1')
    blog1.save()
    blog2 = Blog(name='blog2')
    blog2.save()
    entry1 = Entry(blog = blog1, headline = 'headline1')
    entry1.save()
    entry1.authors.add(a1)
    entry2 = Entry(blog = blog1, headline = 'headline2')
    entry2.save()
    entry2.authors.add(a1)
    # entry3 = Entry(blog = blog2, headline = 'headline2')
    # entry3.save()
    # entry3.authors.add(a1)

    print('create1')



def all_entries():
    entries = Entry.objects.all()
    print(entries.query)
    print([e.blog.name for e in entries])
    return entries


def simple_filter():
    entries = Entry.objects.filter(headline='headline1')
    print(entries.query)
    print(['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])
    pass

def exclude():
    entries = Entry.objects.exclude(headline='none_headline1')
    print(entries.query)
    print(['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])

def complex():
    entries = Entry.objects.filter(headline='headline1', pk__gt=20)
    print(entries.query)
    print(1, entries[0].pk, ['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])


def comlex_filter_q():
    entries = Entry.objects.filter((Q(headline='headline1') | Q(headline='headline2')))
    print(entries.query)
    print(1, entries[0].pk, ['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])

def contains():
    '''
    contains, icontains
    startwith, istartwith
    endwith, iendwith
    in
    gt, gte, lt, lte
    range
    isnull
    '''
    entries = Entry.objects.filter(headline__contains='head')
    print(entries.query)
    print(entries[0].pk, ['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])


def relashinships():
    entries = Entry.objects.filter(blog__name='blog1')
    print(1, entries.query)
    print(entries[0].pk, ['{} {} {}'.format(e.blog.name, e.headline, e.authors.all()[0].name) for e in entries])

def reverse_relashionships():
    blogs = Blog.objects.filter(entry__authors__name='a1')
    print(2, blogs.query)
    print(blogs[0].pk, ['{} '.format(e.name) for e in blogs])

def distinct():
    objects = Blog.objects.all()
    entries = Entry.objects.all()

    blogs1 = Blog.objects.filter(entry__headline__contains='headline')
    print(['{} '.format(e.name) for e in blogs1])

    blogs2 = Blog.objects.filter(entry__headline__contains='headline').distinct()
    print(['{} '.format(e.name) for e in blogs2])

def isnull():
    objects = Blog.objects.all()
    for e in objects:
        entries = Entry.objects.filter(blog__name=e.name)
        print(444, entries)

    entries = Entry.objects.all()
    print(entries)
    blogs = Blog.objects.filter(entry__headline__isnull=True)
    blogs and print(blogs[0].name)

def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass

def show_tables():

    user_n = Author.objects.all().count()
    user_names = [e.name for e in Author.objects.all()]
    print(user_n, user_names)

    blog_n = Blog.objects.all().count()
    blog_titles = [e.name for e in Blog.objects.all()]
    print(blog_n, blog_titles)

    topic_n = Author.objects.all().count()
    topics_titles = [e.blog.name for e in Entry.objects.all()]
    print(topic_n, topics_titles)

