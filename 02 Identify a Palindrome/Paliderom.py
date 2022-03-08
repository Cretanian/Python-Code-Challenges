#!/usr/bin/python

def check_for_palindrome(str):
    tail = len(str) - 1
    head = 0
    while head <= tail:
        if str[head] != str[tail]:
            return False
        tail -= 1
        head += 1
    return True


if __name__ == '__main__':
    print('Enter your string:')
    str_input = input()
    # removing special characters
    str_input = ''.join(e for e in str_input if e.isalnum())
    print(check_for_palindrome(str_input.lower()))
