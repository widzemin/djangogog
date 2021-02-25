import pytest
from animal.models import Animal
from doctor.models import Doctor
from order.models import Order
import datetime
from consts.NamesConsts import MOPS, PEKINES, SHPIC 
from consts.NamesConsts import DOCTOR, SDOCTOR, MDOCTOR

@pytest.mark.django_db
def test_with_client(client):
    response = client.get('/order/dog/')
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
    assert order_past.is_active() == False

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
    assert order_future.is_active() == True

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
    assert order_now.is_active() == True 



