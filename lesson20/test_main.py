from l20 import add
def test_add_positive_num():
    assert  add(2, 3) == 5

def test_add_neg_num():
    assert add(-1,4) == -5

def test_add_mixed_num():
    assert add(-2, 5) == 3