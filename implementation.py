def height(AVL):
    if AVL == {} or AVL == None:
        return 0
    return AVL['height']

# calculate new height following an insertion
def update_height(AVL):
    AVL['height'] = 1 + max(height(AVL['left']), height(AVL['right']))

# This function performs a right rotation on the given node y 
# and returns the new tree after rotation. It assumes y has a left child. 
# The rotation adjusts the pointers between nodes to maintain the AVL tree property 
# and updates the heights accordingly.
def rotate_right(y):
    if y['left'] != {}:
        x = y['left']
        T2 = x['right']

        x['right'] = y
        y['left'] = T2

        update_height(y)
        update_height(x)

        return x

# This function performs a left rotation on the given node x and 
# returns the new avl tree after rotation. It assumes x has a right child. 
# Similar to rotate_right, it adjusts pointers and updates heights.
def rotate_left(x):
    if x['right'] != {} and x['right'] != None:
        y = x['right']
        T2 = y['left']
        
        y['left'] = x
        x['right'] = T2
        
        update_height(x)
        update_height(y)
        
        return y

# This function inserts a new node with the specified key-value pair into the 
# AVL tree rooted at root. It recursively traverses the tree to find the correct 
# position for insertion based on key values. After insertion, it updates heights and 
# performs rotations if necessary to maintain balance.
def insert(AVL, key, value):
    if AVL == {} or AVL == None:
        return {'key': key, 'value': value, 'left': {}, 'right': {}, 'height': 1}

    if key < AVL['key']:
        AVL['left'] = insert(AVL['left'], key, value)
    elif key >= AVL['key']:
        AVL['right'] = insert(AVL['right'], key, value)
    else:
        
        return AVL

    update_height(AVL)

    # calculate balance
    balance = height(AVL['left']) - height(AVL['right'])

    # Left heavy
    if balance > 1:
        if key < AVL['left']['key']:
            return rotate_right(AVL)
        else:
            AVL['left'] = rotate_left(AVL['left'])
            return rotate_right(AVL)

    # Right heavy
    if balance < -1:
        if key > AVL['right']['key']:
            return rotate_left(AVL)
        else:
            AVL['right'] = rotate_right(AVL['right'])
            return rotate_left(AVL)

    return AVL

def inorder_traversal(AVL):
    traversal = []
    if AVL != {} and AVL != None:
        traversal.extend(inorder_traversal(AVL['left']))
        traversal.append((AVL['key'], AVL['value']))
        traversal.extend(inorder_traversal(AVL['right']))
    return traversal

def postorder_traversal(AVL):
    result = []
    if AVL != {} and AVL != None:
        result.extend(postorder_traversal(AVL['left']))
        result.extend(postorder_traversal(AVL['right']))
        result.append((AVL['key'], AVL['value']))
    return result

def preorder_traversal(AVL):
    result = []
    if AVL != {} and AVL != None:
        result.append((AVL['key'], AVL['value']))
        result.extend(preorder_traversal(AVL['left']))
        result.extend(preorder_traversal(AVL['right']))
    return result

def search(AVL, value):
    return _search(AVL, value, [])

def _search(AVL, value, path):
    if AVL == {}:
        return None, path

    if AVL['key'] == value:
        return AVL['value'], path  # Return the result and the path

    if value < AVL['key']:
        path.append('L')
        return _search(AVL['left'], value, path)
    else:
        path.append('R')
        return _search(AVL['right'], value, path)

def get_insertion_order_from_postorder(avl_tree, postorder_traversal):
    avl_tree = {}
    # reconstruct the tree
    for key, value in postorder_traversal:
        avl_tree = insert(avl_tree, key, value)
    return inorder_traversal(avl_tree)

def get_insertion_order_from_preorder(avl_tree, preorder_traversal):
    avl_tree = {}
    # reconstruct the tree
    for key, value in preorder_traversal:
        avl_tree = insert(avl_tree, key, value)

    return inorder_traversal(avl_tree)


# mirrors the tree
def mirror(AVL):
    if AVL == {}:
        return
    else:
        # Swap the left and right subtrees
        AVL['left'], AVL['right'] = AVL['right'], AVL['left']
        mirror(AVL['left'])
        mirror(AVL['right'])
        return AVL

# counts number of nodes
def count_nodes(AVL):
    if AVL == {}:
        return 0
    return 1 + count_nodes(AVL['left']) + count_nodes(AVL['right'])

# calculates sum and then average depth of nodes.  
def sum_of_depths(AVL, depth=0):
    if AVL == {}:
        return 0
    return depth + sum_of_depths(AVL['left'], depth + 1) + sum_of_depths(AVL['right'], depth + 1)

def average_depth(AVL):
    total_depth = sum_of_depths(AVL)
    total_nodes = count_nodes(AVL)
    return total_depth // total_nodes