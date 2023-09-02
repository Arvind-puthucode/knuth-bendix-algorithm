how are terms modelled using my implementation
eg1 :
-a+a looks like 
T+(T-(Va), Va)

eg2 :
(--a+-a)+a looks like
T+(T+(T-(T-(Va)), T-(Va)), Va)

eg3: (x+y)+z
expression 3 T+(T+(Vx, Vy), Vz)

eg4:x+(y+z)
expression 4 T+(Vx, T+(Vy, Vz))

Complexity of expression 3: 2

Complexity of expression 4: 1

Expression 4 is simpler.