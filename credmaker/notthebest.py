
with open("admin.rc", "a") as outFile:
    osAUTH = input("what is the OS_AUTH_URL? ")
    #print(f"export OS_AUTH_URL={osAUTH}", file=outFile)
    outFile.write(f"export OS_AUTH_URL={osAUTH}")
