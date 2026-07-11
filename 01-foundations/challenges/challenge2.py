price_permonth = 50
budget= 320
total_month= budget//price_permonth
#print (total_month)

total_paid =price_permonth*total_month
#print(total_paid)

#fstrings
print (f"Total Months Paid : {total_paid}")

print(f"Months:{total_month}")
reamining= budget%price_permonth

print(f"Reamining:{reamining}")
