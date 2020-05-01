
def print_payment_discrepancies(path, melon_cost=1.00):
  """Given path and melon cost, print report showing customers with payments discrepant from amount due based on purchase

  Opens the customer-orders file at [path], processes each line, and prints all customers with discrepancies into file."""

  #open [path] file to parse through lines
  file = open(path)

  #loop through each line
  for line in file:
      #remove blank spaces on the right
      line = line.rstrip()
      #split each line into a list separated by a "|""
      words = line.split("|")

      #assign variables to list items corresponding to customer name, melons, and amount paid
      customer_name = words[1]
      melons = float(words[2])
      amount_paid = float(words[3])
      #calculate amount due for each customer
      amount_due = melons * melon_cost
      variance = amount_due - amount_paid

      #if there is a variance, print out a line indicating customer name, what they paid, and the variance
      if amount_due != amount_paid:
          print(f"{customer_name} paid ${amount_paid:.2f},",
                f"original amount due ${amount_due:.2f},"
                f"remaining balance ${variance:.2f}"
                )
  #close the file        
  file.close()

#call the function
print_payment_discrepancies("customer-orders.txt")

