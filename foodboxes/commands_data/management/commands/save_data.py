from django.core.management.base import BaseCommand
import requests
from termcolor import colored

from users.models import User
from items.models import Item
from reviews.models import Review


def term_text(data, object_d):
    if data[1] is True:
        print(colored(data[1], color='green'), object_d, data[0])
    else:
        print(colored(data[1], color='red'), object_d, data[0])


def create_data_users():
    response = requests.get("https://raw.githubusercontent.com/"
                            "stepik-a-w/drf-project-boxes/"
                            "master/recipients.json").json()
    for item in response:
        data_users = User.objects.get_or_create(
            id=item['id'],
            defaults={
                "email": item['email'],
                "username": item['email'].split('@')[0],
                "password": item['password'],
                "first_name": item['info']['name'],
                "last_name": item['info']['surname'],
                "middle_name": item['info']['patronymic'],
                "phone": item['contacts']['phoneNumber'],
                "address": item['city_kladr'],
            }
        )
        term_text(data_users, 'object User:')


def create_data_items():
    response = requests.get('https://stepik.org/media/'
                            'attachments/course/73594/foodboxes.json').json()
    for item in response:
        data_items = Item.objects.get_or_create(
            id=item['id'],
            defaults={
                "title": item['title'],
                "description": item['description'],
                "image": item['image'],
                "weight": item['weight_grams'],
                "price": item['price'],
            }
        )
        term_text(data_items, 'object Item:')


def create_data_reviews():
    response = requests.get('https://raw.githubusercontent.com/stepik-a-w'
                            '/drf-project-boxes/master/reviews.json').json()
    for item in response:
        reviews_data = Review.objects.get_or_create(
            id=item['id'],
            defaults={
                "author": User.objects.get(id=item['id']),
                "text": item['content'],
                "created_at": item['created_at'],
                "published_at": item['published_at'],
                "status": item['status'],
            }
        )
        term_text(reviews_data, 'object Review:')


class Command(BaseCommand):

    def handle(self, *args, **options):
        if options['full']:
            create_data_items()
            create_data_users()
            create_data_reviews()

        elif options['items']:
            create_data_items()

        elif options['users']:
            create_data_users()

        elif options['reviews']:
            create_data_reviews()

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--full',
            action='store_true',
            default=False,
            help='Создать и обновить все записи во всех базах данных'
        )
        parser.add_argument(
            '--items',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных items'
        )
        parser.add_argument(
            '--users',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных users'
        )
        parser.add_argument(
            '--reviews',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных reviews'
        )
