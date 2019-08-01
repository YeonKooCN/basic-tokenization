import re
import sys

# speed to process the whole file which is O(N)
# dictionary operations are O(1)
# speed of the sorted function is O(NlogN)
# sorting the whole dictionary would be smaller than O(NlogN)
# total is approximately O(NlogN)

def getOccurence():
    dict={}
    with open(sys.argv[1]) as f:
        for content in f:
        # stem non alphabetical or non number. so tokens would be alphabetical or number
            set = re.split('[^0-9a-zA-Z]', content)
            for x in set:
                if x!="" :
                	# set occurance to 0 when the words pops for the first time
                    if dict.get(x.lower()) == None:
                        dict[x.lower()] = 1
                    else:
                    	# add one to the word's occurance
                        dict[x.lower()] = dict[x.lower()] + 1
    return dict

def main():

    dict=getOccurence()
    # use lambda function to sort output by occurance in reverse order first, and then in alphabetical order
    for w in sorted(dict, key = lambda x: (-dict[x], x)): 
        print "%s\t%d"%(w,dict[w])

if __name__ == "__main__":
    main()