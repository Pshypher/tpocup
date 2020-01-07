# Unless stated otherwise, each variable is assumed to be a tuple

from operator import itemgetter
import pylab

def open_file():
    file_name = input("Input a file name: ")
    found = False
    
    while not found:
        try:
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("Unable to open the file. Please try again.\n")
            file_name = input("Input a file name: ")
    
    return file_pointer


def read_data(fp):
    """Extracts the year, brand, total spending on a drug, prescription fill
        count, and units for all drugs subsidized my Medicar.Also computes the 
        average cost per prescription and the average cost per unit and adds 
        it to the data for each drug. Returns a sorted list of tuples."""
    medications_list = [] # Create an empty list to hold the record of each medication
                            # in tuples from 2011 to 2015
    # Excluding the first line of the file which includes the header,
    # read all other lines in the file pointer object.
    for line in fp:
        line = line.strip()
        if line[:4]!="Year":
            row_list = line.split(',')
            # Skip rows that do not have defined numeric values for the total,
            # prescriptions, and units.
            if row_list[3]!='n/a' and row_list[4]!='n/a' and \
               row_list[5]!='n/a':
                total_cost_float = float(row_list[3])
                prescription_count = int(row_list[4])
                unit_count = int(row_list[5])
                cost_per_prescription = total_cost_float / prescription_count
                cost_per_unit_count = total_cost_float / unit_count
                medication_record = (int(row_list[0]), row_list[1], \
                                     total_cost_float, prescription_count, \
                                     unit_count, cost_per_prescription, \
                                     cost_per_unit_count)
                medications_list.append(medication_record)
                
    medications_list.sort() 
    return medications_list

        
def top_ten_list(column, year_list):
    """Receives column index (an int) and a list of tuples containing all
        the medications covered for a specific year. Returns two lists: (list1)
        containing the brand names of the top 10 and (list2) the values in the
        specified column for the top 10 tuples reverse order."""
    
    # Sort the year list according to the value given by column.The brand name
    # column is used if different drugs have the same value in the specified
    # column
    sorted_list = sorted(year_list,key=itemgetter(column-1,1),reverse=True)
    
    # Slice off the top 10 drugs accordingly based off of the
    # values of the column
    brand_names = [drug[1] for drug in sorted_list]
    list1 = brand_names[:10] if len(brand_names)>10 else brand_names
    column_list = [drug[column-1] for drug in sorted_list]
    list2 = column_list[:10] if len(column_list)>10 else column_list
    
    return list1,list2

    
def get_year_list(year, data):
    """Using the specified year(integer) and the list of tuples with the
        entire dataset, This function returns a sorted list of tuples with all
        the medications covered by Medicaid during the specified year."""
    # Create and return a list of tuples containing the data for
    # seach drug of the specified year
    return [drug_data for drug_data in data
            if drug_data[0]==year]


def display_table(year, year_list):
    """Displays the following information for each medication in a year,
        brand name, number of prescriptions, average prescription cost,
        and the total spending per mdeication. Total spent on a medication
        is shown per thousand of the actual total spent by Medicaid."""
    
    print("{:^80s}".format("Drug spending by Medicaid in "+str(year)))
    print("{:<35s}{:>15s}{:>20s}{:>15s}".format("Medication","Prescriptions",
                                             "Prescription Cost","Total"))
    
    for med in year_list:
        per_thousand_spent = med[2]/1000
        print("{:<35s}{:>15,}{:>20,.2f}{:>15,.2f}".format(
            med[1],med[3],med[5],per_thousand_spent))


def plot_top_ten(x, y, title, xlabel, ylabel):
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
        Input:
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main():
    fp = open_file()
    data = read_data(fp)
    print("Medicaid drug spending 2011 - 2015")
    print()
    # Sentinel control variable quit initialized to an empty string
    year_str = input("Enter a year to process ('q' to terminate): ")
    while year_str!='q':
        valid_year = False
        while not valid_year:
            try:
                year_int = int(year_str)
                if year_int>=2011 and year_int<=2015:
                    valid_year = True
                else:
                    print("Invalid Year. Try Again!")
                    year_str = input("Enter a year to process ('q' to terminate): ")
            except ValueError:
                print("Invalid Year. Try Again!")
                year_str = input("Enter a year to process ('q' to terminate): ")
            
        year_list = get_year_list(year_int, data)
        display_table(year_int, year_list)
        print()
        # Prompt user for choice of whether to visually plot top 10 values
        # of any column for the medications of a particular year
        plot_str = input("Do you want to plot the top 10 values (yes/no)? ")
        if plot_str.lower()=="yes":
            top_ten_prescribed = top_ten_list(4,year_list)
            top_ten_total_spent = top_ten_list(3,year_list)
            plot_top_ten(top_ten_prescribed[0],top_ten_prescribed[1],
                         "Top 10 Medications prescribed in "+year_str,
                         "Medication Name","Prescriptions")
            plot_top_ten(top_ten_total_spent[0],top_ten_total_spent[1],
                         "Top 10 Medicaid Covered Medications in "+year_str,
                         "Medication Name","Amount")
        print()
        year_str = input("Enter a year to process ('q' to terminate): ")
        
if __name__ == "__main__":
    main()