from dataclasses import dataclass,field

@dataclass
class ProductData:
    name : str
    quantity : int
    price : float
    detail : str = "No detail"
    total_price : float = field(init=False)
    
    
    def __post_init__(self):
        
        if self.price <= 0:
            print("Price must be higher than 0!")
            
        self.total_price = self.quantity*self.price
