import requests
import pytest
from config import *
from src.enums.global_enums import Error

def test_get_list():
    req = requests.get(url=url_get_list, timeout=1)
    r = req.json()
    assert req.status_code == 200, Error.status_code
    assert (r['data'][0]['first_name']) == first_name, Error.mismatch
    print(r['data'][0]['first_name'])
    return r

def test_create_user():
    req = requests.post(url=url_create_user, data=params_create_user, timeout=1)
    assert req.status_code == 201, Error.mismatch
    r = req.json()
    assert (r['name']) == name
    print(r['name'])
    return r

def test_update_user():
    req = requests.put(url=url_update_user,data=params_update_user, timeout=1)
    assert req.status_code == 200, error
    r = req.json()
    print(r['name'])
    assert (r['name']) == name_update
    return r

test_create_user()
test_get_list()
test_update_user()