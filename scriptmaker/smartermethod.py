import csv

with open("csv_users.txt", "r") as csvfile:
    i = 0
    for row in csv.reader(csvfile):
        i += 1
        filename = f"admin.rc{i}"

        with open(filename, "w") as outfile:
            outfile.write(f"export OS_AUTH_URL={row[0]}\n")
            outfile.write(f"export OS_IDENTITY_API_VERSION=3\n")
            outfile.write(f"export OS_PROJECT_NAME={row[1]}\n")
            outfile.write(f"export OS_PROJECT_DOMAIN_NAME={row[2]}\n")
            outfile.write(f"export OS_USERNAME={row[3]}\n")
            outfile.write(f"export OS_USER_DOMAIN_NAME={row[4]}\n")
            outfile.write(f"export OS_PASSWORD={row[5]}\n")

print("admin.rc files created")
