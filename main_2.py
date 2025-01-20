import pytest
def upper(s):
    return s.upper()

def test_upper():
    assert upper("привіт") == "ПРИВІТ"

def palindrome(s):
    return s == s[::-1]



def test_palindrome():
    assert palindrome("Мадам")
    assert palindrome("Анна")
    assert palindrome("Привіт")
upper("привіт")
test_upper()
palindrome()
test_palindrome()