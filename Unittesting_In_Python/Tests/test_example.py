from App.First_Pytest import add,sub,mul,div,discount_season
import pytest


@pytest.mark.skipif(discount_season(),reason='')
def test_add():
    assert add(10,20) == 30
    
def test_sub():
    assert sub(20,10) == 10
    
def test_mul():
    assert mul(10,20) == 200
 
@pytest.mark.skip("Skipping")   
def test_div():
    assert div(20,20) == 1
    
    with pytest.raises(ValueError):
        div(4,0)