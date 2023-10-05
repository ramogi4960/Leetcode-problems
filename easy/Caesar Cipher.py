"""
The Caesar Cipher is a message encoding system that was used by Julius Caesar. The decoded message was a string
"""


def caesar_cipher(message: str, skip=1) -> (str, int):
    encoded_message = ''
    for item in message: encoded_message += chr(ord(item) + skip)
    return (encoded_message, skip)


if __name__ == "__main__":
    x = "The quick brown fox jumped over the lazy dog"
    print(f"""Test Input:
{x}
**
will return:
{caesar_cipher(x)[0]}
""")