while True:
	try:
		number=int(input("Enter your number\n"))
		res=18/number
	except NameError:
		print("please input an integer\n")
	except ZeroDivisionError:
		print("don't put zero\n")
	except:
		break
	else:
		print "\nResult is=\n",res
		break					#break loop
	finally:					#it prints after break
		print("complete Loop\n")	
	
