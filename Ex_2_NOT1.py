input=[1,10,44,12,0,-1]

print(input)

def findmax(input):
    resultmax=0
    for x in input:
        print(x)
        if x > resultmax: 
            resultmax=x
print("The maximum of the input is:",findmax(input) )