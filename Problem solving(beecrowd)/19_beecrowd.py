'''  
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
'''
N = int(input())
H = int(N/(60*60))
h = int(N%(60*60))
M = int(h/60)
S = int(h%60)
print(f"{H:.0f}:{M:.0f}:{S:.0f}")