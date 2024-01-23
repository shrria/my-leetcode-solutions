def computeLongestSubString(text):
    start_index = 0

    remember_string = dict()
    longest_count = 0

    for current_index in range(len(text)):
        if text[current_index] in remember_string:
            start_index = current_index
            remember_string = dict()

        remember_string[text[current_index]] = True

        current_count = current_index - start_index + 1
        if longest_count < current_count:
            longest_count = current_count

    return longest_count


def generate_test_cases(n=100, l=10):
    import random
    import string

    test_cases = []
    for i in range(n):
        test_cases.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(l))
        )
    return test_cases


if __name__ == "__main__":
    test_cases = generate_test_cases()
    for test_case in test_cases:
        print(test_case, computeLongestSubString(test_case))
