from dataclasses import dataclass,field,asdict

from dataclass2_customer_class import ProductData
from customers_data_converter import convert_data_into_dict,convert_data_into_dataclass
from load_and_save_file import save_file,load_file

from add_customer_file import add_customer
from edit_customer_file import edit_customer_order

temporary_customers_data_container = load_file('customers_data_file')

print(temporary_customers_data_container)

while True:
    
    decision = input("""
    1.Add Customer Order
    2.Edit Customer Order
    3.Delete Customer Order
    4.Show Customers Orders
    5.Exit
    
    """)
    
    if decision == "1":
        try:
            customer_name = input("Insert customer name: ")
            
            add_customer(customer_name,temporary_customers_data_container)
            
            save_file(temporary_customers_data_container,'customers_data_file')
            
        except ValueError:
            
            print("Must insert at least 3 data and insert a number for the quantity and the price.")
            continue
        
        print(temporary_customers_data_container)
     
    elif decision =='2':
        
        choose_customer = input("Choose customer name: ")
        try:
                    
            edit_customer_order(choose_customer,temporary_customers_data_container)

            print(temporary_customers_data_container)
         
        except ValueError:
            
            print("Please input a number.")
            continue
            
        except TypeError:
            
            print("Invalid input type. Please check the fields and try again.")
            continue
        
        except NameError:
            
            print("Attempted to access an uninitialized identifier.")
            continue
            
        except KeyError:
            
            print("The requested information could not be found.")
    
    elif decision == '3':
        
        choose_name = input("Insert customer name: ")
        
        removed = temporary_customers_data_container.pop(choose_name, None)
        
        if not removed:
            
            print(f"There is no customer name:  {choose_name}")
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
