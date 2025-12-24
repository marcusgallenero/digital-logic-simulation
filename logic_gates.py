# Marcus Gallenero
# 25' Winter Break SDS
# Digital Logic Design & OOP

#-----Class Definition------#

class LogicGate:
    def __init__(self, label):
        """
        Initialize instance attributes
        """
        self.label = label
        
    def get_label(self):
        """
        Return name of the gate
        """
        return self.label
    
    def perform_logic_gate(self):
        """
        Placeholder - Specific gates will replace this with their logic
        """
        raise NotImplementedError('Must Implement Logic for this Gate!')
    

class AndGate(LogicGate):
    def __init__(self, label):
        # Calls Parent __init__ to set label
        super().__init__(label)
    
    def perform_logic_gate(self, a: bool, b: bool):
        """
        If both a and b are 1, return 1. Otherwise return 0
        """
        if a == 1 and b == 1:
            return 1
        else: 
            return 0

class OrGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
    
    def perform_logic_gate(self, a: bool, b: bool):
        """
        If a or b is 1, return 1. Else return 0
        """
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
    
    def perform_logic_gate(self, a: bool):
        """
        Return 1 if a is 0; Retrun 0 if a is 1
        """
        if a == 1:
            return 0
        else:
            return 1
        
class XorGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        # Instantiation: Use relationships between other classes
        # Formula: (a OR b) AND (NOT (a AND b))

        self.or_gate = OrGate('Internal_OR')
        self.outer_and_gate = AndGate('Internal_AND_outer')
        self.not_gate = NotGate('Internal_NOT')
        self.inner_and_gate = AndGate('Internal_AND_inner')
    
    def perform_logic_gate(self, a: bool, b: bool):
        """
        Return 1 if, and only if a and b are different
        """
        # Pass inputs into corresponding gates
        or_result = self.or_gate.perform_logic_gate(a, b)
        inner_result = self.inner_and_gate.perform_logic_gate(a, b)
        not_result = self.not_gate.perform_logic_gate(inner_result)
        outer_result = self.outer_and_gate.perform_logic_gate(or_result, not_result)

        return outer_result
    

class HalfAdder:
    def __init__(self, label):
        self.label = label

        self.xor_gate = XorGate('Sum')
        self.and_gate = AndGate('Carry')

    def perform_calculation(self, a, b):

        #If A xor B = 1, Sum = 1
        sum_bit = self.xor_gate.perform_logic_gate(a, b)

        #If A and B = 1, Carry = 1
        carry_bit = self.and_gate.perform_logic_gate(a, b)

        return sum_bit, carry_bit
   
#-------Testing-------#

if __name__ == "__main__":
    half_adder = HalfAdder('Half Adder')

    print(f'Testing: {half_adder.label}')
    print('| A | B | Sum | Carry |')
    print('|---|---|-----|-------|')

    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for a, b in inputs:
        s, c = half_adder.perform_calculation(a, b)
        print(f'| {a} | {b} |  {s}  |   {c}   |')
