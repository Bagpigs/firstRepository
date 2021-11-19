v = 1234

# zahl der stellen von v, zerlegung in array von stellen

def recfunc(score,v):

    if v == 0:
        return score
    else:
        v_array = str(v)

        p = len(v_array) - 1
        p0 = v//(10**p)
        #print(p)
        #print(p0)

        if p == 0:
            score += 1

        elif p0 >= 2:
            score += recfunc(0,10**p-1)*p0 + 10**p


        elif p0 == 1:
            score += recfunc(0,10**p-1) + 1 + int(v_array[1:])

        elif p0 == 0:
            print('p0=0')
        #print(score)
        return recfunc(score,v-(10**p)*p0)

print(recfunc(0,v))
