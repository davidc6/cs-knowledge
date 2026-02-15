# AST Node Interface
class Node:
    def accept(self, visitor):
        pass

# Concrete Node
# Number and Add inhefit from Node
class Number(Node):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_number(self)

class Add(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_add(self)

class Multiply(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_multiply(self)

# Visitor Interface
class Visitor:
    def visit_number(self, node):
        pass

    def visit_add(self, node):
        pass

    def visit_multiply(self, node):
        pass

# Concrete visitor
# Evaluator inherits from Visitor
class Evaluator(Visitor):
    def visit_number(self, node):
        return node.value

    def visit_add(self, node):
        return node.left.accept(self) + node.right.accept(self)

    def visit_multiply(self, node):
        return node.left.accept(self) * node.right.accept(self)

# Concrete visitor
# PrettyPrinter inherits from Visitor
class PrettyPrinter(Visitor):
    def visit_number(self, node):
        return str(node.value)

    def visit_add(self, node):
        return f"({node.left.accept(self)} + {node.right.accept(self)})"

    def visit_multiply(self, node):
        return f"({node.left.accept(self)} * {node.right.accept(self)})"

# Build AST for: (1 + 2) * 3
tree = Multiply(
    Add(Number(1), Number(2)),
    Number(3)
)

evaluator = Evaluator()
printer = PrettyPrinter()

print(printer.visit_multiply(tree))
print(evaluator.visit_multiply(tree))
