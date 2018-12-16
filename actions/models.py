from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_constraint=True)
    verb = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    target_ct = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True)
    target = GenericForeignKey('target_ct','target_id')
    
    class Meta:
        ordering = ('-created',)
