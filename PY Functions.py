def sum_even(n):
    sum = 0
    if n%2 == 1:
        n -=1

    for i in range(n):
        if not n % 2:
            sum += i
    return sum


print(sum_even(6))

#------------------------------

def calculate_bmi(w, h):
    return w/(h*h)

result = calculate_bmi(10, 2)
print("the bmi:", result)

#------------------------------

def count_down_up(n):
    for i in range (n, 0, -1):
       print(i, ",",  end= ' ')
    for i in range (2, n + 1):
       print(i, ",",  end= ' ')
   
        

count_down_up(3)