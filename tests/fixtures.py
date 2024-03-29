import pytest
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
import django
django.setup()

@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'user'
    password = 'password'

    django_user_model.objects.create_user(
        username=username, password=password
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data['access']
