from __future__ import absolute_import, unicode_literals
from celery import task
import os
from master.loadcsv import convert_task
from master.models import *


@task()
def task_number_one():
    convert_task.clear()
    convert_task.ConvertToCsv()
