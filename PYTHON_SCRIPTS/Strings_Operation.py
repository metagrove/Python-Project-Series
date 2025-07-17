'''
Strings are immutable sequences of Unicode characters.
Python offers powerful methods for manipulation:

len(), lower(), upper(), split(), replace(), find(), slicing ([start:end])

'''

msg = "Hello"
print(len(msg))      # 5
print(msg.upper())   # HELLO


sentence = "I love Python"
words = sentence.split()
print(words)          # ['I', 'love', 'Python']

email = "user@example.com"
username = email.split("@")[0]
domain = email.split("@")[1]
print(f"Username: {username}, Domain: {domain}")
