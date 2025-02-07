import numpy as np;

# reports is a list of lists of integers
def determine_safe(reports, with_prob_damp=False):
    result = np.zeros(len(reports));

    def step_cond(x):
        return (x >= 1) and (x <= 3);
    arr_cond = np.vectorize(step_cond);

    def is_safe(l): #single list bool
        diffs = l[1:]-l[:-1];
        sgns = np.sign(diffs)
        return ((np.all(np.where(sgns==sgns[0], 1, 0))) and \
            (np.all(arr_cond(np.abs(diffs)))));

    # if a list is unsafe the offending entry can be
    #  located on the left or right of the first error
    def modify_list(l):
        diffs = l[1:]-l[:-1];
        adiffs = np.abs(diffs);
        sgns = np.sign(diffs);
        failing_ind = -1;
        prevailing_sign = 1 if (np.count_nonzero(sgns==1) >= np.count_nonzero(sgns==-1)) else -1;
        for i in range(0,len(l)-1):
            if ((sgns[i] != prevailing_sign) or\
                (adiffs[i] < 1) or\
                (adiffs[i] > 3)):
                failing_ind = i;
                break;
        return np.concatenate((l[:i],l[i+1:])), np.concatenate((l[:i+1],l[i+2:]))
    
    for i in range(0,len(reports)):
        l = reports[i];
        if (is_safe(l)):
            result[i] = 1;
        elif (with_prob_damp): #try again removing a problem entry
            l1, l2 = modify_list(l);
            if (is_safe(l1) or is_safe(l2)):
                result[i] = 1;
            
    return np.count_nonzero(result);
    

if __name__ == "__main__":
    lists = [];
    with open("input.txt", 'r') as fp:
        lists = [np.array(line.rstrip('\n').split(), dtype=int) for line in fp];
    print(determine_safe(lists))
    print(determine_safe(lists, with_prob_damp=True))
