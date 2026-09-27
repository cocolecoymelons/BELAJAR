import json

def save_file(the_data_to_save,the_file):
    
    with open(the_file,'w') as customer_data:
        json.dump(the_data_to_save,customer_data,indent=4)
    
def load_file(the_file):
    
    try:
    
        with open(the_file,'r') as customer_data:
            return json.load(customer_data)
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("File is not found or system failed to read the data.")
        print("Making a new one...")
        
        with open(the_file,'w') as customer_data:
            json.dump({},customer_data,indent=4)
            
            print("Re-run the program, thank you!")
            
            return {}
