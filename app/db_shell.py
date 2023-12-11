from app.models import Employee

# exec(open(r'C:\first_project\app\db_shell.py').read())

# all_emp = Employee.objects.all()
# # print(all_emp.id)

# for emp in all_emp:
#     # print(emp)                 or         # print(emp.id)        or    # print(emp.__dict__)


# emp = Employee.objects.get(id=2)
# print(emp)
# print(emp.id)
# print(emp.__dict__)

#filter      ----------- get sirf ek hi catch karke dega same letter wale emp ka but emp naam se to teen hai to hume wo list dega to filter use kiya


# emp = Employee.objects.filter(first_name__startswith = "e")
# print(emp)


# emp = Employee.objects.filter(first_name__in =["emp1" , "emp2"])
# print(emp)

# emp = Employee.objects.filter(first_name__contains ="1")
# print(emp)

# emp = Employee.objects.filter(first_name__contains="e").first()
# print(emp)

# emp = Employee.objects.filter(first_name__contains="e")[0]            #slicing
# print(emp)






#========================================to create new employee

# emp = Employee(first_name = "emp4",last_name = "jkl" , email = "jkl@gmail.com",mob_no = 995511)
# emp.save()

#or

# emp = Employee.objects.create(first_name = "emp5",last_name = "mno" , email = "mno@gmail.com",mob_no = 9944881)


#==========================================to delete

# emp = Employee.objects.get(id=2)
# emp.delete()

#or

# emp = Employee.objects.get(id=5).delete()

#to delete all data

# emp = Employee.objects.filter().delete()

#======================================to update

# emp = Employee.objects.get(id=4)
# emp.first_name = "EMP4"
# emp.last_name = "JKLM"
# emp.save()


#-====================================to count

# total_count = Employee.objects.count()
# print(total_count)

#====================================to sum             we have to import this

from django.db.models import Sum, Avg, Max, Min

# # exec(open(r'C:\first_project\app\db_shell.py').read())

# total = Employee.objects.aggregate(Sum("salary"))

# print(total)

#==========================================avg
# total = Employee.objects.aggregate(Avg("salary"))
# print(total)

#========================================order by

# Ord_by = Employee.objects.order_by("salary")
# print(Ord_by)

#================================to select specific feilds

# spc_fld = Employee.objects.values("email","mob_no")
# print(spc_fld)

#==================================to exclude feilds

# excluded_fields = Employee.objects.defer('email', 'salary')
# print(excluded_fields)


'''create object for person'''
# # exec(open(r'C:\first_project\app\db_shell.py').read())

from app.models import Person,Profile


# person = Person.objects.create(
#       first_name = "Supriya",
#       last_name = "Pathak",
#       date_of_birth = "1997-01-15",
#       email = "sp@gmail.com"
#      )


# profile = Profile.objects.create(
#     person = person,                             
#     bio = "A software developer",
#     address = "10 downing street london , UK"
#        )

'''person se profile ki info nikalni hai'''



# p2 =Person.objects.get(first_name ="supriya")
# print(p2.profile)

# p2 =Person.objects.all()                              # get all person
# print(p2)

# p2 =Person.objects.filter(first_name ="supriya" , email="sp@gmail.com")                  #chaining 
# print(p2)

# p2 =Person.objects.order_by("first_name")                                              #order by
# print(p2)

'''delete'''

# p2 = Person.objects.filter(first_name ="savita" , email="sp@gmail.com").delete()    #delete

# Person.objects.all().delete()

from django.core.exceptions import ObjectDoesNotExist
# try:
#     person_to_delete = Person.objects.get(pk=3)  # Replace with the actual primary key
#     person_to_delete.delete()
#     print("person deleted successfully")
# except ObjectDoesNotExist as msg:
#     print(msg)



'''profile se person'''

# pro_1 = Profile.objects.all()
# # print(pro_1)

# pro_1 = Profile.objects.get(id=3)
# print(pro_1)


'''manytomany'''
'''car object'''
# # exec(open(r'C:\first_project\app\db_shell.py').read())


from app.models import Fueltype,Cartype

# baleno = Cartype.objects.create(name = "Baleno")
# fortuner = Cartype.objects.create(name = "Fortuner")

################or

baleno = Cartype.objects(name = "Baleno")
fortuner = Cartype.objects(name = "Fortuner")

'''fuel object'''

# petrol = Fueltype.objects.create(name = "Petrol")
# diesel = Fueltype.objects.create(name = "Diesel")
# hybrid = Fueltype.objects.create(name = "Hybrid")
# gas = Fueltype.objects.create(name = "Gas")

###########or

petrol = Fueltype.objects(name = "Petrol")
diesel = Fueltype.objects(name = "Diesel")
hybrid = Fueltype.objects(name = "Hybrid")
gas = Fueltype.objects(name = "Gas")


'''to get all car and fuel'''

# f = Fueltype.objects.all()
# print(f)
# c = Cartype.objects.all()
# print(c)


'''associate car model with fuel'''

baleno.fueltype.add(gas)




