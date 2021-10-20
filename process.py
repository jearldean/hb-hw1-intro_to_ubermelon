# Open this file with the data as formatted text:
log_file = open("um-server-01.txt")


def sales_reports(log_file):
    # For each line of log_file
    for line in log_file:
        # Chop off any whitespace characters on the right side of the line
        line = line.rstrip()
        # The date code ('Mon', 'Tue', 'Wed', ...) is the first 3 characters of each line
        day = line[0:3]
        # Changed "Tue" to "Mon" because the boss wants a Monday Report
        if day == "Mon":
            # Print each line that matches
            print(line)
    # It might seem trivial but if log_file was 10k or 100k lines long, we would
    # appreciate a script like this one.


# Call sales_reports with the argument: the contents of the log_file
sales_reports(log_file)
