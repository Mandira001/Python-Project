def integertoroman(num)
    Dictionary={1000'M',900'CM',500'D',400'CD',100'C',90'XC',50'L',40'XL',10'X',5'V',4'IV',1'I'}
    Roman=''
    i=0
    while num0
        k=list(Dictionary.keys())
        for _ in range(numk[i])
            Roman+=Dictionary[k[i]]
            num-=k[i]
        i+=1
    return Roman
num=int(input(Enter a Positive Number ))
print(integertoroman(num))