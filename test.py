from ex5 import CaesarCipher, VigenereCipher, getVigenereFromStr, loadEncryptionSystem
import sys


def test1():
    caesar = CaesarCipher(3)
    return 'd' == caesar.encrypt('a')
def test2():
    caesar = CaesarCipher(-3)
    return caesar.encrypt('Mtm is the BEST!') == 'Jqj fp qeb YBPQ!'
def test3():
    caesar = CaesarCipher(3)
    return 'a' == caesar.decrypt('d')
def test4():
    caesar = CaesarCipher(-3)
    return caesar.decrypt('Jqj fp qeb YBPQ!') == 'Mtm is the BEST!'
def test5():
    vigenere = VigenereCipher([1,2,3,4,-5])
    if vigenere.encrypt('Hello World!')!='Igopj Xqupy!':
        return False
    if vigenere.decrypt('Igopj Xqupy!')!='Hello World!':
        return False
    return True 
def test8():
    loadEncryptionSystem('.')
    with open('plain.enc', 'r') as out:
        with open('plain.out', 'r') as expected:
            if out.read() != expected.read():
                return False
    return True 

def run(funcs):
    '''
    this function runs all the function in main scope with the string "test" in their name
    '''
    tests = [f for f in funcs if 'test' in f]
    if len(sys.argv) < 2:
        for test in tests:
            print(f'{test:.<50}', end='')
            passed = globals()[test]()
            if passed:
                print('SUCCESS')
            else:
                print('FAIL')
    else:
        test_num = int(sys.argv[1])
        if not 0<test_num<=len(tests):
            print('no such test!')
            return False
        test = f'test{test_num}'
        passed = globals()[test]()
        if passed:
            print('SUCCESS')
        else:
            print('FAIL')
    

if __name__ == '__main__':
    try:
        run(dir())
    except:
        print('FAIL')
