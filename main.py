# ----------------------------------------------------------------------
# Validation Functions
#
# These functions validate input values.
# In Python, functions prefixed with an underscore ("_") are private.
# Typically, unit tests should not be written for private functions.
# Don't write tests for them.
# Instead, write input validation tests for the calculation functions.
# ----------------------------------------------------------------------

def _validate_age_month(month):
    month = int(month)

    if month < 0 or month > 11:
        raise ValueError(f'Age month "{month}" must be between 0 and 11')

    return month


def _validate_age_year(year):
    year = int(year)

    if year < 65 or year > 67:
        raise ValueError(f'Age year "{year}" must be between 65 and 67')

    return year


def _validate_birth_month(month):
    month = int(month)

    if month < 1 or month > 12:
        raise ValueError(f'Birth month "{month}" must be between 1 and 12')

    return month


def _validate_birth_year(year):
    year = int(year)

    if year < 1900:
        raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
    elif year >= 3000:
        raise ValueError(f'Birth year "{year}" must be earlier than 3000')

    return year


# ----------------------------------------------------------------------
# Calculation Function: Retirement Age
#
# This function takes in a birth year and returns the retirement age.
# The retirement age is a (years, months) tuple.
#
# Notice the large number of if-else cases for birth years.
# Each one represents an equivalence class.
# Most conditions are single year values, but some represent ranges.
# There should be a test for each equivalence class and each boundary value.
# pytest.mark.parametrize can cover multiple inputs for the same test function.
#
# This function also validates inputs.
# Some inputs can be successfully parsed, but others will raise exceptions.
# There should be a test to cover each equivalence class of inputs, good and bad.
# pytest.raises makes testing exceptions easy.
# ----------------------------------------------------------------------

def calculate_retirement_age(birth_year):
    birth_year = _validate_birth_year(birth_year)

    if birth_year <= 1937:
        return 65, 0
    elif birth_year == 1938:
        return 65, 2
    elif birth_year == 1939:
        return 65, 4
    elif birth_year == 1940:
        return 65, 6
    elif birth_year == 1941:
        return 65, 8
    elif birth_year == 1942:
        return 65, 10
    elif 1943 <= birth_year <= 1954:
        return 66, 0
    elif birth_year == 1955:
        return 66, 2
    elif birth_year == 1956:
        return 66, 4
    elif birth_year == 1957:
        return 66, 6
    elif birth_year == 1958:
        return 66, 8
    elif birth_year == 1959:
        return 66, 10
    else:
        return 67, 0


# ----------------------------------------------------------------------
# Calculation Function: Retirement Date
#
# This function takes in four values to calculate the retirement date.
# The retirement date is a (year, month) tuple.
#
# There isn't a large if-else table in this function.
# Instead, there is a mathematical calculation.
# Unit tests should cover all ways the calculation can happen.
# Hint: look at the "if" condition.
#
# This function also validates all inputs.
# Again, there should be a test to cover good and bad inputs.
# There will be many more input validation tests for this function.
# ----------------------------------------------------------------------

def calculate_retirement_date(birth_year, birth_month, age_years, age_months):
    birth_year = _validate_birth_year(birth_year)
    birth_month = _validate_birth_month(birth_month)
    age_years = _validate_age_year(age_years)
    age_months = _validate_age_month(age_months)

    year = birth_year + age_years
    month = birth_month + age_months

    if month > 12:
        year += 1
        month -= 12

    return year, month
