'''
Составные ассерты:
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"
'''

# Sample Output:
# expected 8, got 11
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f'expected {expected_result}, got {actual_result}'


# Sample Output:
# expected 'some_value' to be substring of 'fulltext':
def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


'''
__name__ хранит имя модуля
__main__ говорит о том, что скрипт был запущен самостоятельно

Cлужит для подтверждения того, что данный скрипт был запущен напрямую, 
а не вызван внутри другого файла в качестве модуля
'''

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__": # если был запущен самостоятельно, то:
    test_abs1()
    print("All tests passed!")

# Чтобы запустить: "python3 name.py"

# EXAMPLE
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")



