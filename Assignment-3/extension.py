fname=input("Enter the file name with the extension: ")

extension=fname.split('.')
print("The extension is .{}".format(extension[-1]))
