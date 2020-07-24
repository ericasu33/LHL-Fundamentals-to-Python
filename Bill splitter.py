subtotal = float(input("Bill Total: "))
tipPercentage = int(input("Tip Percentage: "))
contributors = int(input("Number of People: "))

tax_rate = 0.14
tax = round(subtotal*tax_rate,2)
total = round(subtotal + tax,2)

tips = total*tipPercentage/100

overall_total = round(total+tips,2)

total_per_person = round(overall_total/contributors,2)

print ("The total before tips is:$", total)
print ("The final total including tips is:$", overall_total)
print("The bill per person comes to:$", total_per_person)


