# Python testing in Visual Studio Code

## Next Concept to Investigate

* [IntelliSense for pytest](https://code.visualstudio.com/docs/python/testing#_intellisense-for-pytest)

## Resources

* <https://code.visualstudio.com/docs/python/testing>
  * [Test configuration settings](https://code.visualstudio.com/docs/python/testing#_test-configuration-settings)
  * [Test discovery](https://code.visualstudio.com/docs/python/testing#_test-discovery)
  * [Run tests in parallel](https://code.visualstudio.com/docs/python/testing#_run-tests-in-parallel)

## Python

```python
def increment(x):
    """
    Increments the value of x by 1.
    """
    return x + 1

def decrement(x):
    """
    Decrements the value of x by 1.
    """
    return x - 1
```

## Unified `settings.json`

```json
{
    "python.testing.pytestArgs": [
        "."     // Directory where the tests are located
    ],
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        ".",    // Directory where the tests are located
        "-p",
        "test_*.py"
    ],
    // "python.testing.unittestEnabled": true,
    // "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
}
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

## `settings.json` With Tests Nested Inside Separate Directories

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
