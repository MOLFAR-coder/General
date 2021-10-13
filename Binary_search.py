class Binary_search:
  def __init__(array):
    self.array = array
  def search(self,number):
    lo = 0
    hi = len(self.array)-1
    mid = (lo+hi)//2
    while mid!=number:
      if mid<number:
        lo = mid
        mid = (lo+hi)//2
        continue
      else:
        hi = mid
        mid = (lo+hi)//2
        continue
    return self.array.index(mid)    
