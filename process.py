# This line opens up an extraneous file for reference in our code.
log_file = open("um-server-01.txt")

# this line creates a function that will be able to use a file that's passed into it.
def sales_reports(log_file):
    #this is how python does for loops, and this one iterates over the file that's passed into the function.
    for line in log_file:
        #this just makes the information on each line into its own array(technmically called lists in python).
        line = line.rstrip()
        #this selects the day we're looking for from the array.
        day = line[0:3]
        #an if statement that prints(console.logs) the relevant line where the day is tuesday. now, I'm changing it to monday.
        if day == "Mon":
            print(line)


sales_reports(log_file)
