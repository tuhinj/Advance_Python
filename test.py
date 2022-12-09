# n = int(input())
# if (n % 2 == 0 and 1 < n >=5):
#     print(n + ":","Not Weird")
# elif (n % 2 != 0 and 5 <= n >=20):
#     print("Weird")
# else:
#     print(n + ":","Not Weird")
####################################################
# line1 = input().split(" ")
# line2 = input().split(" ")
# cod1, num1, price1 = line1
# cod2, num2, price2 = line2
# total = (int(num1) * float(price1)) + (int(num2) * float(price2))
# print(f'VALOR A PAGAR: R$ {total:.2f}')        
#######################################################3
# print(ord('B')) # "ord()" for knowing askii value
# print(chr(68)) # "chr()" for knowing askii character

# a = input().split(" ")

# print(a)
# print(type(a))
#######################################################33
# LZW Encoder
# Name: Aditya Gupta
# ID: 800966229
# ITCS 6114

# import sys
# from sys import argv
# from struct import *

# # taking the input file and the number of bits from command line
# # defining the maximum table size
# # opening the input file
# # reading the input file and storing the file data into data variable
# input_file, n = argv[1:]                
# maximum_table_size = pow(2,int(n))      
# file = open(input_file)                 
# data = file.read()                      

# # Building and initializing the dictionary.
# dictionary_size = 256                   
# dictionary = {chr(i): i for i in range(dictionary_size)}    
# string = ""             # String is null.
# compressed_data = []    # variable to store the compressed data.

# # iterating through the input symbols.
# # LZW Compression algorithm
# for symbol in data:                     
#     string_plus_symbol = string + symbol # get input symbol.
#     if string_plus_symbol in dictionary: 
#         string = string_plus_symbol
#     else:
#         compressed_data.append(dictionary[string])
#         if(len(dictionary) <= maximum_table_size):
#             dictionary[string_plus_symbol] = dictionary_size
#             dictionary_size += 1
#         string = symbol

# if string in dictionary:
#     compressed_data.append(dictionary[string])

# # storing the compressed string into a file (byte-wise).
# out = input_file.split(".")[0]
# output_file = open(out + ".lzw", "wb")
# for data in compressed_data:
#     output_file.write(pack('>H',int(data)))
    
# output_file.close()
# file.close()

# name = "Maynuddin tuhin joy"

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.split(" "))
# print(name.strip())
# print(name[:9])
# print(name[10:15])
# print(name[10:])
# print(name[-3:])

# names = ['Tuhin', 'Joy', 'Maynuddin', 'Pronoy']
# name2 = [1, 2, 6, 5, 3, 4]

# names.extend(name2)
# print(names)

# names.append("Maliha")
# print(names)

# names.pop()
# print(names)

# names.insert(3, "Zihad")
# print(names)

# names.remove("Pronoy")
# print(names)

def print_name(name):
    print(f"Is your name {name}")
    
print_name("Maynuddin")


def print_dic(**valkey):
    print("The dic:",valkey)

print_dic(name="Tuhin",age="")