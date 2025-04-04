import pytest
from rest_framework import status
from django.urls import reverse
from company.models import Company


@pytest.mark.django_db
def test_create_company(api_client):
    """
    Тестуємо створення компанії через POST запит.
    """
    url = reverse("company:company-list")
    data = {
        "name": "Test Company",
        "address": "Test Address",
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == data["name"]
    assert response.data["address"] == data["address"]


@pytest.mark.django_db
def test_get_companies_list(api_client):
    """
    Тестуємо доступ до списку компаній через GET запит.
    """
    url = reverse("company:company-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_get_single_company(api_client):
    """
    Тестуємо отримання компанії по її id.
    """
    company = Company.objects.create(name="Test Company", address="Test Address")

    url = reverse("company:company-detail", kwargs={"pk": company.id})

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == company.name
    assert response.data["address"] == company.address


@pytest.mark.django_db
def test_update_company(api_client):
    """
    Тестуємо оновлення компанії через PUT запит.
    """
    company = Company.objects.create(name="Test Company", address="Test Address")

    url = reverse("company:company-detail", kwargs={"pk": company.id})
    data = {
        "name": "Updated Company",
        "address": "Updated Address",
    }

    response = api_client.put(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == data["name"]
    assert response.data["address"] == data["address"]


@pytest.mark.django_db
def test_delete_company(api_client):
    """
    Тестуємо видалення компанії через DELETE запит.
    """
    company = Company.objects.create(name="Test Company", address="Test Address")

    url = reverse("company:company-detail", kwargs={"pk": company.id})

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Company.objects.filter(id=company.id).exists()
