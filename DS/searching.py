def linear_search(array,key):
    if key in array:
        for i in range(len(array)):
            if array[i]==key:
                print("Element Found at: ",i,"Position")
    else:
        print("Element is not present in array")


def binary_search(array,key):
    if key in array:
        array=sorted(array)
        print(array)
        LB=0
        UB=len(array)-1
        mid = (LB+UB)//2
        while array[mid]!=key:
            if key>array[mid]:
                LB=mid+1
                mid = (LB+UB)//2
            else:
                UB=mid-1
                mid = (LB+UB)//2
        print("Element is present at: ",mid," Position")
    else:
        print("Element is not present in array")

data = [10,20,50,30,60,70]
linear_search(data,50)
binary_search(data,50)