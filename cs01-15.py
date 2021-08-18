def my_list(x):
    for i in range (len(x)):
        print(i)
        if (x[i] == 20):
            x[i] = 200
        print(x)
list = [5,10,15,20,25,50,20]
my_list(list)