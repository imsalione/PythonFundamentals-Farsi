from webcolors import name_to_hex

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    except ValueError:
        return None
    
colorname = input("Enter Color Name: ")
result_color = color_name_to_code(colorname)
print(result_color)

