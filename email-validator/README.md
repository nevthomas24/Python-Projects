# Email Validator

A beginner-friendly command-line tool, written in Python, that checks whether an email address looks valid. It keeps asking until you enter a valid one.

## How to run

You need Python 3 installed.

```bash
python email_validator.py
```

## Example

```
*** Welcome to Email Validator ***
Enter your email address: abc
Too Short (minimum 6 characters)
Enter your email address: nevil@gmail
Domain needs a dot
Enter your email address: nevil@gmail.com
Valid Email Address!
```

## What it checks

An email is rejected if it:

- is shorter than 6 characters
- contains spaces
- does not contain exactly one `@`
- has nothing before the `@`
- has no dot in the part after the `@`
- has a domain that starts or ends with a dot

## How it works

- `validate_email(email)` holds the rules. It returns a pair: `(True/False, message)`.
- `main()` handles the user input and repeats the prompt until the email is valid.
- Each rule is a separate check that returns early, so the user gets a specific error message instead of a generic "invalid".

## Concepts practised

- Functions and return values (returning two values at once)
- `while` loops and `break`
- String methods: `.count()`, `.split()`, `.strip()`, `.startswith()`, `.endswith()`
- Early returns instead of deeply nested `if/else`
- Separating logic from input/output

## Limitations

This is a learning project, not a production validator.

- It does not catch every invalid address (for example, `nevil@gmail..com` and `nevil@gmail.c` pass).
- It does not check that the domain or mailbox actually exists.
- The only reliable way to validate an email is to send a confirmation message to it.

## Ideas for improvement

- Reject consecutive dots in the domain
- Require a domain ending of at least 2 characters
- Rewrite the checks using regular expressions (`re` module)
- Add automated tests with `pytest`
