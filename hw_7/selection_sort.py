def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

list = [5,2,8,1,2,2,2,3,6,9,0,4]
selection_sort(list)

print(list)
