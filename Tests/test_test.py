import allure


@allure.step
def test_test_111():
    assert 1+1 == 2
    print("1234")

@allure.step
def test_test_222():
    assert 1+1 == 2
    print("1234")
