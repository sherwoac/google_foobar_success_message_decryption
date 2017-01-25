import base64
# your text goes here
s1 = 'GkMSGE0QDRYBUE9VREYDEwhPB09JUlAMAAgNAQAKWxZPRUhXSAoXFQEEAEsXT0lSUAoJAg4WFR4J U1JFVR4BDBYEAAgPQhZPSVJQDgwMCAEXCEMWBhFVV1VPQxQKDQJNGA0BVVtPSBYABgMEWgBPRUhX SBwFBwFGQQ5UDgodUE9VREYTCAMPVBU= '
s2 = base64.b64decode(s1)
# your username goes here
s3 = 'adam.sherwood'
s3 *= (1 + len(s2) / len(s3))
print ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s2,s3))