# grocery.py

# Dummy grocery category with items and prices
GROCERY_ITEMS = [
    {"name": "Basmati Rice 5kg", "price": 649},
    {"name": "Sunflower Oil 1L", "price": 159},
    {"name": "Toor Dal 1kg", "price": 149},
    {"name": "Green Tea 100pcs", "price": 299},
    {"name": "Wheat Flour 10kg", "price": 499},
    {"name": "Sugar 5kg", "price": 275},
    {"name": "Milk 1L", "price": 55},
]

# Function to display groceries
def display_grocery_items():
    print("=== Grocery Category ===")
    for i, item in enumerate(GROCERY_ITEMS, start=1):
        print(f"{i}. {item['name']} - ₹{item['price']}")

# Function to search item by name
def search_grocery_item(query):
    results = [item for item in GROCERY_ITEMS if query.lower() in item["name"].lower()]
    if results:
        print(f"\nSearch results for '{query}':")
        for item in results:
            print(f"- {item['name']} : ₹{item['price']}")
    else:
        print(f"\nNo items found for '{query}'.")

if __name__ == "__main__":
    display_grocery_items()
    # Example search
    search_grocery_item("rice")
