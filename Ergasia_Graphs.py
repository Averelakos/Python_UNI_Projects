"""""""""""""""""
Arthor: Iraklis Tsikas
AM: MPPL20082
DATE: 1/7/2021
"""""""""""""""""

import networkx as nx
import matplotlib. pyplot as plt
import random


from networkx.readwrite.json_graph import tree



n = random.randint(1,50)
T = nx. random_tree(n)
pos = nx. layout . kamada_kawai_layout(T)
nx. draw_networkx(T,pos)
Tcopy = nx.Graph(T) 

# count is used to determing if the nodes are leafs or neighbours of the leafs
count=0
# trees is used later to count the trees we checked
trees=0
# MAX is used to save the nodes tha are part of the maximum independet set
MAX=[]
# the total sum of the maximun independed set of the tree
MAX_sum=0
print("/////////////////////////////////////////////////////////////////////////////////////////////////////")





"""""""""""
In the while we check  ifthe edges are bigger of 1. 

1.If they are bigger then checks the degree of the nodes to found the 
ones with degree equal of 1 and those one are the leafs.

2. Then counts the MAX and saves thoses leafs and deletes them from the tree and put the count++

3. In the next run if the while is true and the count++ we get in the elifand we check the leafs of the new tree with 
the degree equal to 1. These leafs are deleted from the tree 

4. These loop continius until the Tcopy has only one edge or no edge and exit the while

"""""""""""


while( Tcopy. size (int) > 1):
    leaves = []
    
        
    if count==0:
        trees=1+trees
        sum=0
        for v in Tcopy:
            if( Tcopy. degree(v) == 1):
                    
                leaves . append (v)
                sum=sum+1
                
        Tcopy. remove_nodes_from( leaves )
        MAX.append(leaves)
        print("To MAΣ Για το {} δεντρο είναι: {} και τα φύλλα είναι: {}".format(trees,sum,leaves))
        count=count+1
        MAX_sum=MAX_sum+sum

    elif count==1:
        for v in Tcopy:
            if( Tcopy. degree(v) == 1):
                    
                leaves . append (v)
        Tcopy. remove_nodes_from( leaves )
        count=count-1
    

nx. draw_networkx_nodes(Tcopy ,pos , node_color="green")




"""""""""
1. In case  if the graph has left 2 nodes with one edge we get in the if

2. We get in the for we get the first nodes the fore found and append in the MAX

3. And we break right away
"""""""""




if(Tcopy.size(int)==1):
    leaves=[]
    for v in Tcopy:
        leaves.append(v)
        break
    MAX.append(leaves)
    MAX_sum=MAX_sum+1
    print("To MAΣ Για το τελευταιο δεντρο επειδη είναι 2 κορυφες με ένα δεσμό είναι: 1 και το φύλλο που επιλέγουμε είναι: {}".format(leaves))
else:
    leaves=[]
    for v in Tcopy:
        leaves.append(v)
    MAX.append(leaves)
    MAX_sum=MAX_sum+1
    print("Το ΜΑΣ για το τελευταιο δεντρο είναι 1: και τα φυλλα μας είναι : {}".format(leaves))



print("////////////////////////////////////////////////////////////////////////////////////////////////////")

print("Το συνολικό ΜΑΣ για το δέντρο μας είναι: {}".format(MAX_sum))
print("Στο γράφημμα οι πράσινες κουκίδες μας δειχνουν το τελευταιο δέντρο ")
plt. show()