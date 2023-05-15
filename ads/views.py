import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'ok'}, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request):
        all_cat = Category.objects.all()
        return JsonResponse([cat.serialize() for cat in all_cat], status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_cat = Category.objects.create(**data)
        return JsonResponse(new_cat.serialize())


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):
    def get(self, request):
        all_ads = Ad.objects.all()
        return JsonResponse([ad.serialize() for ad in all_ads], status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)
        return JsonResponse(new_ad.serialize())


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_object().serialize(), safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_object().serialize(), safe=False)
