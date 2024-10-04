#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self._discount = discount
    self._total = 0
    self._quantity = 0
    self._items = []

  @property
  def items(self):
    return self._items
  
  @items.setter
  def items(self, title):
    self._items.append(title)

  
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    self._discount = discount

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    self._total = total

  @property
  def quantity(self):
    return self._quantity

  @quantity.setter
  def quantity(self, quantity):
    self._quantity = quantity

  def add_item(self, title, price, quantity=1):
    self._total += price * quantity
    self._quantity += quantity
    for i in range(quantity):
      self._items.append(title)

    # Store the last transaction
    self._last_transaction = {'title': title, 'price': price, 'quantity': quantity}

  def void_last_transaction(self):
    if self._last_transaction:
        title = self._last_transaction['title']
        price = self._last_transaction['price']
        quantity = self._last_transaction['quantity']
            
        self._total -= price * quantity
        self._quantity -= quantity
        for i in range(quantity):
          self._items.remove(title)
            
        self._last_transaction = None  # Reset the last transaction

  def apply_discount(self):
    if self._discount == 0:
      print('There is no discount to apply.')

    else:
      self._total -= (self._discount/100 * self._total)
      print(f"After the discount, the total comes to ${int(self._total)}.")
