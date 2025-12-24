from logic_gates import HalfAdder, OrGate

class FullAdder:
    """
    Full Adder circuit implementation

    Computes the sum and carry-out of two input bits and a carry-in bit
    """


    def __init__(self, label: str):
        """Initialize Full Adder using two Half Adders"""
    
        self.label = label
        self.half_adder_1 = HalfAdder('Half Adder 1')
        self.half_adder_2 = HalfAdder('Half Adder 2')
        self.or_gate = OrGate('Carry Bridge')

    def perform_calculation(self, a: bool, b: bool, c_in: bool) -> tuple[int, int]:
        """
        Compute the sum and carry_out for a full adder

        Returns: 
            tuple[int, int]: (final_sum, final_carry)
        """

        #if A xor B = 1, sum1 = 1 and carry1 = 0;
        #if A and B = 1, sum1 = 0 and carry1 = 1
        sum1, carry1 = self.half_adder_1.perform_calculation(a, b)

        #if sum1 xor c_in = 1, finalsum = 1 and carry2 = 0
        #if sum1 and c_in = 1, finalsum = 0 and carry2 = 1
        final_sum, carry2 = self.half_adder_2.perform_calculation(sum1, c_in)


        final_carry = self.or_gate.perform_logic_gate(carry1, carry2)

        return final_sum, final_carry


if __name__ == "__main__":

    full_adder = FullAdder('Full Adder')

    print(f'Testing {full_adder.label}:')
    print('| A | B | Cin | Sum | Cout |')
    print('|---|---|-----|-----|------|')

    inputs = [
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)
        ]
    
    for a, b, c_in in inputs:
        s, c_out = full_adder.perform_calculation(a, b, c_in)
        print(f'| {a} | {b} |  {c_in}  |  {s}  |   {c_out}  |')
