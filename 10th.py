'''name="shahid"
vowel="aeiou"
for i in name:
    if i in vowel:
         print(i)'''

names="balaji srinivasan"
print(names)
print(names[:])
print(names[::-3])
print(names[::-2])
sep='-'.join(names[::2])
print(sep)
for i in range(0,len(names)):
    if(i%3==0 and i!=0):
        print('-',end='')
    else:
        print(names[i],end='')