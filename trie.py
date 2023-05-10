from numpy import uint64

class Node:
    def __init__(self, code:uint64=None, ppc:uint64 = None, value=None):
        self.pattern_code = code
        self.previous_pattern_code = ppc
        self.value = value
        self.children:list[Node] = []
        self.is_terminal = False

    def find_child(self, key:str|int):
        if type(key) == str:
            try:
                return self.children[[x.value for x in self.children].index(key)]
            except ValueError:
                return None
        elif type(key) == int:
            try:
                return self.children[[x.pattern_code for x in self.children].index(key)]
            except ValueError:
                return None
        else:
            raise TypeError        
        
    def insert(self, code, ppc, key):
        self.children.append(Node(code=code, ppc=ppc, value=key))

    def __str__(self) -> str:
        return f"{self.pattern_code}:({self.previous_pattern_code}, {self.value})"
            

class Trie:
    def __init__(self):
        self.root = Node(code=0, ppc=None, value="")
        self.new_index = 1

    def find(self, key:str|int):
        if type(key) == str:
            node = self.root
            for char in key:
                new_node = node.find_child(char)
                if new_node == None:
                    return None
                node = new_node
            return node
        else:
            queue:list[Node] = []
            queue.append(self.root)
            node:Node = None

            while len(queue) > 0:
                node = queue.pop()
                if node.pattern_code == key:
                    return node
                else:
                    queue += node.children

            return None        
    
    def insert(self, pattern:str|tuple[int, str]):
        if type(pattern) == str:
            node = self.root
            for char in pattern:
                if node.find_child(char) == None:
                    node.insert(code=self.new_index, ppc=node.pattern_code, key=char)
                    self.new_index += 1
                node = node.find_child(char)
            node.is_terminal = True
        else:
            node = self.find(pattern[0])
            node.insert(code=self.new_index, ppc=pattern[0], key=pattern[1])
            node = node.find_child(pattern[1])
            node.is_terminal = True
            self.new_index += 1


    def get_string_from_code(self, code) -> str:
        if code == None:
            return self.root.value
        else:
            node = self.find(code)
            return self.get_string_from_code(node.previous_pattern_code) + node.value

    def __str__(self) -> str:
        ret = ""
        queue:list[Node] = []
        queue.append(self.root)
        node:Node = None

        while len(queue) > 0:
            node = queue.pop(0)
            queue += node.children
            ret += str(node) + "\n"

        return ret
    
def main():
    # abracadabrarabarabara
    t = Trie()
    patterns = ['a', 'b', 'r', 'ac', 'ad', 'ab', 'ra', 'rab', 'ar', 'aba', 'ra$'] # $ é End of File
    for pattern in patterns:
        t.insert(pattern=pattern)
    print(str(t))

if __name__ == "__main__":
    main()

