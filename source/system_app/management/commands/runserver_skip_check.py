from django.core.management.commands.runserver import Command as RunServer


class Command(RunServer):
    """
    NOTE: using this command will cannot detect error in coding

    NOTE: Put your application name must be on top in the INSTALLED_APPS list
        to override default django command
    reference: https://stackoverflow.com/a/41725866/7639845
    usage: python manage.py runserver_skip_check 0.0.0.0:8000
    """

    # pylint: disable=signature-differs
    def check(self, *args, **kwargs):
        self.stdout.write(
            self.style.WARNING(" ====== customized runserver command ==========\n")
        )
        self.stdout.write(
            self.style.WARNING(" ====== SKIPPING SYSTEM CHECKS! ===============\n")
        )

    def check_migrations(self, *args, **kwargs):
        self.stdout.write(
            self.style.WARNING(" ====== SKIPPING MIGRATION CHECKS! ============\n\n")
        )
