# -*- coding: utf-8 -*-
def testa_funcao(funcao):
    import inspect
    def test(got, expected):
        if got == expected:
            prefix = ' OK '
        else:
            prefix = '  X '
        print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
    
    if not inspect.isfunction(funcao):
        print ("Argumento não é função!")
        return
 
    if funcao.__name__=="match_ends":
        print ('match_ends')
        test(funcao(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        test(funcao(['', 'x', 'xy', 'xyx', 'xx']), 2)
        test(funcao(['aaa', 'be', 'abc', 'hello']), 1)
    elif funcao.__name__=='front_x':
        print ('front_x')
        test(funcao(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
             ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        test(funcao(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
             ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        test(funcao(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
             ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    elif funcao.__name__=='sort_last':
        print ('sort_last')
        test(funcao([(1, 3), (3, 2), (2, 1)]),
             [(2, 1), (3, 2), (1, 3)])
        test(funcao([(2, 3), (1, 2), (3, 1)]),
             [(3, 1), (1, 2), (2, 3)])
        test(funcao([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
             [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    elif funcao.__name__=='donuts':
        print ('donuts')
        test(funcao(4), 'Number of donuts: 4')
        test(funcao(9), 'Number of donuts: 9')
        test(funcao(10), 'Number of donuts: many')
        test(funcao(99), 'Number of donuts: many')
    elif funcao.__name__=='both_ends':
        print ('both_ends')
        test(funcao('spring'), 'spng')
        test(funcao('Hello'), 'Helo')
        test(funcao('a'), '')
        test(funcao('xyz'), 'xyyz')
    elif funcao.__name__=='fix_start':
        print ('fix_start')
        test(funcao('babble'), 'ba**le')
        test(funcao('aardvark'), 'a*rdv*rk')
        test(funcao('google'), 'goo*le')
        test(funcao('donut'), 'donut')
    elif funcao.__name__=='mix_up':
        print ('mix_up')
        test(funcao('mix', 'pod'), 'pox mid')
        test(funcao('dog', 'dinner'), 'dig donner')
        test(funcao('gnash', 'sport'), 'spash gnort')
        test(funcao('pezzy', 'firm'), 'fizzy perm')
    elif funcao.__name__=='verbing':
        print ('verbing')
        test(funcao('hail'), 'hailing')
        test(funcao('swiming'), 'swimingly')
        test(funcao('do'), 'do')
    elif funcao.__name__=='not_bad':
        print ('not_bad')
        test(funcao('This movie is not so bad'), 'This movie is good')
        test(funcao('This dinner is not that bad!'), 'This dinner is good!')
        test(funcao('This tea is not hot'), 'This tea is not hot')
        test(funcao("It's bad yet not"), "It's bad yet not")
    elif funcao.__name__=='front_back':
        print ('front_back')
        test(funcao('abcd', 'xy'), 'abxcdy')
        test(funcao('abcde', 'xyz'), 'abcxydez')
        test(funcao('Kitten', 'Donut'), 'KitDontenut')
   
