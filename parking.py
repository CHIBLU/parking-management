
capacity = 5
parking_lot = [None] * capacity

def park(car):
    if None in parking_lot:
        slot = parking_lot.index(None)
        parking_lot[slot] = car
        print(f"Car {car} parked at slot {slot+1}.")
    else:
        print("Parking lot is full.")

def unpark(slot):
Here's a simple Python code for parking management without using classes:

```python
capacity = 5
parking_lot = [None] * capacity

def park(car):
    if None in parking_lot:
        slot = parking_lot.index(None)
        parking_lot[slot] = car
        print(f"Car {car} parked at slot {slot+1}.")
    else:
        print("Parking lot is full.")

def unpark(slot):
    if 1 <= slot <= capacity:
        if parking_lot[slot-1] is not None:
            car = parking_lot[slot-1]
            parking_lot[slot-1] = None
            print(f"Car {car} removed from slot {slot}.")
        else:
            print(f"Slot {slot} is already empty.")
    else:
        print("Invalid slot number.")

def display():
    print("Parking lot status:")
    for i, car in enumerate(parking_lot):
        if car is not None:
            print(f"Slot {i+1}: Car {car}")
        else:
            print(f"Slot {i+1}: Empty")

# Parking cars
park("ABC123")
park("XYZ789")

# Displaying parking lot status
print("After parking:")
display()

# Unparking a car
unpark(1)

# Displaying parking lot status again
print("After unparking:")
display()
```

This code achieves the same functionality as the previous example but without using classes. It defines functions for parking, unparking, and displaying the status of the parking lot and uses a list to represent the parking slots.    if 1 <= slot <= capacity:
        if parking_lot[slot-1] is not None:
            car = parking_lot[slot-1]
            parking_lot[slot-1] = None
            print(f"Car {car} removed from slot {slot}.")
        else:
            print(f"Slot {slot} is already empty.")
    else:
        print("Invalid slot number.")

def display():
    print("Parking lot status:")
    for i, car in enumerate(parking_lot):
        if car is not None:
            print(f"Slot {i+1}: Car {car}")
        else:
            print(f"Slot {i+1}: Empty")

# Parking cars
park("ABC123")
park("XYZ789")

# Displaying parking lot status
print("After parking:")
display()

# Unparking a car
unpark(1)

# Displaying parking lot status again
print("After unparking:")
display()
