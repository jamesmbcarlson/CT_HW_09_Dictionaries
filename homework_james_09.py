# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 3 Lesson 1 Assignment: Dictionaries

print("\n=== 1. Real-World Python Dictionary Applications ===\n")

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# add beverages
restaurant_menu.update({"Beverages": {"Beer" : 6.99, "Coffee": 3.49}})
print(restaurant_menu)
# update price of steak
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)
# remove bruschetta
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)
print()



print("\n=== 2. Advanced Data Handling with Python ===\n")

# Task 1 - Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "booked", "customer": "Ororo Munroe"},
    "201": {"status": "available", "customer": ""},
    "202": {"status": "booked", "customer": "Scott Summers"},
    "203": {"status": "available", "customer": ""}
}

# books a room and assigns it to customer
def book_room(room, customer):
    if hotel_rooms[room]["status"] == "available":
        hotel_rooms[room] = {"status": "booked", "customer": customer }
        print(f"Room {room} has been booked by {customer}.")
    else:
        print(f"Room {room} is unavailable. Sorry for any inconvenience to {customer}!")

# checks out customer by name
def checkout_customer(customer):
    for room in hotel_rooms:
        if customer in hotel_rooms[room]["customer"]:
            hotel_rooms[room] = {"status": "available", "customer": ""}
            print(f"{customer} is checking out. Room {room} has become available.")
            return
    print(f"{customer} does not appear to be staying at this hotel!")

# prints all rooms, their statuses, and their occupants
def display_all_rooms():
    for room in hotel_rooms:
        print(f"Room {room} is {hotel_rooms[room]["status"]}.", end=" ")
        if hotel_rooms[room]["status"] == "booked":
            print(f"It has been booked by {hotel_rooms[room]["customer"]}.")
        else:
            print()

# test cases
display_all_rooms()
book_room("101", "Charles Xavier")
book_room("101", "Erik Lehnsherr")
book_room("203", "Erik Lehnsherr")
display_all_rooms()
checkout_customer("John Doe")
checkout_customer("James Howlett")
display_all_rooms()
print()



# Task 2: E-commerce Product Search Feature

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20},
    "3": {"name": "shirt", "category": "Clothing", "price": 18},
    "4": {"name": "New Era Avengers Classic 59FIFTY Fitted Cap", "category": "Clothing", "price": 47.99},
    "5": {"name": "SHIRT", "category": "Clothing", "price": 24},
    "6": {"name": "Wireless Mouse", "category": "Electronics", "price": 30}
}

def search_by_name(name):
    # search for products of specified name with case insensitivity and add to list same_name
    same_name = []
    for product in products:
        if products[product]["name"].casefold() == name.casefold():
            same_name.append(products[product])

    # return list if any products are found        
    if same_name == []:
        return f"No products with name \"{name}\" found."
    else:
        print(f"Found the following items with name \"{name}\":")
        return same_name

# test cases
print(search_by_name("shirt"))
print(search_by_name("SHIRT"))
print(search_by_name("New Era Avengers Classic 59FIFTY Fitted Cap"))
print(search_by_name("LEGO® DC Batman Batcave – Shadow Box (76252)"))
print()



print("\n=== 3. Python Programming Challenges for Customer Service Data Handling ===\n")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
    "Ticket003": {"Customer": "Roy", "Issue": "Internet outage", "Status": "open"},
    "Ticket004": {"Customer": "Moss", "Issue": "Computer virus", "Status": "closed"}
}

def open_new_ticket(customer ="", issue ="", status ="open"):
    # format key
    key = "Ticket" + str(len(service_tickets)+1).zfill(3)

    # get input for new ticket if parameters are not specified
    if customer == "":
        customer = input("What is the name of the customer for this new ticket? ")
    if issue == "":
        issue = input("What is the issue the customer is experiencing? ")
    print()

    # add new ticket to dictionary
    service_tickets.update({key : {"Customer": customer, "Issue": issue, "Status": status}})


# sets given ticket to the given status
def update_ticket(ticket, open_or_close):
    service_tickets[ticket]["Status"] = open_or_close

# display all tickets unless otherwise specified by status
def display_tickets(status ="all"):
    for key, value in service_tickets.items():
        if status == "all":
            print(f"{key} : {value}")
        elif value["Status"] == status:
            print(f"{key} : {value}")

# test cases
open_new_ticket()
open_new_ticket("Arin", "Spilled soup on keyboard", "closed")
display_tickets()
print()
update_ticket("Ticket003", "closed")
print("Displaying All: ")
display_tickets()
print("\nDisplaying Open Tickets: ")
display_tickets("open")
print("\nDisplaying Closed Tickets: ")
display_tickets("closed")
print()



print("\n=== 4. Python Essentials for Business Analytics ===\n")

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# create deep copy
weekly_sales_copy = copy.deepcopy(weekly_sales)

# update sales figure in copied data
weekly_sales_copy["Week 2"]["Electronics"] = 18000

# prints for verification
print(weekly_sales)
print(weekly_sales_copy)