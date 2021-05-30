#!/usr/bin/env python
# pylint: disable=import-outside-toplevel
"""Django's command-line utility for administrative tasks."""
import os
import sys


def initialize_debugger(sys_args):
    # Reference: https://stackoverflow.com/a/62944426/7639845
    # optionally check to see what env you're running in, you probably only want this for
    # local development, for example: if os.getenv("MY_ENV") == "dev":

    # RUN_MAIN envvar is set by the reloader to indicate that this is the
    # actual thread running Django. This code is in the parent process and
    # initializes the debugger
    if not os.getenv("RUN_MAIN") and sys_args[1] == "runserver":
        try:
            import debugpy

            debugpy.listen(("0.0.0.0", 5678))
            sys.stdout.write("=======> Start the VS Code debugger now, waiting...\n")
        # pylint: disable=bare-except
        except Exception as e:
            sys.stdout.write("=======> Start the VS Code debugger FAILED %s \n" % e)
        # debugpy.wait_for_client()
        # sys.stdout.write("Debugger attached, starting server...\n")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    allow_run_debug_env = ["dev", "int", "local"]
    if (
        os.getenv("BUILD_ENV") in allow_run_debug_env
        and os.getenv("WORKING_ENV") in allow_run_debug_env
    ):
        initialize_debugger(sys.argv)
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
