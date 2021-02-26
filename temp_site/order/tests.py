import pytest
from animal.models import Animal
from doctor.models import Doctor
from order.models import Order
import datetime
from consts.NamesConsts import MOPS, PEKINES, SHPIC
from consts.NamesConsts import DOCTOR, SDOCTOR, MDOCTOR


@pytest.mark.django_db
def test_with_client_1(client):
    response = client.get('/order/dog/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_with_client_2(client):
    response = client.get('/order/bitch/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_with_client_3(client):
    response = client.get('/order/sort/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_past_valid():
    date_past = datetime.datetime.now() - datetime.timedelta(
        weeks=40,
        days=50,
        seconds=10
    )
    temp_animal = Animal(
        name='temp_animal_name',
        relation_date=date_past,
        gender=True,
        race=MOPS
    )
    temp_doctor = Doctor(
        name='temp_doctor_name',
        grade=DOCTOR
    )
    order_past = Order(
        reason='temp_reason',
        date=date_past,
        doctor=temp_doctor,
        animal=temp_animal
    )
    assert order_past.is_active() is False


@pytest.mark.django_db
def test_order_future_valid():
    date_future = datetime.datetime.now() + datetime.timedelta(
        weeks=40,
        days=50,
        seconds=10
    )
    temp_animal = Animal(
        name='temp_animal_name',
        relation_date=date_future,
        gender=True,
        race=MOPS
    )
    temp_doctor = Doctor(
        name='temp_doctor_name',
        grade=DOCTOR
    )
    order_future = Order(
        reason='temp_reason',
        date=date_future,
        doctor=temp_doctor,
        animal=temp_animal
    )
    assert order_future.is_active() is True


@pytest.mark.django_db
def test_order_now_valid():
    date_now = datetime.datetime.now() + datetime.timedelta(
        seconds=1
    )
    temp_animal = Animal(
        name='temp_animal_name',
        relation_date=date_now,
        gender=True,
        race=MOPS
    )
    temp_doctor = Doctor(
        name='temp_doctor_name',
        grade=DOCTOR
    )
    order_now = Order(
        reason='temp_reason',
        date=date_now,
        doctor=temp_doctor,
        animal=temp_animal
    )
    assert order_now.is_active() is True


@pytest.mark.django_db
def test_order_api_none_keys(admin_client):
    data = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': None,
        'animal': None
    }
    response = admin_client.post(
        '/api/order/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 400
    assert str(response.data['doctor'][0]) == 'This field may not be null.'
    assert str(response.data['animal'][0]) == 'This field may not be null.'


@pytest.mark.django_db
def test_order_api_valid_keys(admin_client):
    temp_animal = Animal.objects.create(
        name='temp_animal_name',
        relation_date=datetime.datetime.now(),
        gender=True,
        race=MOPS
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        grade=DOCTOR
    )
    data = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor.id,
        'animal': temp_animal.id
    }
    response = admin_client.post(
        '/api/order/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 201, response.data
    assert response.data['doctor'] == temp_doctor.id
    assert response.data['animal'] == temp_animal.id
