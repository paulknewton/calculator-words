import calc_words


def test_is_not_encodable():
    assert calc_words.is_encodable("goodbye") is False


def test_words():
    good_words = {"bees": "5338",
                  "bellies": "5317738",
                  "big": "618",
                  "bobsleighs": "5461375808",
                  "boobies": "5318008",
                  "eggs": "5663",
                  "eggshells": "577345663",
                  "giggle": "376616",
                  "globe": "38076",
                  "hello": "07734",
                  "hiss": "5514",
                  "hobbies": "5318804",
                  "holes": "53704",
                  "igloo": "00761",
                  "legs": "5637",
                  "lollies": "5317707",
                  "shell": "77345",
                  "sleigh": "461375",
                  "zoo": "002"}
    for word in good_words:
        assert calc_words.is_encodable(word)
        assert calc_words.encode(word) == good_words[word]
