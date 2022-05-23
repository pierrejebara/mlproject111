from mlproject111.lib import odd,even
def test_make_sure():
    my_list=[1,2,3,4,5,6,7,8]
    assert isinstance(even(my_list),list)

def test_make_sure_odd():
    my_list=[1,2,3,4,5,6,7,8]
    assert type(odd(my_list)).__name__=="list"
