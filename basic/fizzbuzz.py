def fizzbuzz(start, end):
    fizzy = { 3: "fizz", 5: "buzz", 7: "bazz"}
    for i in range(start, end):
        res_str = ""
        for denom in fizzy:
            if i % denom == 0:
                res_str += fizzy[denom]
        if (res_str == ""):
            print(i)
        else:
            print(res_str)

# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()

