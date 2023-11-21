"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from movies.tasks import update_now_playing, update_upcoming

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

# 서버 시작 시 실행
# update_now_playing()
# update_upcoming()

# 매일 자정에 실행
# scheduler.add_job(update_movie_rating_avg, 'cron', hour=0, id='my_job_id', replace_existing=True)
scheduler.add_job(update_now_playing, 'cron', hour=0, id='update_now_playing', replace_existing=True)
scheduler.add_job(update_upcoming, 'cron', hour=0, id='update_upcoming', replace_existing=True)
# scheduler.add_job(update_now_playing, 'interval', seconds=30, id='update_now_playing', replace_existing=True)

# scheduler.add_job(update_upcoming, 'interval', seconds=30, id='update_upcoming', replace_existing=True)
# scheduler.start()