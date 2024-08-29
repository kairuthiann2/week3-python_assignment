def calculate_discount(price, discount_percent):

    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying th discount 
        final_price = price - discount_amount
        return final_price
    else: 
        # Return the original price if the discount is less than 20%
        return price
    

# prompt the user to enter the original price
original_price = float(input("Enter the original price of the Rice: "))
# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price == original_price:
    print(f"No discount applied. The price is: ${original_price:.2f}")
else:
    print(f"After applying the discount, the final price of the rice is: ${final_price:.2f}")


