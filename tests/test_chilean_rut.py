import pytest
import chilean_rut
from chilean_rut import __version__


def test_version():
    assert __version__ == '0.1.0'


class TestIsValid:

    @pytest.mark.parametrize("input_value, expected_value", [
        ("17317684-8", True),
        ("16202879-0", True),
        ("6141076-7", True),
        ("5440241-4", True),
        ("12450547-k", True),
        ("17.317.684-8", True),
        ("16.202.879-0", True),
        ("6.141.076-7", True),
        ("5.440.241-4", True),
        ("12.450.547-k", True),
        ("173176848", True),
        ("162028790", True),
        ("61410767", True),
        ("54402414", True),
        ("12450547k", True),
    ])
    def test_valid_rut(self, input_value, expected_value):
        assert chilean_rut.is_valid(input_value) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", False),
        ("4.", False),
        (".-", False),
        ("3-", False),
        ("*", False),
        ("2", False),
        ("k", False),
        (" ", False),
        ("", False),
        (None, False),
        ("17317684-2", False),
        ("16202879-1", False),
        ("6141076-k", False),
        ("5440241-3", False),
        ("12450547-2", False),
        ("17.317.684-1", False),
        ("16.202.879-9", False),
        ("6.141.076-4", False),
        ("5.440.241-2", False),
        ("12.450.547-1", False),
        ("173176840", False),
        ("162028798", False),
        ("6141076k", False),
        ("54402412", False),
        ("124505471", False),
        ("12450547.k", False),
        ("12,450,547-k", False),
        ("12,450,547k", False),
        ("12*450*547k", False),
        ("error12.450.547-k", False)
    ])
    def test_invalid_rut(self, input_value, expected_value):
        assert chilean_rut.is_valid(input_value) == expected_value


class TestGetVerificationDigit:

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", ValueError),
        ("4.", ValueError),
        (".-", ValueError),
        ("3-", ValueError),
        ("*", ValueError),
        ("2", ValueError),
        ("k", ValueError),
        ("2k", ValueError),
        (" ", ValueError),
        ("", ValueError),
        (None, ValueError),
        ("12312-K", ValueError),
        ("12.312-K", ValueError),
        ("17317684-8", ValueError),
        ("12.450.547-k", ValueError),
    ])
    def test_invalid_rut_argument(self, input_value, expected_value):
        with pytest.raises(ValueError) as error:
            chilean_rut.get_verification_digit(input_value)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("22174688", "0"),
        ("22191269", "1"),
        ("16615805", "2"),
        ("14505346", "3"),
        ("6088258", "4"),
        ("10502516", "5"),
        ("5338758", "6"),
        ("20878704", "7"),
        ("15131923", "8"),
        ("9692487", "9"),
        ("10065654", "k"),
        ("8101865", "0"),
        ("21291924", "1"),
        ("22859224", "2"),
        ("13562292", "3"),
        ("18430875", "4"),
        ("23203058", "5"),
        ("24813516", "6"),
        ("10521968", "7"),
        ("11905223", "8"),
        ("11267918", "9"),
        ("5391862", "k")
    ])
    def test_valid_rut(self, input_value, expected_value):
        assert chilean_rut.get_verification_digit(input_value) == expected_value


class TestFormatRut:

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", ValueError),
        ("4.", ValueError),
        (".-", ValueError),
        ("3-", ValueError),
        ("*", ValueError),
        ("2", ValueError),
        ("k", ValueError),
        ("2k", ValueError),
        (" ", ValueError),
        ("", ValueError),
        (None, ValueError),
        ("12312-K", ValueError),
        ("12.312-K", ValueError),
        ("24752955-2", ValueError),
        ("24.752.955-2", ValueError)
    ])
    def test_format_rut_true_raise(self, input_value, expected_value):
        with pytest.raises(ValueError) as error:
            chilean_rut.format_rut(input_value, True)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", ValueError),
        ("4.", ValueError),
        (".-", ValueError),
        ("3-", ValueError),
        ("*", ValueError),
        ("2", ValueError),
        ("k", ValueError),
        ("2k", ValueError),
        (" ", ValueError),
        ("", ValueError),
        (None, ValueError),
        ("123.111.111-2", ValueError),
    ])
    def test_format_rut_false_raise(self, input_value, expected_value):
        with pytest.raises(ValueError) as error:
            chilean_rut.format_rut(input_value, False)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("17317684-8", "17.317.684-8"),
        ("16202879-0", "16.202.879-0"),
        ("6141076-7", "6.141.076-7"),
        ("5440241-4", "5.440.241-4"),
        ("12450547-k", "12.450.547-k"),
        ("17.317.684-8", "17.317.684-8"),
        ("16.202.879-0", "16.202.879-0"),
        ("6.141.076-7", "6.141.076-7"),
        ("5.440.241-4", "5.440.241-4"),
        ("12.450.547-k", "12.450.547-k"),
        ("173176848", "17.317.684-8"),
        ("162028790", "16.202.879-0"),
        ("61410767", "6.141.076-7"),
        ("54402414", "5.440.241-4"),
        ("12450547k", "12.450.547-k"),
    ])
    def test_format_rut_true(self, input_value, expected_value):
        assert chilean_rut.format_rut(input_value) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("17317684-8", "17.317.684-8"),
        ("16202879-0", "16.202.879-0"),
        ("6141076-7", "6.141.076-7"),
        ("5440241-4", "5.440.241-4"),
        ("12450547-k", "12.450.547-k"),
        ("17.317.684-8", "17.317.684-8"),
        ("16.202.879-0", "16.202.879-0"),
        ("6.141.076-7", "6.141.076-7"),
        ("5.440.241-4", "5.440.241-4"),
        ("12.450.547-k", "12.450.547-k"),
        ("173176848", "17.317.684-8"),
        ("162028790", "16.202.879-0"),
        ("61410767", "6.141.076-7"),
        ("54402414", "5.440.241-4"),
        ("12450547k", "12.450.547-k"),
        ("17317684-2", "17.317.684-2"),
        ("16202879-1", "16.202.879-1"),
        ("6141076-5", "6.141.076-5"),
        ("5440241-2", "5.440.241-2"),
        ("12450547-9", "12.450.547-9"),
        ("17.317.684-1", "17.317.684-1"),
        ("16.202.879-k", "16.202.879-k"),
        ("6.141.076-8", "6.141.076-8"),
        ("5.440.241-1", "5.440.241-1"),
        ("12.450.547-0", "12.450.547-0"),
        ("173176844", "17.317.684-4"),
        ("162028792", "16.202.879-2"),
        ("61410761", "6.141.076-1"),
        ("54402416", "5.440.241-6"),
        ("124505478", "12.450.547-8"),
        ("134", "13-4"),
        ("1345", "134-5"),
        ("21345", "2.134-5"),
        ("1121345", "112.134-5")
    ])
    def test_format_rut_false(self, input_value, expected_value):
        assert chilean_rut.format_rut(input_value, False) == expected_value


class TestCleanRut:

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", ValueError),
        ("4.", ValueError),
        (".-", ValueError),
        ("3-", ValueError),
        ("*", ValueError),
        ("2", ValueError),
        ("k", ValueError),
        ("2k", ValueError),
        (" ", ValueError),
        ("", ValueError),
        (None, ValueError),
        ("12312-K", ValueError),
        ("12.312-K", ValueError),
        ("24752955-2", ValueError),
        ("24.752.955-2", ValueError)
    ])
    def test_clean_rut_true_raise(self, input_value, expected_value):
        with pytest.raises(ValueError) as error:
            chilean_rut.clean_rut(input_value, True)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        (".1", ValueError),
        ("4.", ValueError),
        (".-", ValueError),
        ("3-", ValueError),
        ("*", ValueError),
        ("2", ValueError),
        ("k", ValueError),
        ("2k", ValueError),
        (" ", ValueError),
        ("", ValueError),
        (None, ValueError),
        ("123.111.111-2", ValueError),
    ])
    def test_clean_rut_false_raise(self, input_value, expected_value):
        with pytest.raises(ValueError) as error:
            chilean_rut.clean_rut(input_value, False)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("17317684-8", "173176848"),
        ("16202879-0", "162028790"),
        ("6141076-7", "61410767"),
        ("5440241-4", "54402414"),
        ("12450547-k", "12450547k"),
        ("17.317.684-8", "173176848"),
        ("16.202.879-0", "162028790"),
        ("6.141.076-7", "61410767"),
        ("5.440.241-4", "54402414"),
        ("12.450.547-k", "12450547k"),
        ("173176848", "173176848"),
        ("162028790", "162028790"),
        ("61410767", "61410767"),
        ("54402414", "54402414"),
        ("12450547k", "12450547k"),
    ])
    def test_format_rut_true(self, input_value, expected_value):
        assert chilean_rut.clean_rut(input_value) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("17317684-8", "173176848"),
        ("16202879-0", "162028790"),
        ("6141076-7", "61410767"),
        ("5440241-4", "54402414"),
        ("12450547-k", "12450547k"),
        ("17.317.684-8", "173176848"),
        ("16.202.879-0", "162028790"),
        ("6.141.076-7", "61410767"),
        ("5.440.241-4", "54402414"),
        ("12.450.547-k", "12450547k"),
        ("173176848", "173176848"),
        ("162028790", "162028790"),
        ("61410767", "61410767"),
        ("54402414", "54402414"),
        ("12450547k", "12450547k"),
        ("17317684-2", "173176842"),
        ("16202879-1", "162028791"),
        ("6141076-5", "61410765"),
        ("5440241-2", "54402412"),
        ("12450547-9", "124505479"),
        ("17.317.684-1", "173176841"),
        ("16.202.879-k", "16202879k"),
        ("6.141.076-8", "61410768"),
        ("5.440.241-1", "54402411"),
        ("12.450.547-0", "124505470"),
        ("173176844", "173176844"),
        ("162028792", "162028792"),
        ("61410761", "61410761"),
        ("54402416", "54402416"),
        ("124505478", "124505478"),
        ("134", "134"),
        ("1345", "1345"),
        ("21345", "21345"),
        ("1121345", "1121345")
    ])
    def test_format_rut_false(self, input_value, expected_value):
        assert chilean_rut.clean_rut(input_value, False) == expected_value
