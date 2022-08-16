from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, int_list_validator
from django.utils.encoding import smart_str

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, default=False)
    smart_str(first_name, encoding='utf-8',
              strings_only=False, errors='strict')

    last_name = models.CharField(max_length=100, default=False)
    smart_str(last_name, encoding='utf-8',
              strings_only=False, errors='strict')

    id_nummber = models.CharField(

        verbose_name="id_nummber", max_length=15,
        validators=[int_list_validator(sep=''), MinLengthValidator(14)],
    )

    smart_str(id_nummber, encoding='utf-8',
              strings_only=False, errors='strict')

    phone_nummber = models.CharField(

        verbose_name="phone_nummber", max_length=11,
        validators=[int_list_validator(sep=''), MinLengthValidator(11)],
    )

    def __unicode__(self):
        return self.user.clean
