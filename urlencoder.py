#!/usr/bin/env python3

encoded_url = ""

def encoder(url):
    global encoded_url
    for character in url:
        if (not character.isalnum()) and character != "-" and character !=".":
            encoded_url = encoded_url + "%" + hex(ord(character))[2:]
        else:
            encoded_url = encoded_url + character
    print(encoded_url)

encoder("https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment")