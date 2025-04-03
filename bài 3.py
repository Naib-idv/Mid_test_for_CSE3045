def bubble_sort_tang_dan(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Hãy nhập dãy các số bạn muốn sắp xếp, cách nhau bằng khoảng trắng: ").split()))
print("Trước khi sắp xếp:", arr)
bubble_sort_tang_dan(arr)
print("Sau khi sắp xếp tăng dần:", arr)
def bubble_sort_giam_dan(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubble_sort_giam_dan(arr)
print("Sau khi sắp xếp giảm dần:", arr)
