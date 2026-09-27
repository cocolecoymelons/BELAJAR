from dataclasses import dataclass,field

from dataclass2_customer_class import ProductData
from customers_data_converter import convert_data_into_dict,convert_data_into_dataclass
from load_and_save_file import save_file,load_file

temporary_customers_data_container = load_file('customers_data_file')

while True:
    
    decision = input("""
    1.Add product
    2'Edit product
    3.Delete product
    4.Show Customers
    5.Exit
    
    """)
    
    if decision == "1":
        
        customer_name = input("Insert customer name: ")
        
        product_name,product_quantity,product_price, *rest = input("Insert product name,the quantity,the price and the detail(optzional). (write with a comma ex: Keyboard,3,1000,Type-1)" ).strip().split(",")
        
        temporary_customers_data_container[customer_name] = ProductData(name=product_name,quantity=int(product_quantity),price=float(product_price),detail= rest[0] if rest else 'No detail')
        
        temporary_customers_data_dict_container = convert_data_into_dict(temporary_customers_data_container)
        
        save_file(temporary_customers_data_dict_container,'customers_data_file')
        print(temporary_customers_data_container)
     
    elif decision =='2':
        
        choose_customer = input("Choose customer name: ")
        
        for name in temporary_customers_data_container:
            
            if name == choose_customer:
                edit_decision = input("""
                What do you want to edit:
                1.product
                2.Quantity
                0.Exit
                """)
                
                if edit_decision == '1':
                    edited_product_variable = input("Insert the product(0 for cancel): ")
                    
                    if edited_product_variable == '0':
                        break
                    
                    not_edited_quantity = temporary_customers_data_container[name].quantity
                    
                    temporary_customers_data_container[name] = ProductData(name=edited_product_variable,quantity=not_edited_quantity)
                    
                    print(temporary_customers_data_container)
                    
                elif edit_decision == '2':
                    
                    edited_quantity_variable = input("Insert the quantity(0 for cancel): ")
                    
                    if edited_quantity_variable == '0':
                        
                        break
                    
                    not_edited_product = temporary_customers_data_container[name].name
                    
                    temporary_customers_data_container[name]=ProductData(name=not_edited_product,quantity=int(edited_quantity_variable))
                    
                    print(temporary_customers_data_container)
                    
                elif edit_decision == '0':
                    
                    break
                
                else:
                    print("Invalid menu.")
                    
                break
            
        else:
            print(f"There is no customer name: {choose_customer}.")
            
        save_file(temporary_customers_data_container,'customers_data_file')
    
    elif decision == '3':
        
        choose_name = input("Insert customer name: ")
        
        removed = temporary_customers_data_container.pop(choose_name, None)
        
        if not removed:
            
            print(f"There is no name {choose_name}")
            continue
        
        print("Success.")
        
        save_file(temporary_customers_data_container,'customers_data_file')
        
        print(temporary_customers_data_container)
        
    elif decision == '4':
        
        pass #later
    
    elif decision == '5':
        break
    
    else:
        print("Invalid menu.")
