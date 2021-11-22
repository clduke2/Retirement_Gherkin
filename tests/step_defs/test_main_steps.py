import pytest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from main import calculate_retirement_age


@pytest.mark.parametrize(
    ['year', 'years', 'months'],
    [(1900, 65, 0),
     (1937, 65, 0),
     (1938, 65, 2),
     (1939, 65, 4),
     (1940, 65, 6),
     (1941, 65, 8),
     (1942, 65, 10),
     (1943, 66, 0),
     (1954, 66, 0),
     (1955, 66, 2),
     (1956, 66, 4),
     (1957, 66, 6),
     (1958, 66, 8),
     (1959, 66, 10),
     (1960, 67, 0),
     (2999, 67, 0)]
)
@scenario('../features/main.feature', 'Calculate the age I retire')
def test_add(year, years, months):
    pass


@given('I run the program')
@when('I enter my birth year')
@then('using the "<year>" given, the program calculates how old I am in "<years>" and "<months>" when I can retire.')
def calc_retire_age(year, years, months):
    assert calculate_retirement_age(year) == (years, months)
