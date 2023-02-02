#   Shay Dixon
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input('Enter Start date (mm/dd/yyyy):  ')
    todate = input('Enter End date (mm/dd/yyyy):  ')
    return fromdate, todate
    #write the code to input fromdate and todate and return the values from the function.  
    #Prompt the user for the dates in the following format: mm/dd/yyyy
    #no validations are needed for this input, we will assume the dates are entered correctly




def GetHoursWorked():
    hours = float(input ('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
# COMMENT OUT THE FOLLOWING CODE
#def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
#    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst




        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print('Name: ', empname)
        print('From Date: ', fromdate)
        print('To Date: ', todate)
        print('Hours Worked: ', f'{hours:,.2f}')
        print('Hourly Rate: ', f'{hourlyrate:,.2f}')
        print('Gross Pay: ', f'{grosspay:,.2f}')
        print('Tax Rate: ', f'{taxrate:,.1%}')
        print('Income Tax: ', f'{incometax:,.2f}')
        print('Net Pay: ', f'{netpay:,.2f}')
        print()
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item




 
# COMMENT OUT THE FOLLOWING CODE
#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
#    print()n
#    print(f"Total Number Of Employees: {TotEmployees}")
#    print(f"Total Hours Worked: {TotHours:,.2f}")
#    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
#    print(f"Total Income Tax:  {TotTax:,.2f}")
#    print(f"Total Net Pay: {TotNetPay:,.2f}")

def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHours"]}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]}')
    print(f'Total Tax Rate: {EmpTotals["TotTax"]}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary



if __name__ == "__main__":
    # COMMENT OUT THE FOLLOWING CODE
    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
        EmpDetail = ['fromdate', 'todate', 'empname', 'hours', 'hourlyrate', 'taxrate']

        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)
        # COMMENT OUT THE FOLLOWING CODE
        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)
