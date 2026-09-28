from dataclasses import dataclass,field

from dataclass2_customer_class import ProductData
from customers_data_converter import convert_data_into_dict,convert_data_into_dataclass
from load_and_save_file import save_file,load_file

temporary_customers_data_container = load_file('customers_data_file')

temporary_container_for_saving_data = {}

while True:
    
    decision = input("""
    1.Add Customer Order
    2.Edit Customer Order
    3.Delete Customer Order
    4.Show Customers Orders
    5.Exit
    
    """)
    
    if decision == "1":
        
        customer_name = input("Insert customer name: ")
        
        product_name,product_quantity,product_price, *rest = input("Insert product name,the quantity,the price and the detail(optzional). (write with a comma ex: Keyboard,3,1000,Type-1)" ).strip().split(",")
        
        temporary_customers_data_container[customer_name] = {
            'name':product_name,
            'quantity':int(product_quantity),
            'price':float(product_price),
            'detail': rest[0] if rest else 'No detail'
        }
        
        save_file(temporary_customers_data_container,'customers_data_file')
        print(temporary_customers_data_container)
     
    elif decision =='2':
        
        choose_customer = input("Choose customer name: ")
        
        for customer_name,order_detail in temporary_customers_data_container.items():
            
            if customer_name == choose_customer:
                edit_decision = input("""
                What do you want to edit:
                1.Product
                2.Quantity
                3.Price
                4.Detail
                0.Exit
                """)
                
                if edit_decision == '1':
                    edited_product_variable = input("Insert the product name(0 for cancel): ")
                    
                    if edited_product_variable == '0':
                        break
                    
                    customer_name = {
                        'name':edited_product_variable,
                        'quantity':order_detail['quantity'],
                        'price':order_detail['price'],
                        'detail': order_detail['detail']
                    }
                    
                    print(temporary_customers_data_container)
                    
                elif edit_decision == '2':
                    
                    edited_quantity_variable = input("Insert the quantity(0 for cancel): ")
                    
                    if edited_quantity_variable == '0':
                        
                        break
                    
                    customer_name = {
                        'name':order_detail['name'],
                        'quantity':int(edited_quantity_variable),
                        'price':order_detail['price'],
                        'detail': order_detail['detail']
                    }
                    
                    print(temporary_customers_data_container)
                    
                elif edit_decision == '3':
                    
                    edited_price_variable = input("Insert the product price(0 for cancel): ")
                    
                    if edited_price_variable == '0':
                        
                        break
                    
                    customer_name = {
                        'name':order_detail['name'],
                        'quantity':order_detail['quantity'],
                        'price':int(edited_price_variable),
                        'detail': order_detail['detail']
                    }
                
                elif edit_decision == '4':
                    
                    edited_detail_variable = input("Insert the product price(0 for cancel): ")
                    
                    if edited_detail_variable == '0':
                        
                        break
                    
                    customer_name = {
                        'name':order_detail['name'],
                        'quantity':order_detail['quantity'],
                        'price':edited_price_variable,
                        'detail': edited_detail_variable
                    }
                
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
        
        print("=====CUSTOMERS ORDER LIST=====")
        
        try:
            for customer_name,order_detail in temporary_customers_data_container.items():
                
                print(f"""
                    
    {customer_name}: ordering {order_detail['name']} for {order_detail['price']} each. Order {order_detail['quantity']} total price is {order_detail['total_price']}
                     """)
                            
        except KeyError:
            print("Oopss, there's something wrong with the customer order data, please check for the details. ")
    
    elif decision == '5':
        break
    
    else:
        print("Invalid menu.")
