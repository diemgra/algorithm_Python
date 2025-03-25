def fibonacci(nums):
    x = 0
    serie = []
    ultNum = 0
    serie.append(0)
    
    while(x < nums):
        if(x < 2):
            calc = 1 + ultNum
            serie.append(calc)
            x+=1
        else:
            if (ultNum == 0): 
                calc = serie[x-1] + 1
                serie.append(calc)
                ultNum = calc
                x+=1 
            else:
                calc = serie[x-1] + ultNum
                serie.append(calc)
                ultNum = calc
                x+=1      

    return serie

if __name__ == "__main__":
    print(list(fibonacci(20)))
