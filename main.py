# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# PART 1: Counters for the price bands and the whole day
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0

billing = True

# PART 2: Serve one customer each time this loop repeats
while billing:
    customer_name = input("Enter the customer's name: ")
    item_count = int(input("How many different items are they buying? "))

    # PART 3: Do not start billing if the item count is invalid
    if item_count <= 0:
        print("Please enter a number of items greater than 0.\n")
        continue

    # PART 4: Get each item for this customer
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        print("\nItem", item_number)
        item_name = input("Enter the item name: ")
        price = int(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))

        # PART 5: Check the price and quantity, then calculate the item total
        if price <= 0 or quantity <= 0:
            print("Price and quantity must both be greater than 0.")
            continue

        item_total = price * quantity
        print(item_name + ":", quantity, "x", price, "=", item_total)

        customer_total = customer_total + item_total

        # Add the quantity to the matching price band
        if quantity < 50:
            low_price_items = low_price_items + quantity
        elif quantity <= 100:
            medium_price_items = medium_price_items + quantity
        else:
            high_price_items = high_price_items + quantity

        item_number = item_number + 1

    # PART 6: Finish this customer's bill
    customers_served = customers_served + 1
    total_sales = total_sales + customer_total
    print("\n" + customer_name + "'s total is", customer_total)

    next_customer = input("Next customer? (yes/no): ").strip().lower()
    if next_customer != "yes":
        billing = False

# PART 7: Print a star report for each price band
print("\n=== Item Quantity Report ===")

for band_name, item_count in [
    ("Low (under 50)", low_price_items),
    ("Medium (50 to 100)", medium_price_items),
    ("High (over 100)", high_price_items),
]:
    print(band_name + ": ", end="")
    for item in range(item_count):
        print("*", end="")
    print()

print("\nCustomers served:", customers_served)
print("Total sales:", total_sales)
