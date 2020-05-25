'''Two different implementations of how to check whether or not a string
is made up of all unique characters. '''
def is_unique_1(string):
    '''
    string: str
    returns boolean

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    seen_chars = set()


    for char in string:

        if char in seen_chars:
            return False

        seen_chars.add(char)
    return True
