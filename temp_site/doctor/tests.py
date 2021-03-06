import pytest
from doctor.models import Doctor
import datetime
from consts.NamesConsts import MOPS, PEKINES, SHPIC
from consts.NamesConsts import DOCTOR, SDOCTOR, MDOCTOR


@pytest.mark.django_db
def test_doctor_api_client(client):
    data = {
        'name': 'temp_doctor_name',
        'grade': DOCTOR,
        'min_animal_weight': 0,
        'max_animal_weight': 0
    }
    response = client.post(
        '/api/doctor/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 403, response.data


@pytest.mark.django_db
def test_doctor_api_valid_keys(admin_client):
    data = {
        'name': 'temp_doctor_name',
        'grade': DOCTOR,
        'min_animal_weight': 0,
        'max_animal_weight': 0
    }
    response = admin_client.post(
        '/api/doctor/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 201, response.data
    assert response.data['name'] == 'temp_doctor_name'
    assert response.data['grade'] == DOCTOR
    assert response.data['min_animal_weight'] == 0
    assert response.data['max_animal_weight'] == 0
