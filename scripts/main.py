"""
MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from shutil import copytree
from os import system


def new_VOS():
    VOS_name = input('Please enter a name you would like to call your VOS (Please remember this path you need it later!): ')
    copytree(src='new_VOS_files', dst=f'VOSs/{VOS_name}')


def open_VOS():
    VOS_name = input('Please enter the name of your VOS: ')
    if not system(f'cd "VOSs/{VOS_name}" && python3 "root/boot/boot.py"'):
        system(f'cd "VOSs/{VOS_name}" && python "root/boot/boot.py"')


print('******************************Welcome!!!******************************')
while True:
    choice = input('Enter "n" for a new VOS and "o" to open an existing VOS: ')
    if choice == 'n':
        new_VOS()
        break
    elif choice == 'o':
        open_VOS()
        break
    else:
        print('Sorry, try again!')
