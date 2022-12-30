import os

def check_token():
	if os.path.exists("/mypath/file"):
		with open('/mypath/file', 'r') as reader:
            my_variable=reader.readlines()[1].strip('\n\r')
            return my_variable
    else:
        print("\nThis script requires SOME_SECRET and it must be stored in /mypath/file \n")
        quit()
