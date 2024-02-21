from employee import Employee
import pytest

def test_give_default_raise():
    employee = Employee("Jarryd", "Deane", 100_000)
    assert employee.firstname == "Jarryd"
    assert employee.lastname == "Deane"
    assert employee.annualSalary == 100_000

    employee.give_raise()
    assert employee.annualSalary == 105_000

def test_give_custom_raise():
    employee = Employee("Jarryd", "Deane", 100_000)
    assert employee.firstname == "Jarryd"
    assert employee.lastname == "Deane"
    assert employee.annualSalary == 100_000

    employee.give_raise(10_000)
    assert employee.annualSalary == 110_000

@pytest.fixture
def employee():
    employee = Employee("Jarryd", "Deane", 200_000)
    return employee

def test_using_fixture_give_default_raise(employee):
    assert employee.firstname == "Jarryd"
    assert employee.lastname == "Deane"
    assert employee.annualSalary == 200_000

    employee.give_raise()
    assert employee.annualSalary == 205_000

def test_using_fixture_give_custom_raise(employee):
    assert employee.firstname == "Jarryd"
    assert employee.lastname == "Deane"
    assert employee.annualSalary == 200_000

    employee.give_raise(10_000)
    assert employee.annualSalary == 210_000