def is_leap(year):
    leap = False
    notleap=True
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return notleap
            else:
                return leap
        else:
            return notleap
    return leap