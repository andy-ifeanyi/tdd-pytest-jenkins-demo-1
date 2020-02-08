def is_palindrome(seq):
    if seq.lower() == seq[::-1].lower():
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome("civic"))
    print(is_palindrome("Madam"))
    print(is_palindrome("02022020"))
    print(is_palindrome("year_of_the_harvest"))