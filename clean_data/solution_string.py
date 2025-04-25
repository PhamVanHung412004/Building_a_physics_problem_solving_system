
def solution(string : str) -> str:
    oke = True
    while(oke):
        begin = -1
        end = -1
        for i in range(len(string)):
            if (string[i] == '<' and string[i + 1 : i + 1 + 4] == "math"):
                begin = i
            if (string[i] == ">" and string[i - 4: i] == "math"):
                end = i
        
        if (begin == -1 or end == -1):
            oke = False
        else:        
            string = string.replace(string[begin : end + 1], " ") 
        
    if (string[-1] == '→'):
        string = string[ : -1]

    return (string if (oke == False) else "1")
    
