import numpy as np;

def process_mul_substring(substring):
    result = 0;
    if ((substring.find(',') > -1) and (substring.find(')') > -1)):
        int1 = substring[substring.find('(')+1:substring.find(',')];
        int2 = substring[substring.find(',')+1:substring.find(')')];
        if (int1.isdigit() and int2.isdigit()):
            result = int(int1)*int(int2);
    return result;

def check_for_do(substring, do_var):
    retval = do_var;
    do_ind = substring.rfind("do()");
    dont_ind = substring.rfind("don't()")

    if (do_ind == dont_ind): # neither found
        retval = do_var; #no change
    elif (do_ind > dont_ind):
        retval = True; 
    elif (do_ind < dont_ind):
        retval = False; 
    return retval;

def scan_memory(with_do=False):
    result = 0;
    do_var = True;

    with open("input.txt", 'r') as fp:
        for line in fp:
            ind = 0;
            while (ind >= 0):
                ind = line.find('mul(')
                do_substring = line[:ind];
                mul_substring = line[ind:ind+len('mul(,)')+2*3]
                do_var = check_for_do(do_substring, do_var) if with_do else True;
                result = result + process_mul_substring(mul_substring) if do_var else result;
                line = line[ind+len('mul('):]
        return result;

if __name__ == "__main__":
    print(scan_memory());
    print(scan_memory(with_do=True));
