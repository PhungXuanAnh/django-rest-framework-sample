from django.core.management.base import BaseCommand, CommandError
from music.models import Musician


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("emails", nargs="+", type=str)

        # Named (optional) arguments
        # refer here for this type of argument: https://docs.python.org/3/library/argparse.html#module-argparse
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete these musicans',
        )

    def handle(self, *args, **options):
        for email in options["emails"]:
            try:
                musican = Musician.objects.get(email=email)
                self.stdout.write(
                    self.style.SUCCESS('Musical with email "%s" is %s' % (email, musican))
                )
            except Musician.DoesNotExist:
                raise CommandError('Musical with email "%s" does not exist' % email)

        self.stdout.write(
            self.style.SUCCESS("option: --delete = %s" % options['delete'])
        )
        self.stdout.write(
            self.style.SUCCESS("=========== finished command =======================")
        )
