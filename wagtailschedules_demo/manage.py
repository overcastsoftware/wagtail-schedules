#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "wagtailschedules_demo.settings.dev")

    # start new section
    from django.conf import settings

    if settings.DEBUG:
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            import debugpy
            debugpy.listen(("0.0.0.0", 3000))
            print('Attached!')
    # end new section

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
