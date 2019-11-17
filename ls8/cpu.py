"""CPU functionality."""

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%% Code Storage %%%%%%%%%%
# This is the part of the code that would print the 2: from sprint challenge test file

# TEST1 (address 19):
# 10000010 # LDI R2,TEST2
# 00000010
# 00100000
# 10100111 # CMP R0,R1
# 00000000
# 00000001
# 01010110 # JNE R2
# 00000010
# 10000010 # LDI R3,2
# 00000011
# 00000010
# 01000111 # PRN R3
# 00000011
# TEST2 (address 32):

# It compares R0 to R1 (R0 is 10, R1 is 20).
# If they're not equal, which they aren't, it jumps over
# the PRN that would have printed the 2 all the way to TEST2 (address 32).
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Step 1: Add the constructor to cpu.py
        # Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers.
        # Hint: you can make a list of a certain number of zeros with this syntax:
        # x = [0] * 25  # x is a list of 25 zeroes

        self.ram = [0] * 256  # allocate 256 bytes of memory
        self.registers = [0] * 8  # registers
        self.program_counter = 0  # Program Counter, current index, pointer to currently executing instruction
        self.stack_pointer = 7  # Because it will live in registers spot 7
        self.less = 0
        self.greater = 0
        self.equal = 0
        self.blank = ""  # better readability

        # %%%%%%%%%%%%%%%%%%%%%
        self.ADD = 0b10100000
        self.CALL = 0b01010000
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.MUL = 0b10100010
        self.POP = 0b01000110
        self.PRN = 0b01000111
        self.PUSH = 0b01000101
        self.RET = 0b00010001
        # %%%%%%%%%%%%%%%%%%%%%

        # %%%%%%%%%%%%%%%%%%%%%
        self.CMP = 0b10100111
        self.JEQ = 0b01010101
        self.JMP = 0b01010100
        self.JNE = 0b01010110
        # %%%%%%%%%%%%%%%%%%%%%

    # Step 2: Add RAM functions

    # ram_read() should accept the address to read and return the value stored there.
    def ram_read(self, address):
        return self.ram[address]

    # raw_write() should accept a value to write, and the address to write it to.
    def ram_write(self, val, address):
        self.ram[address] = val

    def load(self):
        """Load a program into memory."""

        address = 0
        with open(sys.argv[1]) as program:
            for row in program:
                row = row.split("#")[0].strip()
                if row is self.blank:
                    continue
                value = int(row, 2)  # set value to the number, of base 2
                print(f"\t\tdef load-> binary: {value: 08b}: \t decimal: {value}")
                self.ram[address] = value
                address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":  # add
            self.registers[reg_a] += self.registers[reg_b]
        elif op == "MUL":  # multiply
            self.registers[reg_a] *= self.registers[reg_b]
        elif op == "CMP":  # compare
            if self.registers[reg_a] < self.registers[reg_b]:
                self.less = 1
            elif self.registers[reg_a] > self.registers[reg_b]:
                self.greater = 1
            elif self.registers[reg_a] == self.registers[reg_b]:
                self.equal = 1
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.program_counter,
            # self.fl,
            # self.ie,
            self.ram_read(self.program_counter),
            self.ram_read(self.program_counter + 1),
            self.ram_read(self.program_counter + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.registers[i], end='')

        print()

    # Step 3: Implement the core of `CPU`'s `run()` method

    def run(self):
        """Run the CPU."""
        while True:

            # the instruction register is an internal register that temporarily holds a copy of the
            # currently-executing instruction. It's a copy of the thing at the address in RAM held
            # in the program counter. It's what you look at to decide what to actually do.
            # e.g. is this a LDI? Then do this.
            # e.g. is this a PRN? Then do this.
            instruction_register = self.ram[self.program_counter]
            operand_x = self.ram_read(self.program_counter + 1)
            operand_y = self.ram_read(self.program_counter + 2)

            if instruction_register is self.LDI:
                self.registers[operand_x] = operand_y
                self.program_counter += 3

            elif instruction_register is self.PRN:
                print(self.registers[operand_x])  # print the register at that place
                self.program_counter += 2    # increments by 2 to pass the arguments

            elif instruction_register is self.ADD:
                self.alu("ADD", operand_x, operand_y)
                self.program_counter += 3

            elif instruction_register is self.MUL:
                self.alu("MUL", operand_x, operand_y)
                self.program_counter += 3

            elif instruction_register is self.CMP:
                self.alu("CMP", operand_x, operand_y)
                self.program_counter += 3

            elif instruction_register is self.POP:
                self.registers[operand_x] = self.ram[self.stack_pointer]
                self.stack_pointer += 1
                self.program_counter += 2

            elif instruction_register is self.PUSH:
                self.stack_pointer -= 1
                self.ram[self.stack_pointer] = self.registers[operand_x]
                self.program_counter += 2

            elif instruction_register is self.CALL:
                self.registers[self.stack_pointer] -= 1
                self.ram[self.stack_pointer] = self.program_counter + 2
                self.program_counter = self.registers[operand_x]

            elif instruction_register is self.RET:
                self.program_counter = self.ram[self.stack_pointer]
                self.registers[self.stack_pointer] += 1

            # "jumping to an address" is the same as setting the program_counter to that address.
            elif instruction_register is self.JMP:
                self.program_counter = self.registers[operand_x]

            elif instruction_register is self.JEQ:
                if self.equal is 1:
                    self.program_counter = self.registers[operand_x]
                else:
                    self.program_counter += 2

            elif instruction_register is self.JNE:
                if self.equal is 0:
                    self.program_counter = self.registers[operand_x]
                else:
                    self.program_counter += 2

            elif instruction_register is self.HLT:
                break

            else:
                print(f"Unknown instruction at index: \t {self.program_counter}")
                sys.exit(1)

