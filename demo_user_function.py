#! /use/bin/env python3
# how to define name call and optionally pas parameters in and optionally return data from a use function

def say_hello(greeting:str='ciao',recipient:str='amici'):
    message = f'{greeting} {recipient}'
    print(message)
    return None

say_hello('hello','my friends')
say_hello(greeting='konichiwa',recipient='tomodachi')
say_hello(recipient='mes amis',greeting='bonjour')
say_hello('ciao', )
