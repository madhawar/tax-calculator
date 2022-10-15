gross_salary = float(input("Your Monthly Gross Salary in 2023 (i.e. 425000.00): "))
annual_gross_income = gross_salary * 12.00;
tax_exempt_threshold = 1200000

category_1=0.00
category_2=30000.00
category_3=90000.00
category_4=180000.00
category_5=300000.00
category_6=450000.00

category_1_tax=6
category_2_tax=12
category_3_tax=18
category_4_tax=24
category_5_tax=30
category_6_tax=36

cat_1_left_boundary=0.00
cat_1_right_boundary=500000.00
cat_2_right_boundary=1000000.00
cat_3_right_boundary=1500000.00
cat_4_right_boundary=2000000.00
cat_5_right_boundary=2500000.00
cat_6_right_boundary=3000000.00

if tax_exempt_threshold > annual_gross_income :
  taxable_income = 0.00
  print("You will not be taxed!")
else:
  print("Annual gross income is Rs. " + "{:,.2f}".format(annual_gross_income))
  taxable_income = annual_gross_income - tax_exempt_threshold
  print("Taxable income is Rs. " + "{:,.2f}".format(taxable_income))
  if taxable_income > cat_1_left_boundary and taxable_income < cat_1_right_boundary:
    total_tax = (taxable_income * (category_1_tax/100) - category_1)    
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))    
  elif taxable_income > cat_1_right_boundary and taxable_income < cat_2_right_boundary:  
    total_tax = (taxable_income * (category_2_tax/100) - category_2)
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))
  elif taxable_income > cat_2_right_boundary and taxable_income < cat_3_right_boundary:
    total_tax = (taxable_income * (category_3_tax/100) - category_3)
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))    
  elif taxable_income > cat_3_right_boundary and taxable_income < cat_4_right_boundary:
    total_tax = (taxable_income * (category_4_tax/100) - category_4)
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))        
  elif taxable_income > cat_4_right_boundary and taxable_income < cat_5_right_boundary:
    total_tax = (taxable_income * (category_5_tax/100) - category_5)
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))          
  elif taxable_income > cat_5_right_boundary and taxable_income < cat_6_right_boundary:
    total_tax = (taxable_income * (category_6_tax/100) - category_6)
    print("Total annual tax will be Rs. " + "{:,.2f}".format(total_tax))            
  else:
    print("Hi, Dhammika Perera")