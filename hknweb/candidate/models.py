from django.db import models
from django.contrib.auth.models import User

max_strlen = 255 # default max length for char fields
max_txtlen = 2000 # default max length for text fields


class OffChallenge(models.Model):
    """
    Model for an officer challenge submitted by a candidate.
    Each candidate who did the challenge must submit a separate request
    (May be changed in the future).
    Assumes the existence of two groups, "candidate" and "officer".
    """

    class Meta:
        verbose_name = "Officer challenge"

    id              = models.AutoField(primary_key=True)
    requester       = models.ForeignKey('auth.User', limit_choices_to={'groups__name': "candidate"},
                        on_delete=models.CASCADE, default=None, related_name='requester')
    officer         = models.ForeignKey('auth.User', limit_choices_to={'groups__name': "officer"},
                        on_delete=models.CASCADE, default=None, related_name='officer')
    name            = models.CharField(max_length=max_strlen, default='', verbose_name="title")
    description     = models.TextField(max_length=max_txtlen, blank=True, default='')
    # proof of completion is optional (if proof is a file, the candiate can send it to slack)
    proof           = models.TextField(max_length=max_txtlen, blank=True, default='')

    # TODO not sure if I need a field for partners

    def __str__(self):
        return self.name
