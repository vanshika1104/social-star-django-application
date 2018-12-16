from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    related_name='images_created')
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, blank = True)
    url = models.URLField(max_length=600)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
