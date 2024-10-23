def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        return None

def fsm_calculator(expression):
    # States
    START = 0
    OPERAND1 = 1
    OPERATOR = 2
    OPERAND2 = 3
    RESULT = 4
    DEAD = 5
    
    table = [
        [OPERAND1, DEAD, DEAD],      # Start state
        [OPERAND1, OPERATOR, DEAD],  # Operand1 state
        [OPERAND2, DEAD, DEAD],      # Operator state
        [OPERAND2, OPERATOR, RESULT], # Operand2 state
        [DEAD, DEAD, DEAD],          # Result state
        [DEAD, DEAD, DEAD]           # Dead state
    ]
    
    state = START
    operand1 = 0
    operand2 = 0
    operator = None
    result = 0
    i = 0

    while i < len(expression):
        ch = expression[i]

	# 0 - Digit, 1 - Operator, 2 - Equal Sign        
        if ch.isdigit():
            column = 0  
        elif ch in '+-*/':
            column = 1  
        elif ch == '=':
            column = 2 
        else:
            state = DEAD
            break
        
        state = table[state][column]

        if state == OPERAND1:
            operand1 = operand1 * 10 + int(ch) 
        elif state == OPERATOR:
            if operator:  
                operand1 = calculate(operand1, operand2, operator)
            operator = ch 
            operand2 = 0
        elif state == OPERAND2:
            operand2 = operand2 * 10 + int(ch)  
        elif state == RESULT:
            result = calculate(operand1, operand2, operator)
            print(f"Result: {result}")
            
            # Reset variables after result is calculated
            operand1 = result
            operand2 = 0
            operator = None
        elif state == DEAD:
            print("Error: Invalid input sequence.")
            return
        
        i += 1

    if state != RESULT:
        print("Error: Incomplete expression.")
    else:
        return result


expression = input("Enter an expression: ")
fsm_calculator(expression)

