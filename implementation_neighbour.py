# Function to insert a key-value pair into the AVL tree and balance it
def insert_2(root, key, value):
    # If the root is None, create a new node
    if root is None:
        return {'key': key, 'value': value, 'left': None, 'right': None, 'height': 1}
    # If the key is less than the root key, insert into the left subtree
    elif key < root['key']:
        root['left'] = insert_2(root['left'], key, value)
    # Otherwise, insert into the right subtree
    else:
        root['right'] = insert_2(root['right'], key, value)

    # Update the height of the current node
    root['height'] = 1 + max(get_height_2(root['left']), get_height_2(root['right']))

    # Check and perform rotations if necessary to balance the tree
    balance = get_balance_2(root)

    if balance > 1:
        if key < root['left']['key']:
            root['left'] = left_rotate_2(root['left'])
        return right_rotate_2(root)

    if balance < -1:
        if key > root['right']['key']:
            root['right'] = right_rotate_2(root['right'])
        return left_rotate_2(root)

    return root

# Function to perform a left rotation
def left_rotate_2(z):
    y = z['left']
    if y is not None:
        T2 = y['right']
        y['right'] = z
        z['left'] = T2
        # Update heights
        z['height'] = 1 + max(get_height_2(z['left']), get_height_2(z['right']))
        y['height'] = 1 + max(get_height_2(y['left']), get_height_2(y['right']))
        return y
    else:
        return z

# Function to perform a right rotation
def right_rotate_2(z):
    y = z['right']
    if y is not None:
        T3 = y['left']
        y['left'] = z
        z['right'] = T3
        # Update heights
        z['height'] = 1 + max(get_height_2(z['left']), get_height_2(z['right']))
        y['height'] = 1 + max(get_height_2(y['left']), get_height_2(y['right']))
        return y
    else:
        return z

# Function to get the height of a node
def get_height_2(root):
    if not root:
        return 0
    return root['height']

# Function to get the balance factor of a node
def get_balance_2(root):
    if not root:
        return 0
    return get_height_2(root['left']) - get_height_2(root['right'])

# Function to perform an inorder traversal of the tree
def inorder_traversal_2(root):
    if root:
        inorder_traversal_2(root['left'])
        print(root['key'], root['value'])
        inorder_traversal_2(root['right'])

# Function to find the successor of a given key in the AVL tree
def successor_2(avl, key):
    lst = []
    subtree = helper(avl, key, lst)
    temp = subtree
    prev = None
    if (temp['right'] != None):
        temp = temp['right']
        while (temp['left'] != None):
            temp = temp['left']
        prev = temp
    else:
        succ = None
        lst = lst[::-1]
        for i in lst:
            if i > key:
                succ = i
                break
        return succ
    return prev['key']

# Function to find the predecessor of a given key in the AVL tree
def predecessor_2(avl, key):
    lst = []
    subtree = helper(avl, key, lst)
    temp = subtree
    prev = None
    if (temp['left'] != None):
        temp = temp['left']
        while (temp['right'] != None):
            temp = temp['right']
        prev = temp
    else:
        succ = None
        lst = lst[::-1]
        for i in lst:
            if i < key:
                succ = i
                break
        return succ
    return prev['key']

# Helper function to traverse the tree and find the node with the given key
def helper(avl, snode, lst):
    if avl['key'] == snode:
        return avl
    else:
        if snode < avl['key']:
            lst.append(avl['key'])
            return helper(avl['left'], snode, lst)
        elif snode > avl['key']:
            lst.append(avl['key'])
            return helper(avl['right'], snode, lst)
