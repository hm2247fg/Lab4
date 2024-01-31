def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    if len(item_prices) > 0:  # added to avoid errors if you try to find the minimum value in an empty list
        min_value = item_prices[0]  # initializes the variable min_value with the first element of the list
        for i in item_prices:  # for loop that iterates ove each element i in the list item_prices
            if i < min_value:  # if statement that checks if i is smaller than the current minimum value
                min_value = i  # if current value is smaller, it updates min value with the smaller amount

        return min_value


if __name__ == '__main__':
    main()
