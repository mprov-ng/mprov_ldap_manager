# Defines the DB Models that will be used by this Django App or section of mProv
from django.db import models
import sh, os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save


