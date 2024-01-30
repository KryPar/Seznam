# Definice třídy TreeNode pro reprezentaci jednotlivých uzlů stromové struktury
class Treenode:
    def __init__(self, type, value, operation, parent=None, children=None):
        self.type = type         # Typ uzlu
        self.value = value       # Hodnota uzlu
        self.operation = operation  # Operace k provedení (ADD nebo MULTIPLY)
        self.parent = parent     # Rodičovský uzel, None pokud je uzel kořenem
        self.children = children # Seznam dětských uzlů, None pokud nejsou žádné děti

# Funkce pro výpočet souhrnné hodnoty od zadaného uzlu ke kořeni stromu
def aggregate(node, nodeType, startingValue):
    current_value = startingValue  # Inicializace souhrnné hodnoty

    # Iterace přes uzly stromu směrem ke kořeni
    while node is not None:
        # Zpracování uzlu, pokud odpovídá zadanému typu
        if node.type == nodeType:
            # Provádění operace podle typu uzlu
            if node.operation == "ADD":
                current_value += node.value
            elif node.operation == "MULTIPLY":
                current_value *= node.value
            else:
                return None  # Vrácení None pro neplatnou operaci

        # Posun k rodičovskému uzlu
        node = node.parent

    # Vrácení vypočítané hodnoty
    return current_value

# Vytvoření stromové struktury
root = Treenode("A", 1, "ADD")  # Kořenový uzel
child1 = Treenode("B", 2, "MULTIPLY", root)  # Dětský uzel kořene
child2 = Treenode("A", 2, "ADD", root)  # Další dětský uzel kořene
root.children = [child1, child2]  # Přidání dětských uzlů k kořeni

# Použití funkce aggregate a výpis výsledku
result = aggregate(child2, "A", 0)
print(result)  # Výpis vypočítané hodnoty

