def linear_search(array,key):
    for i in range(len(array)):
        if array[i]==key:
            return("Element Found at: ",i,"Position")
    return("Element is not present in array")


def binary_search(array,key):
        array=sorted(array)
        LB=0
        UB=len(array)-1
        while LB<=UB:
             mid = (LB+UB)//2
             if array[mid]==key:
                  return("Element is at:",mid,"Position")
             elif array[mid]>key:
                  UB=mid-1
             else:
                  LB=mid+1
        return("Element not found")

def search_rec(data,key,l,h):
     if l > h:  # Base case for when the element is not found
        return "Element not found"
     mid=(l+h)//2
     if data[mid]==key:
          return ("Element is at:",mid,"Position")
     elif data[mid]>key:
          return search_rec(data,key,l,mid-1)
     elif data[mid]<key:
          return search_rec(data,key,mid+1,h)

def bin_search_rec(data,key):
     data=sorted(data)
     l=0
     h=len(data)-1
     return search_rec(data,key,l,h)

data = [10,20,50,30,60,70]
print(linear_search(data,50))
print(binary_search(data,20))
print(bin_search_rec(data,50))