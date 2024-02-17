from generic_decorator import *

run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        "First: We like to play it all\nSecond: Welcome to Tally Hall\n",
    ),
    (
        set(),
        {
            "conclusion": "## That's why Python is great!",
            "title": "Why Python is Great",
            "body": """Python is a great language.

## Reasons:
* It's really easy to learn
* Everyone uses it
""",
        },
        format_as_essay,
        """Title: Why Python is Great
Body: Python is a great language.

Reasons:
* It's really easy to learn
* Everyone uses it

Conclusion: That's why Python is great!
""",
    ),
]

submit_cases = run_cases + [
    (
        ("She's a killer queen",),
        {
            "second_doc": "### Gunpowder, gelatine",
        },
        concat,
        "First: She's a killer queen\nSecond: Gunpowder, gelatine\n",
    ),
    (
        (
            "Boots' grocery list",
            """Don't forget!

## Grocery List:
* Salmon
* Honey
* Quest Scrolls
""",
        ),
        {
            "conclusion": "## Boots is getting ready for the weekend!",
        },
        format_as_essay,
        """Title: Boots' grocery list
Body: Don't forget!

Grocery List:
* Salmon
* Honey
* Quest Scrolls

Conclusion: Boots is getting ready for the weekend!
""",
    ),
]


def test(args, kwargs, func, expected_output):
    print("---------------------------------")
    print(f"\nVariadic Arguments:\n{args}\n")
    print(f"Keyword Arguments:\n{kwargs}\n")
    print(f"Expecting:\n{expected_output}")
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:\n{result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

