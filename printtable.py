''' Basic table-printing function

Given a list of the headers and a list of lists of row values,
it will print a human-readable table.

Toggle extra_padding to true to add an extra row of the spacer
character between table entries in order to improve readability
'''
def print_table(headers,rows,extra_padding=False,spacer=' '):
    lengths = []
    for i in range(len(headers)):
        h = headers[i]
        longest = 0
        if len(str(h)) > longest:
            longest = len(str(h))
        for r in rows:
            if len(str(r[i])) > longest:
                longest = len(str(r[i]))
        lengths.append(longest)
    #Make the template for each row in the table
    template = ' {{: <{}}} |'*len(headers)
    template = template.format(*lengths)
    #Format the template for the header
    heading = template.format(*headers)
    #Print out the header
    print heading
    #Print a spacer row between the header and the data
    print '-'*len(heading)
    #Print out the rows
    for row in rows:
        print template.format(*row) #do the printing
        if extra_padding: #if extra padding is desired
            print spacer*len(heading) #print out a row of the spacer character
    return template
