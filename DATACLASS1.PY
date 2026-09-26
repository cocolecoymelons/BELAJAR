from dataclasses import dataclass

@dataclass
class ProductData:
    name : str
    quantity : int


list_customer = {}
temporary_container={}

while True:
    
    decision = input("""
    1.Add product
    2'Edit product
    3.Delete product
    4.Exit
    
    """)
    
    if decision == "1":
        
        customer_name = input("Insert customer name: ")
        
        product_name,product_quantity = input("Insert product name and the quantity(write with a comma ex,(Keyboard,3))" ).split(",")
        
        list_customer[customer_name] = ProductData(name=product_name,quantity=int(product_quantity))
        
        print(list_customer)
     
    elif decision =='2':
        
        choose_customer = input("Choose customer name: ")
        
        for name in list_customer:
            
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
                    
                    not_edited_quantity = list_customer[name].quantity
                    
                    list_customer[name] = ProductData(name=edited_product_variable,quantity=not_edited_quantity)
                    
                    print(list_customer)
                    
                elif edit_decision == '2':
                    
                    edited_quantity_variable = input("Insert the quantity(0 for cancel): ")
                    
                    if edited_quantity_variable == '0':
                        
                        break
                    
                    not_edited_product = list_customer[name].name
                    
                    list_customer[name]=ProductData(name=not_edited_product,quantity=int(edited_quantity_variable))
                    
                    print(list_customer)
                    
                elif edit_decision == '0':
                    
                    break
                
                else:
                    print("Invalid menu.")
                    
                break
            
        else:
            print(f"There is no customer name: {choose_customer}.")
    
    elif decision == '3':
        
        choose_name = input("Insert customer name: ")
        
        removed = list_customer.pop(choose_name, None)
        
        if not removed:
            
            print(f"There is no name {choose_name}")
            continue
        
        print("Success.")
        
        print(list_customer)
    
    elif decision == '4':
        break
    
    else:
        print("Invalid menu.")