import pytest
import random

class Product:

    def __init__(self, name, price, weight, flammability, identifier):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability =flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
          print("Not so stealable")
        elif self.price / self.weight >= 0.5:
          print("Very stealable!")

    def explode(self):
        if self.flammability * self.weight < 10:
          print("...fizzle.")
        elif 10 < self.flammability * self.weight < 50:
          print("...boom!")
        elif self.flammability * self.weight > 50:
          print("...BABOOM!!")

class BoxingGlove(Product):

    def __init__(self, name, price, weight, flammability, identifier):
        super().__init__(name, price, weight, flammability, identifier)
        self.weight = 10

    def explode(Product):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
          print("That tickles.")
        elif 5 <= self.weight < 15:
          print("Hey that hurt!")
        elif self.weight > 15:
          print("OUCH!")