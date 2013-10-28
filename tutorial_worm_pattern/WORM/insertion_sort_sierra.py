import sys, getopt
import random  # for generating random numbers
import time    # for timing each sort function with time.clock()
from decimal import *

def data_reader(filename):
    data_list_char =[];
    data_list_int =[];
    data_list_char = open(filename, 'r').read().split(" ")
    r=0;
    for info in data_list_char:
        if(info==''):
           continue;
        k=int(info);
        #print(k);
        data_list_int.append(k);

    return data_list_int;

def output_writer(filename,data_set,N):
    fptr1=   open(filename, "w");
    count=0;
    for i in data_set:
        fptr1.write(str(i));
        if(count==(N-1)):
            break;
        fptr1.write(" ");
        count=count+1;
        

def insertion_sort(list4):
    for i in range(1, len(list4)):
        temp = list4[i]
        j = i
        while j > 0 and list4[j - 1] > temp:
            list4[j] = list4[j - 1];
            j =j- 1;
        list4[j] = temp
    return list4



def main():
   inputfile = 'Data_part_2.txt'
   outputfile = 'Sorted_Data2.txt'
   data_set=data_reader(inputfile);
   no_of_elements=len(data_set);
   sorted_data_ins_sort=insertion_sort(data_set);
   output_writer(outputfile,sorted_data_ins_sort,no_of_elements)



if __name__ == "__main__":
   main()

