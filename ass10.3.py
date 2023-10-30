# Write a program to print currency denominations.

amt=int(input())
ttc=0
fhc=0
thc=0
oh=0
ft=0
tw=0
ten=0
five=0
two=0
one=0
while amt>=2000:
    ttc=ttc+1
    amt=amt-2000
while amt>=500:
    fhc=fhc+1
    amt=amt-500
while amt>=200:
    thc=thc+1
    amt=amt-200
while amt>=100:
    oh=oh+1
    amt=amt-100
while amt>=50:
    ft=ft+1
    amt=amt-50
while amt>=20:
    tw=tw+1
    amt=amt-20
while amt>=10:
    ten=ten+1
    amt=amt-10
while amt>=5:
    five=five+1
    amt=amt-5
while amt>=2:
    two=two+1
    amt=amt-2
while amt>=1:
    one=one+1
    amt=amt-1
if ttc>0:
    print('2000:'+str(ttc))
if fhc>0:
    print('500:'+str(fhc))
if thc>0:
    print('200:'+str(thc))
if oh>0:
    print('100:'+str(oh))
if ft>0:
    print('50:'+str(ft))
if tw>0:
    print('20:'+str(tw))
if ten>0:
    print('10:'+str(ten))
if five>0:
    print('5:'+str(five))
if two>0:
    print('2:'+str(two))
if one>0:
    print('1:'+str(one))

