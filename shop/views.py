from django.shortcuts import render
from .models import Item


def item_list(request):
    # 데이터베이스로부터 모든 Item내역을 가져올려고 한다.
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
    })
