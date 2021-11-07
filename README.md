# **Chilean RUT** | [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]()

Python module to validate, format, clean and get verification digit for Chileans RUT/RUN numbers

## **Introduction**

### What is a RUN/RUT?

It's a unique identification number given to every natural person (RUN) or juridical person (RUT).
* RUN (Rol Único Nacional) 
* RUT (Rol Único Tributario)

For individuals, the RUN number is the same as the RUT and also in Chile the word "RUT" is commonly used to refer to the RUN number, they are not synonymous but they are used as if they were.

RUT / RUN numbers have seven or eight digits, plus a verification digit, and are generally written in this format: xx.xxx.xxx-z. Where Z can be a digit or the letter K, and it’s determined by "Module 11 algorithm" ensuring that typing mistakes when entering a RUT or RUN number will result in an invalid number.

## **Installation**
```
$ pip install chilean-rut
```

## **Usage**

### **is_valid**

Checks if a Chilean RUT number is valid or not.

| Argument | Type   | Default | Description          |
| -------- | ------ | ------- | -------------------- |
| rut      | string | None    | A Chilean RUT Number |

```
import chilean_rut

# Valid RUT numbers (correct verification digit)
chilean_rut.is_valid('17.317.684-8') # True
chilean_rut.is_valid('17317684-8)    # True
chilean_rut.is_valid('173176848)     # True
# Wrong RUT numbers (bad verification digit)
chilean_rut.is_valid('17.317.684-2)  # False
chilean_rut.is_valid('17317684-2)    # False
chilean_rut.is_valid('173176842)     # False
```

### **get_verification_digit**

Calculates the verification number or letter.

| Argument | Type   | Default | Description                                     |
| -------- | ------ | ------- | ----------------------------------------------- |
| rut      | string | None    | A Chilean RUT number without verification digit |

```
import chilean_rut

chilean_rut.get_verification_digit('22174688')     # 0
chilean_rut.get_verification_digit('22191269)      # 1
chilean_rut.get_verification_digit('16615805)      # 2
chilean_rut.get_verification_digit('14505346)      # 3
chilean_rut.get_verification_digit('6088258)       # 4
chilean_rut.get_verification_digit('5391862)       # k
chilean_rut.get_verification_digit('12312-K')      # ValueError
chilean_rut.get_verification_digit('12.312-K')     # ValueError
chilean_rut.get_verification_digit('17317684-8')   # ValueError
chilean_rut.get_verification_digit('12.450.547-k') # ValueError
```

### **format_rut**

Formats Chilean RUT number adding dots as thousands separator and a dash before verification digit.

| Argument     | Type   | Default | Description                       |
| ------------ | ------ | ------- | --------------------------------- |
| rut          | string | None    | A Chilean RUT Number              |
| validate_rut | bool   | True    | Validate RUT number before format |

```
import chilean_rut

# Valid RUT numbers (correct verification digit)
chilean_rut.format_rut('17317684-8', True)   # 17.317.684-8
chilean_rut.format_rut('12.450.547-k, True)  # 12.450.547-k
chilean_rut.format_rut('61410767', True)      # 6.141.076-7
# Wrong RUT numbers (bad verification digit)
chilean_rut.format_rut('17317684-1', True)   # ValueError
chilean_rut.format_rut('12.450.547-2', True)  # ValueError
chilean_rut.format_rut('61410763', True)      # ValueError

# Valid RUT numbers (correct verification digit)
chilean_rut.format_rut('17317684-8', False)   # 17.317.684-8
chilean_rut.format_rut('12.450.547-k, False)  # 12.450.547-k
chilean_rut.format_rut('61410767', False)      # 6.141.076-7
# Wrong RUT numbers (bad verification digit)
chilean_rut.format_rut('17317684-1', False)   # 17.317.684-1
chilean_rut.format_rut('12.450.547-2', False)  # 12.450.547-2
chilean_rut.format_rut('61410763', False)      # 6.141.076-3

# Invalid RUT format
chilean_rut.format_rut('123.111.111-2', True)   # ValueError
chilean_rut.format_rut('123.111.111-2', False) # ValueError
```

### **clean_rut**

Cleans Chilean RUT number removing dots (thousands separador) and dash before verification digit.

| Argument     | Type   | Default | Description                       |
| ------------ | ------ | ------- | --------------------------------- |
| rut          | string | None    | A Chilean RUT Number              |
| validate_rut | bool   | True    | Validates RUT number before clean |

```
import chilean_rut

# Valid RUT numbers (correct verification digit)
chilean_rut.clean_rut('17317684-8', True)   # 173176848
chilean_rut.clean_rut('12.450.547-k, True)  # 12450547k
chilean_rut.clean_rut('61410767, True)      # 61410767
# Wrong RUT numbers (bad verification digit)
chilean_rut.clean_rut('17317684-1', True)   # ValueError
chilean_rut.clean_rut('12.450.547-2', True)  # ValueError
chilean_rut.clean_rut('61410763', True)      # ValueError

# Valid RUT numbers (correct verification digit)
chilean_rut.clean_rut('17317684-8', False)   # 173176848
chilean_rut.clean_rut('12.450.547-k, False)  # 12450547k
chilean_rut.clean_rut('61410767, False)      # 61410767
# Wrong RUT numbers (bad verification digit)
chilean_rut.clean_rut('17317684-1', False)   # 173176841
chilean_rut.clean_rut('12.450.547-2', False)  # 124505472
chilean_rut.clean_rut('61410763', False)      # 61410763

# Invalid RUT format
chilean_rut.format_rut('123.111.111-2,True)   # ValueError
chilean_rut.format_rut('123.111.111-2, False) # ValueError
```


## **Test**
Running tests:
```
$ pytest
```

Checking the package installs correctly with different Python versions and interpreters.

Tested with python3.6, python3.7, python3.8, python3.9 and python3.10 versions:
```
$ tox
```

## **Contributing**
Contributions are welcome - submit an issue/pull request.