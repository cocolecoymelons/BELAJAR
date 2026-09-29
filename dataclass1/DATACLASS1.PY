from dataclasses import dataclass,field,asdict

from dataclass2_customer_class import ProductData
from customers_data_converter import convert_data_into_dict,convert_data_into_dataclass
from load_and_save_file import save_file,load_file

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
            
            product_name,product_quantity,product_price, *rest = input("Insert product name,the quantity,the price and the detail(optional). (write with a comma ex: Keyboard,3,1000,Type-1)" ).strip().split(",")
            
            customer_order = ProductData(name=product_name,quantity=int(product_quantity),price=float(product_price),detail=rest[0] if rest else 'No detail')
            
            temporary_customers_data_container[customer_name] = asdict(customer_order)
            
            
            save_file(temporary_customers_data_container,'customers_data_file')
            
        except ValueError:
            
            print("Must insert at least 3 data and insert a number for the quantity and the price.")
            continue
        
        print(temporary_customers_data_container)
     
    elif decision =='2':
        
        choose_customer = input("Choose customer name: ")
        try:
            for customer_name,order_detail in temporary_customers_data_container.items():
                
                if customer_name == choose_customer:
                    edit_decision =  input("""
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
                        
                        
                        
                        customer_data = ProductData(
                            name=edited_product_variable,
                            quantity=order_detail['quantity'],
                            price=order_detail['price'],
                            detail=order_detail['detail']
                        )
                        
                        temporary_customers_data_container[choose_customer] = asdict(customer_data)
            
                        save_file(temporary_customers_data_container,'customers_data_file')
                        
                        print(temporary_customers_data_container)
                        
                    elif edit_decision == '2':
                        
                        edited_quantity_variable = input("Insert the quantity(0 for cancel): ")
                        
                        if edited_quantity_variable == '0':
                            
                            break
                        
                        customer_data = ProductData(
                            name=order_detail['name'],
                            quantity=int(edited_quantity_variable),
                            price=order_detail['price'],
                            detail=order_detail['detail']
                        )
                        
                        temporary_customers_data_container[choose_customer] = asdict(customer_data)
            
                        save_file(temporary_customers_data_container,'customers_data_file')
                        
                        print(temporary_customers_data_container)
                        
                    elif edit_decision == '3':
                        
                        edited_price_variable = input("Insert the product price(0 for cancel): ")
                        
                        if edited_price_variable == '0':
                            
                              break
                        
                        customer_data = ProductData(
                            name=order_detail['name'],
                            quantity=order_detail['quantity'],
                            price=float(edited_price_variable),
                            detail=order_detail['detail']
                        )
                    
                        temporary_customers_data_container[choose_customer] = asdict(customer_data)
            
                        save_file(temporary_customers_data_container,'customers_data_file')
                    
                    elif edit_decision == '4':
                        
                        edited_detail_variable = input("Insert the product detail(0 for cancel): ")
                        
                        if edited_detail_variable == '0':
                            
                            break
                        
                        customer_data = ProductData(
                            name=order_detail['name'],
                            quantity=order_detail['quantity'],
                            price=order_detail['price'],
                            detail=edited_detail_variable
                        )
                    
                        temporary_customers_data_container[choose_customer] = asdict(customer_data)
            
                        save_file(temporary_customers_data_container,'customers_data_file')
                    
                    elif edit_decision == '0':
                        
                        break
                    
                    else:
                        print("Invalid menu.")
                        
                    break
                
            else:
                print(f"There is no customer name: {choose_customer}.")
            
            
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
