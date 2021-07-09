import word_processor
import pytest

@pytest.mark.parametrize("word, expected", [("hello", "hello!"), ("h", "h!"), ("1","1!"), ("", "!")])
def test_add_excl_mark(word, expected):
    assert word_processor.add_exclamation_mark(word) == expected

def test_type_error_add_excl_mark():
    with pytest.raises(TypeError):
        word_processor.add_exclamation_mark()

def test_type_error_add_excl_mark_too_much_params():
    with pytest.raises(TypeError):
        word_processor.add_exclamation_mark(1,2,3)

# ------

def test_chars_counter():
    assert word_processor.chars_counter("cat") == 3
    assert word_processor.chars_counter("") == 0

def test_type_error_chars_counter():
    with pytest.raises(TypeError):
        word_processor.chars_counter()

# ------

@pytest.mark.parametrize("word, char, expected", [("dog","o",1), ("generate","e",3), ("with","x",0)])
def test_char_occurence_counter(word, char, expected):
    assert word_processor.char_occurence_counter(word, char) == expected

def test_char_occurence_counter_without_parameteres():
    assert word_processor.char_occurence_counter("dog", "o") == 1
    assert word_processor.char_occurence_counter("generate", "e") == 3
    assert word_processor.char_occurence_counter("with", "x") == 0

def test_type_error_char_occurence_counter():
    with pytest.raises(TypeError):
        word_processor.char_occurence_counter()

# ------

def test_word_reverse():
    assert word_processor.word_reverse("pass") == "ssap"
    assert word_processor.word_reverse("p") == "p"
    assert word_processor.word_reverse("") == ""

def test_type_error_word_reverse():
    with pytest.raises(TypeError):
        word_processor.word_reverse()





