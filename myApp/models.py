from django.db import models
from accounts.models import Account
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    post_type_choices = [('FAMILY', 'FAMILY'),
                         ('WORK', 'WORK'),
                         ('PERSONAL', 'PERSONAL')
                         ]
    post_type = models.CharField(max_length=20, choices=post_type_choices, default='PERSONAL')
    created_date = models.DateTimeField(verbose_name='created_date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(verbose_name='modified_date', auto_now=True, null=True, blank=True)
    completion_status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('myApp:mytodo_list')

    def __str__(self):
        return self.title
