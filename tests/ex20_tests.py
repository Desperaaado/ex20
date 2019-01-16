from nose.tools import *
from ex20.ex20 import *

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    states = BSTree()
    states.set(3, 'OR')
    states.set(8, 'FL')
    states.set(44, 'CA')
    states.set(0, 'NY')
    states.set(44, 'CA44')
    states.set(9, 'MI')
    states.set(30, 'OR')
    states.set(80, 'FL')
    # states.set(404, 'CA')
    # states.set(401, 'NY')
    # states.set(404, 'CA44')
    # states.set(911, 'MI')
    assert_equal(states.get(44), 'CA44')
    states.show_list()
    assert_equal(states.do_delete(44), 'CA44')
    # states.do_delete(3)
    states.show_list()