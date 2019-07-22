#Converter from RGB to HEX and HEX to RGB

def rgb_hex():
  invalid_msg = "Invalid value had been entered"
  red = int(input("Enter the value for Red: "))
  if red < 0 or red > 255:
    return(invalid_msg)
    
  green = int(input("Enter a value for Green: "))
  if green < 0 or green > 255:
    return(invalid_msg)
    
  blue = int(input("Enter a value for Blue: "))
  if blue < 0 or blue > 255:
    return(invalid_msg)
    
  val = (red << 16) + (green << 8) + blue
  return("%s" % (hex(val)[2:]).upper())
  
def hex_rgb():
  hex_val = input("Enter a Hex Value: ")
  if len(hex_val) != 6:
    return("Invalid Value Entered")
    
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  return("rgb(%s, %s, %s,)" % (red, green, blue))

        
def convert1():
  while True:
    option = input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ')
    if option == '1':
      print('RGB to Hex...')
      print(rgb_hex())
    elif option == '2':
      print('Hex to RGB...')
      print(hex_rgb())
    elif option == 'X' or option == 'x':
      break
    else:
      print('Error')


convert1()
  
  
  
  
    
    

