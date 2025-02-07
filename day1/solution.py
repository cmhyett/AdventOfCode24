import numpy as np;

# lists is Nx2 array
def pairwise_dist(list1, list2):
    list1.sort()
    list2.sort()
    return np.sum(np.abs(list1 - list2));

def similarity_dist(list1, list2):
    result = 0;
    for i in range(0, len(list1)):
        result += np.count_nonzero(np.where(list2 == list1[i], 1, 0))*list1[i];
    return result;

if __name__ == "__main__":
    lists = np.fromfile("input.txt", dtype=int, sep=" ");
    N = len(lists);
    lists = lists.reshape((int(N/2), 2));
    print(pairwise_dist(lists[:,0], lists[:,1]))
    print(similarity_dist(lists[:,0], lists[:,1]))

