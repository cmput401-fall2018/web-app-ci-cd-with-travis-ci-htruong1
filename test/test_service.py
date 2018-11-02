from service import Service
from unittest.mock import patch

def test_abs_plus():
    serviceTest = Service()
    testValue = serviceTest.abs_plus(-5)
    assert(testValue == 6)

    testValue = serviceTest.abs_plus(0)
    assert(testValue == 1)

@patch.object(Service, "bad_random")
def test_divide(bad_randomStub):
    bad_randomStub.return_value = 8

    serviceTest = Service()
    x = serviceTest.divide(2)
    assert(x == 4)

    

@patch.object(Service, "bad_random")
def test_complicated_function(bad_randomStub):
    bad_randomStub.return_value = 7

    serviceTest = Service()
    div= serviceTest.complicated_function(5)
    assert(div == (7/5,1))
