#!/usr/bin/env python
import os
import sys

import confy

dot_env = os.path.join(os.getcwd(), ".env")
if os.path.exists(dot_env):
    confy.read_environment_file()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apigw.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
