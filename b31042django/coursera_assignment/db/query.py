from datetime import datetime
from unicodedata import name

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    # python manage.py migrate
    # python manage.py makemigrations

    for e in User.objects.all():
        e.delete()
        pass

    u1 = User(first_name = 'u1', last_name = 'u1')
    u2 = User(first_name = 'u2', last_name = 'u2')
    u3 = User(first_name = 'u3', last_name = 'u3')
    u1.save()
    u2.save()
    u3.save()
    blog1 = Blog(title='blog1', author=u1)
    blog2 = Blog(title='blog2', author=u1)
    blog1.save()
    blog2.save()
    blog1.subscribers.add(u1)
    blog1.subscribers.add(u2)
    blog2.subscribers.add(u2)
    topic1 = Topic(title="topic1", blog=blog1, author=u1)
    topic2 = Topic(title="topic2_content", blog=blog1, author=u3)
    # created='2017-01-01'
    topic1.save()
    topic2.save()
    topic1.likes.add(u1, u2, u3)
    


def edit_all():
    for e in User.objects.all():
        e.first_name = 'uu1'
        e.save()
    user_n = User.objects.all().count()
    user_names = [e.first_name for e in User.objects.all()]
    print(user_n, user_names)

    blog_n = Blog.objects.all().count()
    blog_titles = [e.title for e in Blog.objects.all()]
    print(blog_n, blog_titles)

    topic_n = User.objects.all().count()
    topics_titles = [e.title for e in Topic.objects.all()]
    print(topic_n, topics_titles)

def edit_u1_u2():

    for e in User.objects.all():
        if e.first_name == 'u1' or e.first_name == 'u2':
            e.first_name = 'uu1'
            e.save()



def delete_u1():

    users = User.objects.filter(first_name='u1')
    if len(users) > 0:
        users[0].delete()


def unsubscribe_u2_from_blogs():

    blogs = Blog.objects.filter(title="blog1")

    if len(blogs) > 0:
        subscribers = blogs[0].subscribers.all()
        for e in subscribers:
            if e.first_name == 'u2':
                blogs[0].subscribers.remove(e)



def get_topic_created_grated():
    pass


def get_topic_title_ended():

    topics = Topic.objects.all()
    
    print(3333, len(topics))


    user_n = User.objects.all().count()
    user_names = [e.first_name for e in User.objects.all()]
    print(user_n, user_names)

    blog_n = Blog.objects.all().count()
    blog_titles = [e.title for e in Blog.objects.all()]
    print(blog_n, blog_titles)

    topic_n = User.objects.all().count()
    topics_titles = [e.title for e in Topic.objects.all()]
    print(topic_n, topics_titles)



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

if __name__ == "__main__":
    create()
    print(222)