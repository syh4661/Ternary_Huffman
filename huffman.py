import queue

class HuffmanNode(object):
    def __init__(self, left=None, mid=None ,right=None, root=None):
        self.left = left
        self.mid = mid
        self.right = right
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.left, self.mid, self.right))
def create_tree(probabilities):
    p = queue.PriorityQueue()
    for value in probabilities:    # 1. Create a leaf node for each symbol
        p.put(value)               #    and add it to the priority queue
    while p.qsize() > 2:         # 2. While there is more than two node
        l, m, r = p.get(), p.get(), p.get()  # 2a. remove three highest nodes
        node = HuffmanNode(l, m, r) # 2b. create internal node with children
        p.put((l[0]+m[0]+r[0], node)) # 2c. add new node to queue 
        
    return p.get()               # 3. tree is complete - return root node

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    w, n = node
    if isinstance(n, str):
        code[n] = prefix
    else:
        walk_tree(n.left, prefix + "2")
        walk_tree(n.mid, prefix + "1")
        walk_tree(n.right, prefix + "0")
    return(code)

size = int(input('Enter the number of your codes :'))

probability = [] # create empty list

for i in range(0, size): # set up loop to run 5 times
    print('Please enter the',i+1,'input')
    number = str(input('The signal number:              ')) # prompt user for number 
    prob = float(input('The probability:                '))
    tup=(prob,number)
    probability.append(tup) # append to our_list
node = create_tree(probability)

leng_sum =0
var_sum=0

print('|---------------THE-SOURCE-CODE-----------------|')
print(' Prob  CodeWord')
code = walk_tree(node)

for i in sorted(probability, reverse=True):
    print ('{:6.3f}'.format(i[0]), code[i[1]])
    leng_sum+=i[0]*len(code[i[1]])
for i in sorted(probability, reverse=True):    
    var_sum+=i[0]*((len(code[i[1]])-leng_sum)**2)
print('|----------------MEASURES-----------------------|')
print(' The expected Length : ','{:6.2f}'.format(leng_sum))
print(' The variance :        ','{:6.2f}'.format(var_sum))