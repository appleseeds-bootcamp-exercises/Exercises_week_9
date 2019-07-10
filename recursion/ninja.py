def reverse1(a_list):
    if len(a_list) == 0:
        return []
    return reverse1(a_list[1:]) + [a_list[0]]


def reverse_helper(a_list, index):
    if index >= len(a_list) // 2:
        return
    temp = a_list[index]
    a_list[index] = a_list[-1 - index]
    a_list[-1 - index] = temp
    reverse_helper(a_list, index + 1)


def reverse2(a_list):
    reverse_helper(a_list, 0)
    return a_list


def test_equal(actual, expected, msg=""):
    if actual != expected:
        print('Error testing {}. expected: {}, got {}'.format(
            msg, expected, actual))


# tests for function 1:
test_equal(reverse2([]), [], "Empty list")
test_equal(reverse2([33]), [33], "[33]")
test_equal(reverse2([1, 2]), [2, 1], "[1, 2]")
test_equal(reverse2([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1], "[1,2,3,4,5]")
test_equal(reverse1([]), [], "Empty list")
test_equal(reverse1([33]), [33], "[33]")
test_equal(reverse1([1, 2]), [2, 1], "[1, 2]")
test_equal(reverse1([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1], "[1,2,3,4,5]")