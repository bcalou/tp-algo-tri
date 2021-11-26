import time
start: float = time.time()
import random


def tri_selection(tri):
   for i in range(len(tri)):
      # Find min
       min = i
       for j in range(i+1, len(tri)):
           if tri[min] > tri[j]:
               min = j 
                
       tmp = tri[i]
       tri[i] = tri[min]
       tri[min] = tmp
   return tri

# Test code
tri = [random.randint(0, 100) for i in range(int('9_000'))]
tri_selection(tri)
print ("Le tableau trié est:")
for i in range(len(tri)):
    print ("%d" %tri[i])

end: float = time.time()
print("Temps écoulé :", end - start)