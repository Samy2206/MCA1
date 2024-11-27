def linear_search(array,key):
    if key in array:
        for i in range(len(array)):
            if array[i]==key:
                print("Element Found at: ",i,"Position")
    else:
        print("Element is not present in array")


data = [10,20,50,30,60,70]
linear_search(data,10)