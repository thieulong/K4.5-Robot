from dc_motors import turn_left, turn_right, stop
import time

spin = 1.175

def addition(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 + num2
        print(num1,'+',num2,'=',answer)
        turn_right()
        time.sleep(spin*answer)
        stop()

    except Exception:

        pass

def subtraction(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 - num2
        print(num1,'-',num2,'=',answer)
        turn_left()
        time.sleep(spin*answer)
        stop()

    except Exception:

        pass

def multiplication(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 * num2
        print(num1,'x',num2,'=',answer)
        turn_right()
        time.sleep(spin*answer)
        stop()

    except Exception:

        pass

def division(result):
    
    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 / num2
        print(num1,'/',num2,'=',answer)
        turn_left()
        time.sleep(spin*answer)
        stop()

    except Exception:

        pass
    
