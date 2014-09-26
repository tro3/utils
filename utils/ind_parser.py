#!/usr/bin/env python


class Node(list):
    def __init__(self, data=None):
        list.__init__(self)
        self.data = data
        
    def dump(self, ind=0):
        buff = ' '*ind + (self.data or '')
        for item in self:
            buff += '\n' + item.dump(ind+2)
        return buff
        

def parse(text):
    root = Node()
    last_node = root
    last_ind = 0
    stack = [(last_node, last_ind)]
    
    for line in text.split('\n'):
        if line.strip():
            new_ind = len(line) - len(line.lstrip())
                    
            if new_ind > stack[-1][1]:
                stack.append((last_node, new_ind))
            else:
                while new_ind < stack[-1][1]:
                    stack.pop()
                
            last_node = Node(line.strip())
            stack[-1][0].append(last_node)
    
    return root


if __name__ == '__main__':
    text = """
    
    Top A
        Child A1
        Child A2
            Subchild A2A 
    Top B
      Child B1
      Child B2
    
    """
    
    print parse(text).dump()

