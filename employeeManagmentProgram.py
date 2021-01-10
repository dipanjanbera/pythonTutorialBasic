'''
1. A Company named as "ABC Consultant" decided to build an employee management software to organise their employy data.
The software must has below functionalities :
	a. Employee can save below details : name , address , salary
	b. A auto generated employee ID will assigned to each employee starting from 100
	c. employee can search details by their employee id
	d. employee can modify their details by their employee id
	e. employee can delete their details by their employee id
	f. employee can view all records

* there will be a menu for all these functionalities.
* user can perform a particular task by entering correct menu option details otherwise system will prompt invalid entry.
'''
listOEmployee=[];
id = 100;
while 1>0:
    print "1.Save Employee Details";
    print "2.Search Employee Details";
    print "3.Update Employee Details";
    print "4.Delete Employee Details";
    print "5.View all Employee Details";
    choice = int(raw_input("Enter your choice "));

    if choice == 1:
            employee = {};
            name = raw_input("Name : ");
            address = raw_input("Address : ");
            salary = raw_input("Salary : ");
            employee['id']=id;
            employee['name']=name;
            employee['address'] = address;
            employee['salary'] = salary;
            id+=1;
            listOEmployee.append(employee)
            print "Employee added successfully";

    if choice == 2:
        idToSearch = int(raw_input("Please enter id to search ? "))
        for employeeDetails in listOEmployee:
            print employeeDetails['id']
            if employeeDetails['id'] == idToSearch:
                print "Employee Details";
                print "=====================";
                print "Employee ID : ", employeeDetails['id']
                print "Employee Name : ",employeeDetails['name']
                print "Employee Address : ", employeeDetails['address']
                print "Salary : ",employeeDetails['salary']

    if choice == 3:
        idToSearch = int(raw_input("Please enter id to update ? "));
        for employeeDetails in listOEmployee:
            if employeeDetails['id'] == idToSearch:
                name = raw_input("Name : ");
                address = raw_input("Address : ");
                salary = raw_input("Salary : ");
                employeeDetails['name'] = name;
                employeeDetails['address'] = address;
                employeeDetails['salary'] = salary;
                print "Employee details updated successfully";
                break
        else:
            print "Employee with id ",idToSearch," not found"


    if choice == 4:
            idToSearch = int(raw_input("Please enter id to delete ? "))
            for employeeDetails in listOEmployee:
                if employeeDetails['id'] == idToSearch:
                    listOEmployee.remove(employeeDetails)
                    print "Employee deleted successfully";
            else:
                print "Employee with id ", idToSearch, " not found"


    if choice == 5:
        print "All Employee Details";
        print "=====================";
        for employeeDetails in listOEmployee:
                print "Employee ID : ", employeeDetails['id']
                print "Employee Name : ",employeeDetails['name']
                print "Employee Address : ", employeeDetails['address']
                print "Salary : ",employeeDetails['salary']
                print "---------------------------------";

    cofirm = raw_input("Do you wish to continue (Y/N) ")
    if cofirm == 'Y' or cofirm == 'y':
        continue
    else:
        break
