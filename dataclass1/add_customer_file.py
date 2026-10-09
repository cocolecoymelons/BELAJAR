from dataclasses import asdict
from dataclass2_customer_class import ProductData

def add_customer(customer_name,temporary_container):
    
    product_name,product_quantity,product_price, *rest = input("Insert product name,the quantity,the price and the detail(optional). (write with a comma ex: Keyboard,3,1000,Type-1)" ).strip().split(",",3)
            
    customer_order = ProductData(name=product_name,quantity=int(product_quantity),price=float(product_price),detail=rest[0] if rest else 'No detail')
    
    temporary_container[customer_name] = asdict(customer_order)
