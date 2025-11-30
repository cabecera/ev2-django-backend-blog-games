import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.shortcuts import render

def product_list_get(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    items = Product.objects.all()
    data = [i.to_dict() for i in items]
    return JsonResponse(data, safe=False)


@csrf_exempt
def product_create_post(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        payload = json.loads(request.body.decode('utf-8'))

        p = Product.objects.create(
            name=payload['name'],
            description=payload.get('description', ''),
            price=payload.get('price', 0),
            stock=payload.get('stock', 0),
            available=payload.get('available', True)
        )

        return JsonResponse(p.to_dict(), status=201)

    except (KeyError, ValueError, json.JSONDecodeError) as e:
        return JsonResponse({'error': str(e)}, status=400)



def list_products_view(request):
    return render(request, 'api_app/list_products.html')