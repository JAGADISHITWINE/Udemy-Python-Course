double_val = []
odd_sum = 0
even_sum = 0
card_no = '5610591081018250'
number = list(card_no)
for (index,val) in enumerate(number):
    if index % 2 != 0:
        odd_sum = odd_sum + int(val)
    else:
        double_val.append(int(val)*2)


## Converting list into string
double_string = ""
for x in double_val:
    double_string += str(x)
    
double_val = list(double_string)

for x in double_val:
    even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('Valid Card')
else:
    print('Invalid Card')