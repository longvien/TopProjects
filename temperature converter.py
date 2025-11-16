def convert_F_C(number):  
    return (number - 32) * 5 / 9  

def convert_C_F(number):  
    return (number * 9 / 5) + 32  


choice = input('In which direction would u like to convert? °F to °C or conversely?\n')
if choice == '°F to °C' or choice == 'F to C':
    measure = '°C'
elif choice == '°C to °F' or choice == 'C to F':
    measure = '°F'
choices = {
    '°F to °C': convert_F_C,
    'F to C': convert_F_C,
    '°C to °F': convert_C_F,
    'C to F': convert_C_F
}
if choice in choices:
    number = float(input(f'Please type in a number that you want to convert from {choice} \n'))
    result = choices[choice](number)
    print(f'The result after convert {number} from {choice} is: {str(result)} {measure}') # type: ignore
else:
    print('Invalid choice. Please select a valid conversion option.')