from django.db import models
# for support of foreign characters
from django.utils.encoding import smart_unicode

# Create your models here.
# signup singular instance (below) -> signups for all instances (app)
class SignUp(models.Model):
    for_you = models.BooleanField(default=True, verbose_name="Is this purchase for you? If so, check this box.")
    # null = database ok blank
    # blank = form ok blank when submitted
    # charfield = max_length always required
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    # auto_now_true = timestamp when created
    # auto_now = timestamp for changes
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)