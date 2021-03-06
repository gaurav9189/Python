import requests
import sys
import hashlib


def pwned_api(hash_char):
    url = 'https://api.pwnedpasswords.com/range/' + hash_char
    try:
        response = requests.get(url)
        print(response.status_code)

    except:
        print('something is wrong')
    return response


def hash_generator(password):
    pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(pw)
    first_5, last = pw[:5], pw[5:]
    # print(first_5)
    # print(last)
    output = pwned_api(first_5)
    for i in output.text.splitlines():
        li = i.split(':')
        if last in li:
            return li[1]
    return 0


def check_password(args):
    for i in args:
        count = hash_generator(i)
        if count:
            print(f'found the match, used {count} times')
        else:
            print('Carry on using this one')


if __name__ == '__main__':
    check_password(sys.argv[1:])
