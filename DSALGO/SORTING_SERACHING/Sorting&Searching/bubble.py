def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(i,":swap occres")

#arr=[1,10,2,2,20,5]

arr=[3,44,38,5,2,4]
bubblesort(arr)
print(arr)