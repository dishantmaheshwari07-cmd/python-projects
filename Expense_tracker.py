class expense_tracker:
	def __init__(self, income=0 , expense=0, old_expense= None):
		
		self.income = income
		self.expense = expense
		self.old_expense = old_expense
		self.total_expense_details = []	
		
	def adding_income(self,amount):
		self.income+=amount
		print(f" Balance = {self.income}")
		
	
	def expense_detail_update(self,amount,categry, short_description):
		self.expense += amount
		self.total_expense_details.append([amount,categry,short_description])
	
	def total_calculation(self):
		print(f"Total income = {self.income}")
		print(f"Total expense = {self.expense}")
		print(f"Balance left = {self.income - self.expense}")
		
	def expense_history(self):
		unique = []
		if self.old_expense:
			self.total_expense_details+=self.old_expense
			for item in self.total_expense_details:
			     if item not in unique:
			     	unique.append(item)
			
		self.total_expense_details = unique
			
		for num , i in  enumerate(self.total_expense_details, start =1):
			
			print(f"{num}.   {i[1]} -> ₹{i[0]}")
			
				
	def get_account_data(self):
		list = [self.income, self.expense]
		return list
	
	def return_expense_list(self):
		return self.total_expense_details	
	
def int_input(message):
	while True:
		try:
			return int(input(f"{message} "))
		except ValueError:
			print(f"enter a valid integer")	
	
current_account= None
user_file = None	
txn = 0		
all_account = []
account_file  = {}

def create_file(file_name , name, income , expense,  expense_history):
	with open(file_name,"w") as f:
		f.write(f" {name}\n {income}\n {expense} \n")
		for i in expense_history:
			f.write(f"{i[1]} | ₹{i[0]} | {i[2]}\n")

def single_account():
	single_account_list =[None, None,None,None]
	income_expense = current_account.get_account_data()
	expense_list = current_account.return_expense_list()
		
	single_account_list[0] = name
	single_account_list[1] = income_expense[0]
	single_account_list[2] = income_expense[1]
	single_account_list[3] = expense_list
	
	all_account.append(single_account_list)

def update_all_account(num):
	  acc_data= current_account.get_account_data()
	  expense_his = current_account.return_expense_list()
	  		
	  updated_single_account = [change_name,acc_data[0], acc_data[1], expense_his]
	  		
	  all_account[num] = updated_single_account	
	
while True:
	  choice = int_input(f"{'-' * 17} MENU {'-' * 17}\n\n Enter \n 1 to make new expense account\n 2 for adding income \n 3 to add expense \n 4 to see left balance \n 5 to watch expense  history  \n 6 for changing expnese account \n 7 to exit\n")
		     		
	  if choice in (1,6,7):
	  	
	  	if account_file:
	  		single_account()
	  		
	  		if len(all_account) > 1 and txn > 0:
	  			for num,i in enumerate(all_account):
	  				if i[0].upper() == change_name.upper():
	  					update_all_account(num)
	  			
	  			file_name = account_file[name]
	  			acc_data= current_account.get_account_data()
	  			expense_his = current_account.return_expense_list()
	  			
	  			create_file(file_name, name, acc_data[0], acc_data[1],expense_his)

	  	if choice == 1 :
	  		name = input("Enter name :")
	  		current_account = expense_tracker()
	  		user_file = f"{name} Expense File"
	  		account_file[name] = user_file
	  		 
	  	if choice == 6:
	  		 found = False
	  		 if not account_file :
	  		 	print("Make a account first ")
	  		 if len(account_file) > 1:
	  		 	change_name = input("Enter name:")
	  		 	name = change_name
	  		 	for i in all_account:
	  		 	  	
	  		 	  	if i[0].upper() == name.upper():
	  		 	  		found = True
	  		 	  		acc_info = i
	  		 	  		current_account = expense_tracker(acc_info[1], acc_info[2], acc_info[3])	
	  		 	  		txn+=1
	  		 	  	if found == False:
	  		 	  		print("No account found")
	  		 else:
	  		 	print("Minimum 2 account there on devicce to switch")
	  	if choice == 7 :
	  		break	  		 	  	
	  		 	 
	  elif choice == 2:
	  	if current_account is None:
	  		print("Creat a account First")
	  	else:
	  		money = int_input("Enter income:")
	  		current_account.adding_income(money)
	  	
	  elif choice == 3:
	  	if current_account is None:
	  		print("Creat a account First")
	  	else:
	  		category = input("Enter category :")
	  		amount = int_input("Enter money: ")
	  		description = input("Enter a short description : ")
	  		current_account.expense_detail_update (amount,category , description)
	  	
	  elif choice == 4:
	  	if current_account is None:
	  		print("Creat a account First")
	  	else:
	  		current_account.total_calculation()
	  		
	  elif choice == 5:
	  	if current_account is None:
	  		print("Creat a account First")
	  	else:
	  		current_account.expense_history()
