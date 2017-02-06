import base64

def decrypt_message(encrypted_message, google_user):
    """ decrypts google foobar end message """
    encrypted_message_b64 = base64.b64decode(encrypted_message)
    google_user *= (1 + len(encrypted_message) / len(google_user))
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(encrypted_message_b64, google_user))


# your text goes here
print decrypt_message('GkMSGE0QDRYBUE9VREYDEwhPB09JUlAMAAgNAQAKWxZPRUhXSAoXFQEEAEsXT0lSUAoJAg4WFR4J U1JFVR4BDBYEAAgPQhZPSVJQDgwMCAEXCEMWBhFVV1VPQxQKDQJNGA0BVVtPSBYABgMEWgBPRUhX SBwFBwFGQQ5UDgodUE9VREYTCAMPVBU= ',
    'adam.sherwood')
