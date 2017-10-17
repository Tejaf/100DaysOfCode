'''
    Lazy day:
        convert time formated in 12hrs to 24hrs
'''

def timeConversion(st):
    h,m,s = map(int, st[:-2].split(':'))

    h = h%12 + ((st[-2:]).upper() == 'PM')*12

    return ('%02d:%02d:%02d' % (h, m, s))

print timeConversion('08:12:49PM')