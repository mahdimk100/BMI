def bmi(height, weight):
    x = weight / (height * height)
    return x

def main():
    height = float(input('Enter your height: '))
    weight = float(input('Enter your weight: '))
    
    x = bmi(height, weight)
    
    print(f'BMI: {x}')
    
    if x < 18.5:
        z= 'laghar'
    elif x >= 18.5 and x < 25:
        z= 'normal'
    elif x >= 25 and x < 30:
        z= 'ezafe vazn'
    else:
        z= 'very fattttt'
    print(z)

if __name__ == '__main__':
    main()