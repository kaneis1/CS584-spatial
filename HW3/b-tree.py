class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  
        self.leaf = leaf 
        self.keys = []  
        self.children = []
        self.father = None  

class BTree:
    def __init__(self, t):
        self.t = t  
        self.root = None  

    def search(self, k, node):
        
        if k in node.keys:
            return node
        else:
            if node.leaf:
                return node
            else:
                i=len(node.keys)-1
                while i>=0 and k<node.keys[i]:
                    i-=1
                i+=1
                return self.search(k, node.children[i])
    def checkoverflow(self, node):
        if len(node.keys) <= 2 * self.t:
            return True
        else:
            father = node.father
            median = node.keys[int(self.t)]
            leftnode = BTreeNode(self.t, node.leaf) 
            rightnode = BTreeNode(self.t, node.leaf)
            leftnode.keys = node.keys[:self.t]
            rightnode.keys = node.keys[self.t+1:]
            
            if father is self.root:
                father = BTreeNode(self.t, False)
                father.keys.append(median)
                father.children.append(leftnode)
                father.children.append(rightnode)
                father.father=father
                father.leaf=False
                self.root = father
            else:
                i=len(father.keys)-1
                father.keys.append(0)
                while i>=0 and median<father.keys[i]:
                    father.keys[i+1]=father.keys[i]
                    i-=1
                i+=1
                father.keys[i]=median
                father.children[i]=leftnode
                j=len(father.children)-1
                father.children.append(0)
                while j>i:
                    father.children[j+1]=father.children[j]
                    j-=1
                father.children[j+1]=rightnode
            
            l=len(node.children)-1    
            
            if(l>0):
                for i in range(int(l/2+1)):
                    node.children[i].father = leftnode
                for i in range(int(l/2+1),l+1):
                    node.children[i].father = rightnode
            return self.checkoverflow(father)  
                
            
            
            
    def insert(self, k):
        
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.father=self.root
            self.root.keys.append(k)  
        else:
            currentnode = self.search(k, self.root)
            i=len(currentnode.keys)-1
            currentnode.keys.append(0)
            while i>=0 and k<currentnode.keys[i]:
                currentnode.keys[i+1]=currentnode.keys[i]
                i-=1
            i+=1
            currentnode.keys[i]=k
            self.checkoverflow(currentnode)
              

    def traverse(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.traverse(child, level + 1)



if __name__ == "__main__":
    b_tree = BTree(t=2)  
    
    for val in [10, 20, 5, 6, 12, 30, 7, 17]:
        b_tree.insert(val)

    b_tree.traverse()
