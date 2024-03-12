from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Order, Reservation

#
# def catalog_view(request):
#     # Вывод всех продуктов из каталога
#     products = Product.objects.all()
#     return render(request, 'catalog.html', {'products': products})
#
#
# def product_detail_view(request, product_id):
#     # Просмотр деталей конкретного продукта
#     product = Product.objects.get(id=product_id)
#     return render(request, 'product_detail.html', {'product': product})
#
#
# def make_order(request):
#     if request.method == 'POST':
#         # Обработка заказа
#         product_id = request.POST.get('product_id')
#         pickup_point = request.POST.get('pickup_point')
#         receive_date = request.POST.get('receive_date')
#         promo_code = request.POST.get('promo_code')
#         payment_method = request.POST.get('payment_method')
#         email = request.POST.get('email')
#
#         product = Product.objects.get(id=product_id)
#         order = Order.objects.create(product=product, pickup_point=pickup_point, receive_date=receive_date,
#                                      promo_code=promo_code, payment_method=payment_method, email=email)
#         order.save()
#
#         return render(request, 'order_confirmation.html', {'order': order})
#     else:
#         return render(request, 'make_order.html')
#
#
# def make_reservation(request):
#     if request.method == 'POST':
#         # Обработка бронирования
#         product_id = request.POST.get('product_id')
#         reservation_date = request.POST.get('reservation_date')
#
#         product = Product.objects.get(id=product_id)
#         reservation = Reservation.objects.create(product=product, reservation_date=reservation_date)
#         reservation.save()
#
#         return render(request, 'reservation_confirmation.html', {'reservation': reservation})
#     else:
#         return render(request, 'make_reservation.html')

def home_view(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html')

    if request.method == 'POST':
        # Обработка нажатия кнопки "Перейти в каталог"
        return HttpResponseRedirect(reverse('catalog'))