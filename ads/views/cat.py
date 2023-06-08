from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


def root(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'ok'}, status=200, safe=False)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
