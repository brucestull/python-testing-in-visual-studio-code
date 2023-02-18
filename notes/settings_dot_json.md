# Testing Configuration for VS Code

## Unittest

```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests_unit",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true
}
```

## Pytest

```json
{
    "python.testing.pytestArgs": [
        "tests_pytest"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```
