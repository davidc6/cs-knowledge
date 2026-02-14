class VisitorInterface:
    def visit_mapper(self, element):
        pass

    def visit_reducer(self, element):
        pass

class PrinterVisitor(VisitorInterface):
    def visit_mapper(self, element):
        print(f"printing {element.name}")
    
    def visit_reducer(self, element):
        print(f"printing {element.name}")

class IdVisitor(VisitorInterface):
    def visit_mapper(self, element):
        element.name = f"1_{element.name}_m"
        return element.name
    
    def visit_reducer(self, element):
        element.name = f"1_{element.name}_r"
        return element.name

class ConcatenatorVisitor(VisitorInterface):
    def visit_mapper(self, element):
        return f"{element.name} (mapper allows to map over elements)"
    
    def visit_reducer(self, element):
        return f"{element.name} (reducer allows to reduce elements)"

class Mapper:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor: VisitorInterface):
        return visitor.visit_mapper(self)

    def remove(self, visitor: VisitorInterface):
        pass

class Reducer:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor: VisitorInterface):
        return visitor.visit_reducer(self)

    def combine(self):
        pass

mapper = Mapper("mapper")
reducer = Reducer("reducer")

printer_visitor = PrinterVisitor()
concatenator_visitor = ConcatenatorVisitor()
id_visitor = IdVisitor()

print("====== PrinterVisitor =======")

mapper.accept(printer_visitor)
reducer.accept(printer_visitor)

print("====== ConcatenatorVisitor =======")

print(mapper.accept(concatenator_visitor))
print(reducer.accept(concatenator_visitor))

print("====== IdVisitor  =======")

print(mapper.accept(id_visitor))
print(reducer.accept(id_visitor))

