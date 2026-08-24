is_active = True
is_admin = True

if is_active and is_admin:
    print("Access Level: Full Admin Access")
elif is_active and not is_admin:
    print("Access Level: Employee Access")
else:
    print("Access Level: Access Denied")
