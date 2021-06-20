""" 

Code is in Python 

This program calculates the average of sub arrays 

Example: 

Array [ 1,3,2,6,-1,4,1,8,2] 

Size of sub array, K = 5, can be any value... 

Result : First : 1+3+2+6-1/5 , 3+2+6-1+4/5 , etc.. 

Use SlidingWindow Pattern to solve this Problem..  

O(n) is the time complexity of this program 

"""

def avg_of_sub_arrays(Item,k): 

    sum = 0.0 

    windowStart = 0 

    for x in range(0,len(Item)): 

        #Now Iterate the Item array , get all elements add it,  

        sum+= Item[x] 

        avg = 0.0 

        if x >= k - 1: 

            avg = sum / k 

            sum-= Item[windowStart] 

            print("{0} {1}".format(avg," ")) 

            #print(avg) 

            windowStart+= 1 

 
 

def main(): 

    Items = [ 1,3,2,6,-1,4,1,8,2] 

    k = 5 

    avg_of_sub_arrays(Items,k) 

 
 

if __name__=="__main__": 

    main() 

 
 
