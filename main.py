# Function for taking user input
def cardinf():
    card_no = int(input("Enter your card number: "))
    return card_no

# Getting the number of digits entered
def count(numb):
    count = 0
    while numb > 0:
        numb = numb//10
        count += 1
    return count

# While loop to make sure card number is proper
card_no = None
while type(card_no) != int or count(card_no) != 16:
    try:
        card_no = cardinf()
        if count(card_no) != 16:
            print("Card number must be 16 digits.")
    except ValueError as e:
        print("Please input numbers only. No spaces or any other characters allowed.")

print("The card number you enetered is "+str(card_no))

# Reversing card number
card_no = str(card_no)
cardrev = card_no[::-1]

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Adding all digits in odd places from right to left
for i in cardrev[::2]:
    sum_odd_digits += int(i)

# Addng all digits in even places
for i in cardrev[1::2]:
    i = int(i)*2
    if len(str(i)) > 1:
        sum_even_digits += ((i % 10) + 1)
    else:
        sum_even_digits += i

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("Your credit card number is valid.")
else:
    print("The credit card number you entered is invalid.")
