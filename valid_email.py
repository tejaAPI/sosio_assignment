import re
#Find the regex equation for valid email
regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):
	if(re.search(regex,email)):
		print(email)
	else:
		return
#Input nummber of emails
no_of_emails=int(input())
list_of_emails=[]
#Store the emails in a list
for _ in range(no_of_emails):
	list_of_emails.append(input())
print()
#Check each email in the list
for _ in list_of_emails:
	check(_)
