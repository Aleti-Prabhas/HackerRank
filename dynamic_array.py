N, Q = map( int, input().split() )
lastans = 0

Seqs = [ [] for _ in range( N ) ]

for _ in range( Q ):
    t, x, y = map( int, input().split() )
    if t == 1:
        Seqs[ ( x ^ lastans ) % N ].append( y )
    elif t == 2:
        arr = Seqs[ ( x ^ lastans ) % N ]
        val = arr[ y % len(arr) ]
        print( val )
        lastans = val