"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = 0.00

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5

        if self.species == "Christmas Melon":
            base_price = 1.5 * base_price
        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        super().get_total()

        if self.qty < 10:
            total = 3 + ((1 + self.tax) * self.qty * base_price)
            
        return total
