import re
import sys

# The time it takes to goes through file1 and file2 is O(N + M)
# The intersection is counted using the dictionary so it would be O(M)
# total would be O(N + M + N + M) = O(N + M) which is liear time


# define a function to read every token and set their key to 0 in the dictionary
def getf1Occurence():
    dict={}
    with open(sys.argv[1]) as f:
        for content in f:
            set = re.split('[^0-9a-zA-Z]', content)
            for x in set:
                if x!="" :
                    dict[x.lower()] = 0
    return dict

# if token in file two is also in file 1, set the token's key to 1
def intersect():
    dict=getf1Occurence()
    number=0
    with open(sys.argv[2]) as f:
        for content in f:
            set = re.split('[^0-9a-zA-Z]', content)
            for x in set:
                if x!="" :
                    if dict.get(x.lower())==0:
                        number = number + 1
                        dict[x.lower()] = 1
    return number

def main():
    print intersect()


if __name__ == "__main__":
    main()