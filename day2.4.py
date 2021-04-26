billAmount = int(input("Enter Your Bill Amount:\n"))
tipPrctge = int(input("Enter the Tip Percentage you would like to give:\n"))
personsCount = int(input("Enter the numbers of Person to split Bill:\n"))
tipAmt = billAmount * tipPrctge / 100
totalAmt = billAmount + tipAmt
splitAmt = totalAmt / personsCount

print(f"Your Total Amount After Adding tip is :\n {totalAmt}\nYour Splitted Bill Per Person is :\n{splitAmt:.2f}")