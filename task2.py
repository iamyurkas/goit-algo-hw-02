from collections import deque

def is_palindrome(input_str):
    filtered_str = ''.join(char.lower() for char in input_str if char.isalnum())
    queue = deque(filtered_str)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

test_strings = [
    "A man a plan a canal Panama",
    "No lemon, no melon",
    "Not a palindrome",
    "Palindromeemordnilap"
]

for s in test_strings:
    print(f"'{s}' -> {'Palindrome' if is_palindrome(s) else 'Not palindrome'}")
