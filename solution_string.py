

def solution(string : str) -> str:
    oke = True
    while(oke):
        begin = -1
        end = -1
        for i in range(len(string)):
            if (string[i] == '<'):
                begin = i
            if (string[i] == ">"):
                end = i
        
        if (begin == -1 and end == -1):
            oke = False
        string = string.replace(string[begin : end + 1], "")
        if (string[-1] == '→'):
            string = string[ : -1]

    return (string if (oke == False) else "1")
    
