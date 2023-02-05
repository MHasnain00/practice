# import re
# location = int(input('On which floor you are in europe : ')) + 1
# Original_Place = f'You are on {location} floor'
# name = input('What is your name : ')
# print(f'Hello {name} my name is Laptop')
# Num = int(input('Input a number : '))
# calc = int(input('Type another number : '))
# print(f' Your solution is {Num+calc}')
# def new():
#     try:
#         t = int(input("Temperature Outside : "))
#     except ValueError:
#         print('Wrong input')
#         quit()
#     print(t - 32.0)
#
#
# new()
#
# # while True:
# #     try:
# #         temp = float(input('What is the temperature Outside : '))
# #         break
# #     except ValueError:
# #         print("You entered wrong input")
# # print(temp - 32.0)
# while True:
#     try:
#         temp = int(input('What is the temperature Outside : '))
#         break
#     except ValueError:
#         print("You entered wrong input")
# if temp == 25 or temp == 24:
#     print('WOW')
# elif temp < 24:
#     print('it means its Winter')
# else:
#     print('It means its Summer ')
#
# smallest = None
# print("Before:", smallest)
# for number in [89, 41, 12, 9, 74, 15, 32, 6, 1, ]:
#     if smallest is None:
#         smallest = number
#     elif number < smallest:
#         smallest = number
#     print("Loop:", number, smallest)
# print("Smallest:", smallest)
# word = "banana"
# i = word.find("na")
# print(i)
# simple = 'heLLo WoRld'
# spaces = '  help    '
# print(simple)
# New = True
# while New:
#     print(simple.lower())
#     print(simple.upper())
#     print(simple.find('o'))
#     print(simple.endswith('d'))
#     print(simple.startswith('i'))
#     print(simple.count('o'))
#     print(type(simple))
#     print(spaces.strip())
#     New = False
# My_Data = "From MuhammadHasnaninGct@gmail.com sat 15 09:45 AM"
# location = My_Data.find('@')
# Space = My_Data.find(' ', location)
# print(My_Data[location+1:Space])
# file = open("New.txt")
# mmm = file.read()
# print(len(mmm))
# for line in file:
#     line = line.rstrip()
#     if line.startswith('I'):
#         print(line)
#     elif line.endswith('com'):
#         print(line)
# file = open("New.txt")
# counter = 0
# for line in file:
#     counter += 1
# print(counter)
# file = open("New.txt")
# reader = file.read()
# print(len(reader))
# User = input('Input file name : ')
# try:
#     files = open(User).read()
# except:
#     print("Error, File Not Found!!!")
#     quit()
# print(len(files))
# def new_func(file):
#     my_reader = open(file)
#     data = my_reader.read()
#     for line in data:
#         ad = data.find('@')
#         space = data.find(' ',ad)
#         print(data[ad:space])
# new_func('new.txt')
# def copier(f):
#     file = open(f)
#     reader = file.read()
#     splitter = reader.split('\n')
#     empty = []
#     data = empty.append(reader)
#     count = 0
#     for entry in empty:
#         print(entry)
# copier('new.txt')
# Empty = {}
# copied = []
# all = []
# names = ['Hasnain','Amjad','ali','tariq','tariq']
# n = 1
# for name in names:
#     Empty[name] = n
#     n +=1
# print(Empty)
# Empty = {}
# copied = []
# all = []
# names = ['Hasnain','Amjad','ali','tariq','tariq']
# for name in names :
#     if name not in copied:
#         copied.append(name)
#     else:
#         all.append(name)
# print(copied)
# print(all)
#
#
# def new():
#     your = input('Enter your file name :')
#     word = input('Type a word or alphabet you want to locate : ')
#     file = open(your).read()
#     data = 0
#     for char in file:
#         if char == word:
#             data += 1
#     print(data)
#
#
# new()
# def my(f):
#     f = open(f).read().strip().split()
#     empty = {}
#     for word in f:
#         empty[word] = empty.get(word, 0) + 1
#     s = sorted([(v, k) for k, v in empty.items()], reverse=True)
#     for i in s:
#         print(i)
#
#
# my('new.txt')
# never = 'From user@domain.com sat 9:00 AM at 16 FEb,2003'
#
# file = open('New.txt').read()
# nri = re.findall(r'.*@([^ ]*)\n$', file)
# print(nri)
# import socket
# new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# new.connect(('http://fismed.ciemat.es', 8080))
# cmd = 'GET http://fismed.ciemat.es/GAMOS/download/GAMOS.6.0.0/uncompiled/geant4.10.04.p02.gamos
# /ReleaseNotes/Patch4.9.1-1.txt HTTP/1.0\n\n'.encode()
# new.send(cmd)
# while True:
#     data = new.recv(512)
#     if (len(data)) < 1:
#         break
#     print(data.decode())
# new.close()
# import socket
# soc = socket.socket()
# print('Socket Created Successfully')
# soc.bind(('localhost', 8888))
# print('Socket Bound Successfully')
# soc.listen(5)
# print('Listening')
# while True:
#     ctr, address = soc.accept()
#     print('Accepted : ', address)
#     ctr.send(bytes('Welcome Here ', 'utf-8'))
#     name = ctr.recv(1024).decode()
#     print(name)
#     ctr.close()
#     while True:
#         ctr, address = soc.accept()
#         y = ctr.recv(1024).decode()
#         print(y)
