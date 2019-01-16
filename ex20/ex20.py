import sys

class BSTreeNode(object):

    def __init__(self, parent, key, value):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.parent}: ({self.key})"
        # return f"{self.left}<-from {self.parent}: ({self.key}, {self.value})->{self.right}"

class BSTree(object):

    def __init__(self):
        self.root = None

    def find_last_parent_and_node(self, node, key):
        last_parent = None

        while node:
            if key == node.key:
                last_parent = node.parent
                break
            elif key < node.key:
                last_parent = node
                node = node.left
            elif key > node.key:
                last_parent = node
                node = node.right
            else:
                sys.exit(1)

        return last_parent, node

    def set(self, key, value):
        last_parent, node = self.find_last_parent_and_node(self.root, key)

        if node:
            node.value = value
        elif not last_parent:
            self.root = BSTreeNode(None, key, value)
        else:
            if key < last_parent.key:
                last_parent.left = BSTreeNode(last_parent, key, value)
            elif key > last_parent.key:
                last_parent.right = BSTreeNode(last_parent, key, value)
            else:
                sys.exit(2)

    def get(self, key):
        last_parent, node = self.find_last_parent_and_node(self.root, key)
        return node and node.value or None
        
    def list(self, node, i=0):
        the_mid = []
        if node:
            i += 1
            item = (node.key, node.value)
            # parent_key = node.parent and node.parent.key or None
            # left_key = node.left and node.left.key or None
            # right_key = node.right and node.right.key or None
            # print(f"No.{i}: {node.key}, parent: {parent_key}, left: {left_key}, right: {right_key}")
            the_mid.append(item)
            the_left = self.list(node.left, i)
            the_right = self.list(node.right, i)
            return the_left + the_mid + the_right
        else:
            return []

    def show_list(self):
        print(self.list(self.root))

    def find_min(self, node):
        min_node = node
        while node.left:
            min_node = min_node.left
        return min_node

    def delete(self, node, key):
        last_parent, node = self.find_last_parent_and_node(node, key)
        if not node:
            print(f"No.{key} isn't exist.")
            return None
        elif not last_parent:
            result = self.root.value

            if (not node.left) and (not node.right):
                return node.value
            elif (not node.left) and node.right:
                node.right.parent = last_parent
                return node.value
            elif node.left and (not node.right):
                node.left.parent = last_parent
                return node.value
            elif node.left and node.right:
                node.key = node.left.key
                self.delete(node.left, node.left.key)
            else:
                sys.exit(6)

            return result

        if (not node.left) and (not node.right):
            result = node.value
            
            if last_parent.left == node:
                last_parent.left = None
            elif last_parent.right == node:
                last_parent.right = None
            else:
                sys.exit(5)

        elif (not node.left) and node.right:
            result = node.value
            successor = node.right
            node.key, node.value = successor.key, successor.value
            self.delete(successor, successor.key)
        elif node.left and (not node.right):
            result = node.value
            successor = node.left
            node.key, node.value = successor.key, successor.value
            self.delete(successor, successor.key)
        elif node.left and node.right:
            result = node.value
            successor = self.find_min(node.right)
            node.key, node.value = successor.key, successor.value
            self.delete(successor, successor.key)
        else:
            sys.exit(6)

        return result
        

    def do_delete(self, key):
        return self.delete(self.root, key)
