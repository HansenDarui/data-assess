log_file = open("um-server-01.txt")
# Connects to the text file with the info


def sales_reports(log_file):
#defines sales_reports and lets it take in the log_file which we got from the text file
    for line in log_file:
    # Goes through the lines in the text file
        line = line.rstrip()
        # removes the spaces and such from the lines on the text file
        day = line[0:3]
        # gives day a value of a certain line
        if day == "Mon":
            print(line)
        # if the day is Monday print out the line 


sales_reports(log_file)
# runs the code just created 
