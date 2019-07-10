def palindrome(s):
    if (len(s) < 2):
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])

def test_equal(actual, expected, msg=""):
    if actual != expected:
        print('Error testing {}. expected: {}, got {}'.format(
            msg, expected, actual))


test_equal(palindrome(""), True, "Empty Palindrome")
test_equal(palindrome("a"), True, "a")
test_equal(palindrome("xx"), True, "xx")
test_equal(palindrome("xo"), False, "xo")
test_equal(palindrome("lol"), True, "lol")
test_equal(palindrome("log"), False, "log")
test_equal(palindrome("1234321"), True, "1234321")
test_equal(palindrome("12344321"), True, "1234321")
test_equal(palindrome("ffffffff"), True, "ffffffff")
test_equal(palindrome("koko"), False, "koko")