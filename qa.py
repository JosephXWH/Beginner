unconfirmed_users = ["alice","constandin","viger"]
confirmed_users = []

#loop the confirm while no user in uu
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())

	confirmed_users.append(current_user)

print("\nThe following users are confirmed:")

for user in confirmed_users:
	print(user.title())
