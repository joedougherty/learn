"""
Two types: bytes and str

bytes:
    Composed of 8-bit values

str:
    Composed of unicode characters
"""

# Let's say we get in a series of raw bytes:
band = b'Mot\xc3\xb6rhead'
    
# Want to see that umlaut in its full glory?
band_str = band.decode('utf-8') # >> 'Motörhead'
assert type(band_str) == str
