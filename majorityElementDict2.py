#attempting to solve majority element with counter dictionary 
from collections import Counter

#elements = [2, 3, 9, 2, 2]

def majority_element_naive(elements):
    dictElements = Counter(elements)
    maxValue= max(dictElements.values())
    if maxValue > len(elements) / 2:
        return 1 
    else: 
        return 0
    

#print(majority_element_naive(elements))


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
