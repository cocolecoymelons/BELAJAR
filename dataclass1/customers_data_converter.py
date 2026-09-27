from dataclasses import asdict
from dataclass2_customer_class import ProductData

the_data_in_dict = {}
def convert_data_into_dict(the_data):

    for name,product in the_data.items():
        
        the_data_in_dict[name] = asdict(product) 
    
    return the_data_in_dict
    
def convert_data_into_dataclass(the_data):
    
    for name,product in the_data:
        
        the_data_in_dict[name]= ProductData(**product)
    
    return the_data_in_dict
