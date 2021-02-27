import pytest
from animal.models import Animal
import datetime
from consts.NamesConsts import MOPS, PEKINES, SHPIC
from consts.NamesConsts import DOCTOR, SDOCTOR, MDOCTOR


@pytest.mark.django_db
def test_animal_api_client(client):
    data = {
        'name': 'temp_animal_name',
        'relation_date': datetime.datetime.now(),
        'gender': True,
        'race': MOPS,
        'weight': 0
    }
    response = client.post(
        '/api/animal/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 403, response.data


@pytest.mark.django_db
def test_animal_api_valid_keys(admin_client):
    data = {
        'name': 'temp_animal_name',
        'relation_date': datetime.date.today(),
        'gender': True,
        'race': MOPS,
        'weight': 0
    }
    response = admin_client.post(
        '/api/animal/setview/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == 201, response.data
    assert response.data['name'] == 'temp_animal_name'
    assert response.data['gender'] is True
    assert response.data['race'] == MOPS
    assert response.data['relation_date'] == str(datetime.date.today())
    assert response.data['weight'] == 0
