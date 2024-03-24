class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_html= ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'  
        return props_html
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value}, children: {self.children}, {self.props})"




class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None):
        super().__init__(tag, value, None, None)
        
        
    def to_html(self):
        if self.value == None:
            raise ValueError("No leafnode value specified!")
        if self.tag == None:
            return f'{self.value}'
        else:
            return f'{self.tag}{self.value}'
        
        