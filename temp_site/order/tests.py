import pytest
from animal.models import Animal
from doctor.models import Doctor
from order.models import Order
import datetime
from consts.NamesConsts import (
    MOPS, PEKINES, SHPIC, RACES,
    DOCTOR, SDOCTOR, MDOCTOR, GRADES,
    DOG, BITCH, BOTH, GENDERS
)


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
        race=MOPS,
        weight=3
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        grade=DOCTOR,
        min_animal_weight=1,
        max_animal_weight=10
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


@pytest.mark.django_db
def test_order_api_invalid_weight(admin_client):
    temp_animal = Animal.objects.create(
        name='temp_animal_name',
        relation_date=datetime.datetime.now(),
        gender=True,
        race=MOPS,
        weight=5
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        grade=DOCTOR,
        min_animal_weight=3,
        max_animal_weight=4
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
    assert response.status_code == 400, response.data


@pytest.mark.django_db
def test_order_api_valid_weight(admin_client):
    temp_animal = Animal.objects.create(
        name='temp_animal_name',
        relation_date=datetime.datetime.now(),
        gender=True,
        race=MOPS,
        weight=5
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        grade=DOCTOR,
        min_animal_weight=1,
        max_animal_weight=10
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


@pytest.mark.django_db
def test_order_api_invalid_doctor_race(admin_client):
    temp_animal = Animal.objects.create(
        name='temp_animal_name',
        race=SHPIC
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_race=[MOPS, PEKINES]
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
    assert response.status_code == 400, response.data


@pytest.mark.django_db
def test_order_api_valid_doctor_race(admin_client):
    temp_animal = Animal.objects.create(
        name='temp_animal_name',
        race=MOPS
    )
    temp_doctor = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_race=[MOPS, SHPIC, PEKINES]
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
    assert response.data['animal'] == temp_animal.id
    assert response.data['doctor'] == temp_doctor.id


@pytest.mark.django_db
def test_order_api_invalid_doctor_gender(admin_client):
    temp_animal_1 = Animal.objects.create(
        name='temp_animal_name',
        gender=True
    )
    temp_doctor_1 = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_gender=BITCH
    )
    temp_animal_2 = Animal.objects.create(
        name='temp_animal_name',
        gender=False
    )
    temp_doctor_2 = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_gender=DOG
    )
    data_1 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_1.id,
        'animal': temp_animal_1.id
    }
    data_2 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_2.id,
        'animal': temp_animal_2.id
    }
    response_1 = admin_client.post(
        '/api/order/setview/',
        data=data_1,
        content_type='application/json'
    )
    response_2 = admin_client.post(
        '/api/order/setview/',
        data=data_2,
        content_type='application/json'
    )
    assert response_1.status_code == 400, response_1.data
    assert response_2.status_code == 400, response_2.data


@pytest.mark.django_db
def test_order_api_valid_doctor_race(admin_client):
    temp_animal_1 = Animal.objects.create(
        name='temp_animal_name',
        gender=True
    )
    temp_animal_2 = Animal.objects.create(
        name='temp_animal_name',
        gender=False
    )
    temp_doctor_1 = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_gender=DOG
    )
    temp_doctor_2 = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_gender=BITCH
    )
    temp_doctor_3 = Doctor.objects.create(
        name='temp_doctor_name',
        available_animal_gender=BOTH
    )
    data_1 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_1.id,
        'animal': temp_animal_1.id
    }
    data_2 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_2.id,
        'animal': temp_animal_2.id
    }
    data_3 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_3.id,
        'animal': temp_animal_1.id
    }
    data_4 = {
        'reason': 'temp_reason',
        'date': datetime.datetime.now(),
        'doctor': temp_doctor_3.id,
        'animal': temp_animal_2.id
    }
    response_1 = admin_client.post(
        '/api/order/setview/',
        data=data_1,
        content_type='application/json'
    )
    response_2 = admin_client.post(
        '/api/order/setview/',
        data=data_2,
        content_type='application/json'
    )
    response_3 = admin_client.post(
        '/api/order/setview/',
        data=data_3,
        content_type='application/json'
    )
    response_4 = admin_client.post(
        '/api/order/setview/',
        data=data_4,
        content_type='application/json'
    )
    assert response_1.status_code == 201, response_1.data
    assert response_2.status_code == 201, response_2.data
    assert response_3.status_code == 201, response_2.data
    assert response_4.status_code == 201, response_2.data
    assert response_1.data['animal'] == temp_animal_1.id
    assert response_1.data['doctor'] == temp_doctor_1.id
    assert response_2.data['animal'] == temp_animal_2.id
    assert response_2.data['doctor'] == temp_doctor_2.id
    assert response_3.data['animal'] == temp_animal_1.id
    assert response_3.data['doctor'] == temp_doctor_3.id
    assert response_4.data['animal'] == temp_animal_2.id
    assert response_4.data['doctor'] == temp_doctor_3.id
