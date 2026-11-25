
def read_cookie(header_part):

  for line in header_part.split("\r\n")[1:]:
    
    first_line, _, value = line.partition(":")
        
    if first_line.lower() == "cookie":
     
      chunks = value.split(";")

      for chunk in chunks:
            
        cookie_name, _, cookie_value = chunk.partition("=")

        if cookie_name.lower().strip() == "username":
                  
          return cookie_value
  
  return None