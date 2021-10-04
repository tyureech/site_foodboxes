from django.core.management.base import BaseCommand

from users.models import User
from items.models import Item
from reviews.models import Review


class Command(BaseCommand):

    def handle(self, *args, **options):
        if options['full']:
            Review.objects.all().delete()
            Item.objects.all().delete()
            User.objects.all().delete()
            print("Items, Reviews, Users deleted!")

        elif options['items']:
            Item.objects.all().delete()
            print("Items deleted!")

        elif options['users']:
            User.objects.all().delete()
            print("Users deleted!")

        elif options['reviews']:
            Review.objects.all().delete()
            print("Reviews deleted!")

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--full',
            action='store_true',
            default=False,
            help='Удалить все записи во всех базах данных'
        )
        parser.add_argument(
            '--items',
            action='store_true',
            default=False,
            help='Удалить записи в базе данных items'
        )
        parser.add_argument(
            '--users',
            action='store_true',
            default=False,
            help='Удалить записи в базе данных users'
        )
        parser.add_argument(
            '--reviews',
            action='store_true',
            default=False,
            help='Удалить записи в базе данных reviews'
        )
