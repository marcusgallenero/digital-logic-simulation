# Marcus Gallenero 
# Digital Logic Design & OOP


#-----Class Definition------#
class LogicGate:
    """
    Base class for all logic gates.

    Attributes:
        label (str): Readable name of the gate
    """

    def __init__(self, label: str):
        """Initialize instance attributes"""
        self.label = label
 
    def get_label(self) -> str:
        """Return name of the gate"""
        return self.label
    
    def perform_logic_gate(self):
        """Perform the logic operation of the gate (implemented in subclasses)"""
        raise NotImplementedError('Must Implement Logic for this Gate.')
    

class AndGate(LogicGate):
    """Logic gate that performs the AND opertaion"""

    def perform_logic_gate(self, a: bool, b: bool) -> int: 
        """
        Returns 1 if both inputs are 1. Otherwise return 0
        """
        if a == 1 and b == 1:
            return 1
        else: 
            return 0


class OrGate(LogicGate):
    """Logic gate that performs the OR operation"""

    def perform_logic_gate(self, a: bool, b: bool) -> int:
        """
        Return 1 if either input is 1. Otherwise return 0
        """
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(LogicGate):
    """Logic gate that performs the NOT operation"""
    
    def perform_logic_gate(self, a: bool) -> int:
        """
        Return the logical inverse of an input
        """
        if a == 1:
            return 0
        else:
            return 1
        
class XorGate(LogicGate):
    """Logic gate that performs the XOR operation"""

    def __init__(self, label: str):
        """Initialize internal gates used to compute XOR"""

        super().__init__(label)
        self.or_gate = OrGate('Internal_OR')
        self.outer_and_gate = AndGate('Internal_AND_outer')
        self.not_gate = NotGate('Internal_NOT')
        self.inner_and_gate = AndGate('Internal_AND_inner')
    
    def perform_logic_gate(self, a: bool, b: bool) -> int:
        """
        Return 1 if inputs differ. Otherwise return 0
        """
        
        or_result = self.or_gate.perform_logic_gate(a, b)
        inner_result = self.inner_and_gate.perform_logic_gate(a, b)
        not_result = self.not_gate.perform_logic_gate(inner_result)
        outer_result = self.outer_and_gate.perform_logic_gate(or_result, not_result)

        return outer_result
    

class HalfAdder:
    """
    Half adder circuit implementation

    Computes the sum and carry of two input bits
    """

    def __init__(self, label: str):
        self.label = label
        self.xor_gate = XorGate('Sum')
        self.and_gate = AndGate('Carry')

    def perform_calculation(self, a: bool, b: bool) -> tuple[int, int]:
        """
        Compute the sum and carry bits for two input bits

        Returns:
            tuple[int, int]: (sum_bit, carry_bit)
        """

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
