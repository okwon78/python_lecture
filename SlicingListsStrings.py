my_list = [0, 1, 2, 3, 4, 5, 6, 7]

print(my_list[0])
print(my_list[5])
print(my_list[-1])
print(my_list[-5])

print(my_list[0:-1])    # [0, 1, 2, 3, 4, 5, 6]
print(my_list[3:-3])    #[3, 4]
print(my_list[0:-1:2])  # [0, 2, 4, 6]
print(my_list[0:-1:-1]) # []
print(my_list[-1:0:-1]) # [7, 6, 5, 4, 3, 2, 1]
print(my_list[::-1])    # [7, 6, 5, 4, 3, 2, 1, 0]
print(my_list[::1])     # [0, 1, 2, 3, 4, 5, 6, 7]

url = "http://www.naver.com"

print(url)
print(url[::-1])
print(url[-4:])
print(url[7:])

