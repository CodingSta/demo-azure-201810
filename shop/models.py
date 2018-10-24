from django.core.validators import MinLengthValidator
from django import forms
from django.db import models


# def min_length_3(value):
#     if len(value) < 3:
#         raise forms.ValidationError('3글자 이상 !!!')

min_length_3 = MinLengthValidator(3)


# TODO: Item.name 필드에 최대길이 10자 제한



class Item(models.Model):
    name = models.CharField(max_length=100,
                            validators=[min_length_3])
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return '<{}> {}'.format(self.id, self.name)
        return f'<{self.pk}> {self.name}'
