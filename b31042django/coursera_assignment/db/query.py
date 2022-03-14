from datetime import datetime
from django.utils import timezone
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
    topic1.save()
    date_2017 = datetime(2017, 1, 1, tzinfo=timezone.utc)
    topic2 = Topic(title="topic2_content", blog=blog1, author=u3, created=date_2017)
    topic2.save()
    topic1.likes.add(u1, u2, u3)


def edit_all():
    for e in User.objects.all():
        e.first_name = 'uu1'
        e.save()

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
    topics = None
    date_2018 = datetime(2018, 1, 1, tzinfo=timezone.utc)
    topics = Topic.objects.filter(created__gt=date_2018)
    print(1)
    return topics

def get_topic_title_ended():
    topics = Topic.objects.order_by('-pk')[:2]
    return topics


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    count_blog = Blog.objects.count()
    qn = 'qn'
    q = Blog.objects.aggregate(qn=Count('topic'))
    count_topic = q[qn]
    avg_topic_count = count_topic // count_blog
    return avg_topic_count



def get_blog_that_have_more_than_one_topic():
    count = Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1).count()
    return count


def get_topic_by_u1():

    user = User.objects.get(first_name='u1')
    blogs = Topic.objects.filter(author=user)
    return blogs


def get_user_that_dont_have_blog():
    blogs = None
    blogs = Blog.objects.all()
    for e in blogs:
        print(e.subscribers.all(), len(e.subscribers.all()))
    blogs = Blog.objects.select_related('author')
    print(3333, blogs)
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass

def show_users_all():
    user_n = User.objects.all().count()
    user_names = [e.first_name for e in User.objects.all()]
    print(user_n, user_names)

    blog_n = Blog.objects.all().count()
    blog_titles = [e.title for e in Blog.objects.all()]
    print(blog_n, blog_titles)

    topic_n = User.objects.all().count()
    topics_titles = [e.title for e in Topic.objects.all()]
    print(topic_n, topics_titles)

if __name__ == "__main__":
    create()
    print(2222)