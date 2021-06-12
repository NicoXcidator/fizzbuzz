#generate number from 1 to 100
num_list = list(range(1,101))
for i in range(len(num_list)):
#replace the numbers divisible by 15 as fizzbuzz
  if num_list[i] % 3 == 0 and num_list[i] % 5 == 0:
    num_list[i] = "fizzbuzz"
#replace the numbers divisible by 5 as buzz
  elif num_list[i] % 5 == 0:
    num_list[i] = "buzz"
#replace the numbers divisible by 3 as fizz
  elif num_list[i] % 3 ==0:
    num_list[i] = "fizz"
print(num_list)