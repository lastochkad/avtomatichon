import pytest
from string_utils import StringUtils
utils = StringUtils()

#Проверки Capitalize
def test_capitalize():
    """Posotive"""
    assert utils.capitilize("pyatigorsk") == "Pyatigorsk"
    assert utils.capitilize( "i love ny") == "I love ny"
    assert utils.capitilize("777") == "777"
    """Negative"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("123usa") == "123usa"

#Проверки Trim
@pytest.mark.parametrize('line, result', [(" hello","hello"),("H ello","H ello")])
def test_trim(line, result):
    assert utils.trim(line) == result

@pytest.mark.xfail
def test_negative_trim_with_numbers():
    assert utils.trim(" 123") == " 123"

@pytest.mark.xfail
def test_negative_trim_with_space():
    assert utils.trim(" space ") == " space "

#Проверка to_list
@pytest.mark.parametrize('string, delimetr, result', [
    ("dog,cat,bird", ",", ["dog","cat","bird"]),
    ("1,2,3,4", ",",["1","2","3","4"]),
    ("!*@*#*$", "*", ["!","@","#","$"]),
    #Negative
    ("", None, [] ),
    ("1,2,3,4,5", None, ["1","2","3","4","5"]),                                               
])
def test_to_list(string,delimetr,result):
    if delimetr is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string,delimetr)

    assert res == result 

#Проверка Containce 

@pytest.mark.parametrize('string,symbol,result',[
    ("Father","h", True),
    ("Mother","M", True),
    (" Dog","o", True),
    ("222","2", True),
    ("NewYork","z", False),
    ("12345","t", False),
    ("Rex","", False) # ERROR см. defects.txt
])
def test_contains(string,symbol,result):
    res= utils.contains(string,symbol)
    assert res == result

# Проверка Delete symbol

@pytest.mark.parametrize('string,symbol,result',[
    ("Одеяло","О","деяло"),
    ("парное молоко"," ","парноемолоко"),
    ("7575","5","77"),
    #Negative
    ("Ежик","п","Ежик"),
    ("парашют","","парашют"),
    ("","ы",""),
    ("","","")
])
def test_delete_symbol(string,symbol,result):
    res = utils.delete_symbol(string,symbol)
    assert res == result

# Проверка Starts_with

@pytest.mark.parametrize('string,symbol,result',[
    ("Swarrow","S",True),
    ("girlfriend","g",True),
    ("236","2",True),
    #Negative
    ("JhonSnow","f",False),
    ("Gregor","g",False),
    ("","%",False),
    ("","",False)# ERROR см. Defects.txt
])
def test_starts_with(string,symbol,result):
    res = utils.starts_with(string,symbol)
    assert res == result

    #Проверка end_with 

@pytest.mark.parametrize('string,symbol,result',[
    ("Dragon","n", True),
    ("HarryPotter","r", True),
    ("victory","y", True),
    ("6777","7", True),
    #Negative
    ("Loop","P",False),
    ("city","z",False),
    ("","6",False)
])
def test_end_with(string,symbol,result):
    res = utils.end_with(string,symbol)
    assert res == result

# Проверка is_empty

@pytest.mark.parametrize('string,result',[
    ("",True),
    (" ",True),
    ("  ",True),
    #Negative
    ("123",False),
    ("Hiii",False),
    ("@#$",False)
])
def test_is_empty(string,result):
    res = utils.is_empty(string)
    assert res == result

# Проверка list_to_string

@pytest.mark.parametrize('lst,joiner,result',[
    (["D","A","D"],",","D,A,D"),
    ([1, 2, 3, 4, 5], None,"1, 2, 3, 4, 5"),
    (["Mother","Father"],"&","Mother&Father"),
    (["L","O","L"],"","LOL"),
    #Negative
    ([],None,""),
    ([],",",""),
    ([],"H","")
])
def test_list_to_string(lst,joiner,result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst,joiner)
    assert res == result 