nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums)
nums.remove(3) #используем , если заранее известно значение объекта для удаления
print(nums)
#nums.remove(5) возникнет ошибка

nums.pop()
print(nums)

res = nums.pop(2)
print(nums)
print("Был удален элемент со значением " + str(res))