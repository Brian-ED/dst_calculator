tests = 0
ko = 0


def is_test_ok(result: bool, name: str) -> None:
    global tests
    global ko
    tests += 1
    if result:
        print("[OK]", end="")
    else:
        print("[KO]", end="")
        ko += 1
    print(name)


print("All my tests")

is_test_ok(1 == 1, "simple")

exit(ko)
