#Let the probability that 4-digit numbers greater than 5,000 formed from the digits 0,1,3,5 and 7 and are divisible by 5 
#case i : When repetition of digits is allowed be Pa.
#Let the probability that the 4-digit number formed is not divisible by 5 be Pr1 which implies three possibilities of 1 or 3 or 7 as the last digit.

Pa = 99/249

Pr1 = (2*5*5*3)/(2*5*5*5 - 1)

Pb = 1 - Pa

if Pb == Pr1:
   print("Pa = 99/249")

#case ii : When repetition of digits is not allowed be Pc.
#Let the probability that the 4-digit number formed is not divisible by 5 be Pr2 which implies two possibilitie of 5 or 7 as the first 
#digit and three possibilities 1 or 3 or 7 as the last digit.
#The possible combinations are (5,1) (5,3) (5,7) (7,1) and (7,3)

Pc =  3/8

Pr2 = (6+6+6+6+6)/(2*4*3*2)

Pd = 1 - Pc

if Pr2 == Pd:
   print("Pc = 3/8")