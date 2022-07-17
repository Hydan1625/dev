#this will take an array like ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] and trans form into :
#   698
# +  32
# -----
#   730

def arithmetic(arg):
    count1 = 0
    operation1 = 0
    operation2 = 0
    position = 0
    string = ""
    result = 0

    for i in arg: 
        position = count1
        for a in range(0, position):
            string += arg[a]
            operation1 = int(string)
            string = ""
            for b in range(position+1, arg.lenght() - 1):
                string += b
            operation2 = int(string)
            string = ""
        count1 += 1
    if i == "+":
        result = operation1 + operation2
    else:
        result = operation1 - operation2

    return result

def formater(arg, *args):
    valores = []
    for arg in args:
        arg.strip()
        operation = arithmetic(arg)
        valores.append(operation)
    
    return valores
