from dc_motors import turn_left, turn_right

def addition(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 + num2
        print(num1,'+',num2,'=',answer)

    except Exception:

        pass

def subtraction(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 - num2
        print(num1,'-',num2,'=',answer)

    except Exception:

        pass

def multiplication(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 * num2
        print(num1,'x',num2,'=',answer)

    except Exception:

        pass

def division(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 / num2
        print(num1,'/',num2,'=',answer)

    except Exception:

        pass