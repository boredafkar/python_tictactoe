L=[['A','B','C'],['D','E','F'],['G','H','I']]
def initiate(l):
    for i in range(3):
         for j in range(3):
             print l[i][j],
         print
def index(l,e):
    u=[]
    for i in l:
        if e in i:
            u.append(l.index(i))
            u.append(i.index(e))
    return u

print '!!!! WELCOME TO TIC TAC TOE !!!!'
p=raw_input('Please Enter Password   = ')
if p=='abc':
    print ' Password accepted'
    p1=raw_input('Player 1 ! Please enter your name  = ')
    p2=raw_input('Player 2 ! Please enter your name  = ')
    print p1 ,'is X and ',p2,'is O'
    print 'ALL THE BEST',p1,'&',p2
    print p1,'plays first'
    print
    initiate(L)
    for i in range(4):
        print p1,'Make your move! Enter the alphabet of your choice'
        m1=raw_input('')
        ans=index(L,m1)
        L[ans[0]][ans[1]]='X'
        print
        initiate(L)
        print
        print p2, 'Make your move! Enter the alphabet of your choice'
        m2=raw_input('')
        ans1=index(L,m2)
        L[ans1[0]][ans1[1]]='O'
        print
        initiate(L)
else:
    print 'Wrong password! Try again'
w=input('Press any key to exit')
