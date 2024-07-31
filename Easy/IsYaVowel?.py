"""
The Vowels are a, e, i, o and u, and possibly y. People disagree on whether y is a vowel or not. Unfortunately for you, you have been tasked with counting the number of vowels in a word. You’ll have to count how many vowels there are assuming y is a vowel, and assuming y is not.
Input

The single line of input contains a string of at least one and at most

lowercase letters.
Output

Output two space-separated integers. The first is the number of vowels assuming y is not a vowel, the second is the number of vowels assuming y is a vowel.
"""

txt=str(input())
total=0
vowels={'a','e','o','u','y','i'}
for i in txt:
    if i in vowels:
        total+=1
total1=0
for i in txt:
    if i in vowels and i!='y':
        total1+=1
print(f"{total1} {total}")
