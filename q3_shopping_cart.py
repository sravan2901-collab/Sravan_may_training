# ============================================================
# PART A — Spot the Bug
# ============================================================

def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart

# Predicted output with explanation:
# add_item_buggy("apple")   -> ["apple"]
# add_item_buggy("banana")  -> ["apple", "banana"]   ← BUG: same list reused!
# add_item_buggy("milk", cart=["bread"]) -> ["bread", "milk"]   ← new list passed explicitly
# add_item_buggy("eggs")   -> ["apple", "banana", "eggs"]  ← BUG: still the original shared list!


print("=== PART A — Buggy Output ===")
print(add_item_buggy("apple"))
print(add_item_buggy("banana"))
print(add_item_buggy("milk", cart=["bread"]))
print(add_item_buggy("eggs"))


# ============================================================
# PART B — Fix It
# ============================================================
def add_item(item, cart=None):
    # Use None as the sentinel; create a fresh list inside the function
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("\n=== PART B — Fixed Output ===")
print(add_item("apple"))          # ['apple']
print(add_item("banana"))         # ['banana']  — fresh list every time
print(add_item("milk", cart=["bread"]))  # ['bread', 'milk']
print(add_item("eggs"))           # ['eggs']  — fresh list again


# ============================================================
# PART C — Build the Cart
# ============================================================

def create_cart(owner, discount=0):
    """
    discount=0 is safe because 0 is an integer — immutable.
    A new dict with a fresh [] is created each time this function runs,
    so each customer gets their own independent cart.
    """
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})
    print(f"  Added to {cart['owner']}'s cart: {qty}x {name} @ ₹{price:.2f}")


def update_price(price_tuple, new_price):
    """
    Tuples are IMMUTABLE — you cannot change an element after creation.
    The line below raises TypeError: 'tuple' object does not support item assignment.
    We catch it here to demonstrate the concept.
    """
    try:
        price_tuple[0] = new_price      # This will raise TypeError
    except TypeError as e:
        print(f"  Cannot modify tuple: {e}")
        print("  → Tuples are immutable: once created, their elements cannot be changed.")


def calculate_total(cart):
    subtotal = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = subtotal * (cart["discount"] / 100)
    total = subtotal - discount_amount
    return total


# ---------- Demonstration ----------
print("\n=== PART C — Shopping Cart Demo ===")

# Customer 1
cart1 = create_cart("Sravan", discount=10)
add_to_cart(cart1, "Notebook", 120.0, qty=3)
add_to_cart(cart1, "Pen", 20.0, qty=5)
add_to_cart(cart1, "Eraser", 10.0)

# Customer 2
cart2 = create_cart("Aarav", discount=5)
add_to_cart(cart2, "Backpack", 850.0)
add_to_cart(cart2, "Water Bottle", 250.0, qty=2)

# Prove carts are independent
print(f"\n  {cart1['owner']}'s items: {[i['name'] for i in cart1['items']]}")
print(f"  {cart2['owner']}'s items: {[i['name'] for i in cart2['items']]}")

# Totals
total1 = calculate_total(cart1)
total2 = calculate_total(cart2)
print(f"\n  {cart1['owner']}'s total (after {cart1['discount']}% discount): ₹{total1:.2f}")
print(f"  {cart2['owner']}'s total (after {cart2['discount']}% discount): ₹{total2:.2f}")

# Tuple immutability demo
print("\n  --- Tuple Immutability Demo ---")
price_info = (120.0, "INR")
print(f"  Original price tuple: {price_info}")
update_price(price_info, 150.0)


# ============================================================
# DISCUSSION (as comments)
# ============================================================

# Q1: Why is discount=0 safe but cart=[] dangerous?
#   → 0 is an integer (immutable). Each call gets a new binding if you rebind
#     the variable, and integers can never be mutated in place. By contrast,
#     a list is mutable — Python creates it ONCE when the function is defined,
#     and every call that doesn't pass its own list shares the SAME object.
#     Mutations (append, remove, etc.) persist across calls, which is almost
#     never what you want.

# Q2: What is the difference between rebinding and mutating?
#   → Rebinding: making a variable name point to a different object.
#       e.g.  x = 5; x = 10   — x now points to a new int object.
#   → Mutating: changing the CONTENTS of the object the variable points to.
#       e.g.  my_list = [1,2]; my_list.append(3)  — same object, new content.
#     Rebinding never affects other variables that still point to the old object.
#     Mutating DOES affect all variables that reference the same object.

# Q3: Which of these are mutable?
#   Mutable   : list ✓, dict ✓, set ✓
#   Immutable : tuple ✗, str ✗, int ✗

# Q4: When you pass a list into a function and modify it, do changes reflect outside?
#   → YES. Python passes objects by reference (technically "pass-by-object-reference").
#     The function receives a reference to the SAME list object. Any in-place
#     mutations (append, pop, sort, etc.) are visible to the caller because both
#     the caller and the function are looking at the same object in memory.
#     Rebinding the parameter inside the function (e.g., cart = []) does NOT
#     affect the caller's variable — it only makes the local name point elsewhere.
