import multiprocessing


def square(a,b):
     return a*b
if __name__ == "__main__":
      with multiprocessing.Pool(processes=2) as pool:
            result= pool.starmap(square,[(1,2),(3,4),(5,6)])

      print(result)      
            
            
      
      
