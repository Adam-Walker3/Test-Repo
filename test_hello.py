from hello import reverseString

def test_reverse1():
    assert reverseString("hello") == "olleh"

def test_reverse2():
    assert reverseString("123456789") == "987654321"