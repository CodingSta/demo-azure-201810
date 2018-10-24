from django.core.validators import MinLengthValidator
from django import forms
from django.db import models


# def min_length_3(value):
#     if len(value) < 3:
#         raise forms.ValidationError('3글자 이상 !!!')

min_length_3 = MinLengthValidator(3)


# TODO: Item.name 필드에 최대길이 10자 제한
def max_length_validator(max_length):
    def fn(value):
        if len(value) > max_length:
            raise forms.ValidationError('최대 10자 !!!')
    return fn

fn_10 = max_length_validator(10)
fn_20 = max_length_validator(20)


class Item(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return '<{}> {}'.format(self.id, self.name)
        return f'<{self.pk}> {self.name}'
