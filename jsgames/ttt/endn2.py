x = ['r', 'u', 't', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't']
print ''.join(x)
 
print x.index('r')

print x[1] 

print 'z' in x

y = x.extend('n')

print y

def subit(n):
    return n - 1
print 'r' not in x

def addit(lst):
    if lst==[]: return []
    else:
        first = lst[0]
        rest = lst[1:]
        return [subit(first)] + addit(rest)
    
    
    
print addit([1, 2, 3])
print len(x)


    