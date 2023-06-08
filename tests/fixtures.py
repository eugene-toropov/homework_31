import pytest


@pytest.fixture
@pytest.mark.django_db
def acces_token(client, django_user_model):
    username = 'test'
    password = 'qwerty'
    django_user_model.objects.create(username=username, password=password)
    response = client.post('/user/token/', data={'username': username, 'password': password})
    return response.data.get('access')
