# Python testing in Visual Studio Code

## Resources

* <https://code.visualstudio.com/docs/python/testing>

## Original `settings.json`

```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests_unit",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestArgs": [
        "tests_pytest"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    // "python.testing.pytestEnabled": false,
    // "python.testing.unittestEnabled": true,
}
```

## Python

```python
def increment(x):
    """
    Increments the value of x by 1
    """
    return x + 1

def decrement(x):
    """
    Decrements the value of x by 1
    """
    return x - 1
```

## Pytest

```json
{
    "python.testing.pytestArgs": [
        "."     // Directory where the tests are located
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

## Unittest

```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        ".",    // Directory where the tests are located
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true
}
```
