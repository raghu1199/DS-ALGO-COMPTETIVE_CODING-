def swap(v1,v2):
    temp=v2
    v2=v1
    v1=v2

def selectionsort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if (arr[j] < arr[min_index]):
                min_index=j
        
        if(min_index!=i):
            arr[i],arr[min_index]=arr[min_index],arr[i]
            #swap(arr[i],arr[min_index]) wont work in python no pointer concept

arr=[2,8,1,6,7,4,5]
selectionsort(arr)
print(arr)
