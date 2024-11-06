# Python3.8.16
# Coding: utf-8  
### Calculating the Net Charge of Insulin by Using Python Lists and Loops
### Create a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations
### Use the count() method to get a count of amino acids
### Use a while loop to calculate the net charge of insulin from pH 0 to pH 14


# Store the human preproinsulin sequence in a variable called preproinsulin:  

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

## Note: Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation.
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

## Using count() to count the numbers of each amino acid
#  you will use the count() method and list comprehension to count the number of Y, C, K, H, R, D, and E amino acids. 
# These amino acids contribute to the net charge.
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
#print(seqCount)
#print(type(seqCount))

## Writing the net charge formula
pH = 0
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
