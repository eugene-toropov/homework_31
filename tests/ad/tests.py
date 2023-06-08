import pytest
from rest_framework import status

from ads.serializers import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(5)
    response = client.get('/ad/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'count': 5,
        'next': None,
        'previous': None,
        'results': AdListSerializer(ad_list, many=True).data
    }


@pytest.mark.django_db
def test_ad_retrieve(client, access_token):
    ad = AdFactory.create()
    response = client.get(f'/ad/{ad.pk}', HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == AdDetailSerializer(ad).data


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        'author': user.username,
        'category': category.name,
        'name': 'asdsadsadsadasd',
        'price': 300
    }

    expected_data = {
        'id': 1,
        'category': category.name,
        'author': user.username,
        'is_published': False,
        'name': 'asdsadsadsadasd',
        'price': 300,
        'description': None,
        'image': None
    }

    response = client.post('/ad/', data=data, HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
