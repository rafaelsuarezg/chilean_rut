"""
Module to validate, format, clean and get verification digit for Chileans RUT numbers
"""
import re
from itertools import cycle


def __raise_error(rut, value_error: str):
    raise ValueError(f'{rut}: {value_error}')


def __is_rut_perfectly_formatted(rut: str) -> bool:
    """
    Validates if Chilean RUT Number is perfectly formatted

    Args:
        rut (str):  A Chilean RUT Number. For example 5.126.663-3

    Returns:
        bool: True when Chilean RUT number (rut:str) is perfectly formatted
        ** Only validates the format not if the RUT is valid or not
    """
    perfect_rut_regex = r"^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$"
    return re.match(perfect_rut_regex, rut) is not None


def __is_rut_format(rut: str) -> bool:
    """
    Validates if given string have Chilean RUT Number format

    Args:
        rut (str):  A Chilean RUT Number. For example 5.126.663-3  | 5126663-3 | 51266633

    Returns:
        bool: True when given string is a Chilean RUT number format
        ** Only validates the format not if the RUT is valid or not
    """
    format_rut_regex = r"^0*(\d{1,3}(\.?\d{3})*)-?([\dkK])$"
    return re.match(format_rut_regex, str(rut)) is not None


def __is_only_numbers(rut: str) -> bool:
    """
    Validates if a given string contains only numbers

    Args:
        rut (str):  A Chilean RUT Number without verification digit.
        For example 5126663

    Returns:
        bool:  True when given string contains only numbers
    """
    only_numbers_regex = r"^\d+$"
    return rut and re.match(only_numbers_regex, rut)


def __clean_rut_string(rut: str) -> str:
    if rut is not None:
        rut = rut.lower().strip()
        return re.sub(r'^0+|[^0-9kK]+', '', rut)
    return ''


def is_valid(rut: str = None) -> bool:
    """
    Checks if a Chilean RUT number is valid or not

    Args:
        rut (str):  A Chilean RUT Number. Examples 5126663-3 or 5.126.663-3 or 512666633
        Default None.

    Returns:
        bool: True when Chilean RUT number (rut:str) is valid
    """

    # if RUT starts with 0 return false
    if re.match(r'^0+', str(rut)):
        return False

    if not __is_rut_format(rut):
        return False

    rut_digits = __clean_rut_string(rut)

    return get_verification_digit(rut_digits[:-1]) == rut_digits[-1]


def get_verification_digit(rut: str = None) -> str:
    """
    Calculates the RUT verification number or letter

    Args:
        rut (str):  A Chilean RUT number without verification digit. Example 5126663
                    No dots, no dash or verification digit are allowed.
                    Default None.

    Returns:
        str: The RUT number verification digit. Number 0 to 9 or 'k' letter.

    Raises:
        ValueError: when RUT number argument (rut:str) is not valid to be processed.
    """

    if not __is_only_numbers(rut) or len(rut) <= 2 or len(rut) >= 9:
        __raise_error(rut, 'is not valid to be processed (only numbers)')

    rut_digits = __clean_rut_string(rut)

    # Find verification digit
    reversed_digits = map(int, reversed(str(rut_digits)))
    factors = cycle(range(2, 8))
    mod_11 = sum(d * f for d, f in zip(reversed_digits, factors))
    verification = (-mod_11) % 11

    response = 'k' if verification == 10 else f'{verification}'
    return response


def format_rut(rut: str = None, validate_rut: bool = True) -> str:
    """
    Formats Chilean RUT number adding dots as thousands separator and a dash
    before verification digit

    Args:
        rut (str):  A Chilean RUT Number. Examples 5126663-3 or 5.126.663-3. Default None.
        validate_rut (bool, optional): Validate RUT number before format. Default True.

    Returns:
        str: Chilean RUT number formatted

    Raises:
        ValueError: when RUT number argument (rut:str) is not valid to be processed.
    """

    rut_digits = __clean_rut_string(rut)

    if not __is_rut_format(rut_digits) or len(rut_digits) <= 2 or len(rut_digits) >= 10:
        __raise_error(rut, 'is not a valid format to be processed')

    verification_digit = rut_digits[-1]
    numbers_rut = f'{int(rut_digits[:-1]):,}'.replace(',', '.')

    if validate_rut is True:
        if not is_valid(rut):
            __raise_error(rut, 'is not a valid Chilean RUT number')

    formatted_rut = f'{numbers_rut}-{verification_digit}'

    if not __is_rut_perfectly_formatted:
        __raise_error(rut, 'something went wrong with this RUT number')

    return formatted_rut


def clean_rut(rut: str = None, validate_rut: bool = True) -> str:
    """
    Cleans Chilean RUT number removing dots (thousands separador) and dash
    before verification digit.

    Args:
        rut (str): A Chilean RUT Number. Examples 5126663-3 or 5.126.663-3. Default None.
        validate_rut (bool, optional): Validates RUT number before cleaning. Default True.

    Returns:
        str: Chilean RUT number without format

    Raises:
        ValueError: when RUT number argument (rut:str) is not valid to be processed.
    """

    rut_digits = __clean_rut_string(rut)

    if not __is_rut_format(rut_digits) or len(rut_digits) <= 2 or len(rut_digits) >= 10:
        __raise_error(rut, 'is not a valid format to be processed')

    if validate_rut is True:
        if not is_valid(rut_digits):
            __raise_error(rut, 'is not a valid Chilean RUT number')

    return rut_digits
