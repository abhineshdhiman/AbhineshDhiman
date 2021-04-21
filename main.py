# 2.1 Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇


firstNumber = str(two_digit_number[0]);
secondNumber = str(two_digit_number[1]);
sumDigits = int(firstNumber) + int(secondNumber);
print("The sum of the two digit number is:" + str(sumDigits));


