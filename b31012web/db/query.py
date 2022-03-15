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

    print('create')



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


    print(4444)
    pass




def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


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
