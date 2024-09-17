# Freight Cost Calculator Joseph Rydberg 9/16/24

def weight_conversion(weight):
    shippingCost = 0.0

    if weight <= 2:
        shippingCost = 1.50
    elif weight > 2 and weight <= 6:
        shippingCost = 3.00
    elif weight > 6 and weight <= 10:
        shippingCost = 4.00
    elif weight > 10:
        shippingCost = 4.75
    
    return shippingCost

if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))