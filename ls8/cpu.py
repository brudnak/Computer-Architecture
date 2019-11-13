"""CPU functionality."""

import sys

blank = ""

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Step 1: Add the constructor to cpu.py
        # Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers.
        # Hint: you can make a list of a certain number of zeros with this syntax:
        # x = [0] * 25  # x is a list of 25 zeroes

        self.ram = [0] * 256  # ram
        self.registers = [0] * 8  # registers
        self.program_counter = 0  # Program Counter, current index, pointer to currently executing instruction
        self.HLT = 0b00000001
        self.PRN = 0b01000111
        self.LDI = 0b10000010
        self.MUL = 0b10100010

    # Step 2: Add RAM functions

    # ram_read() should accept the address to read and return the value stored there.
    def ram_read(self, address):
        return self.ram[address]

    # raw_write() should accept a value to write, and the address to write it to.
    def ram_write(self, val, addr):
        self.ram[addr] = val

    def load(self):
        """Load a program into memory."""

        # address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]
        #
        # global ldi
        # global prn
        # global halt
        # ldi = program[0]  # LDI R0,8
        # prn = program[3]  # PRN R0
        # halt = program[5]  # HLT
        #
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

        address = 0
        with open(sys.argv[1]) as program:
            for row in program:
                row = row.split("#")[0].strip()
                if row is blank:
                    continue
                value = int(row, 2)
                self.ram[address] = value
                address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]

        elif op == self.MUL:
            self.registers[reg_a] *= self.registers[reg_b]
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

            instruction_register = self.ram[self.program_counter]
            operand_x = self.ram_read(self.program_counter + 1)
            operand_y = self.ram_read(self.program_counter + 2)

            if instruction_register is self.LDI:
                self.registers[operand_x] = operand_y
                self.program_counter += 3
            elif instruction_register is self.PRN:
                print(self.registers[operand_x])
                self.program_counter += 2
            elif instruction_register is self.MUL:
                self.alu(self.MUL, operand_x, operand_y)
                self.program_counter += 3
            elif instruction_register is self.HLT:
                break
            else:
                print(f"Unknown instruction at index {self.program_counter}")
                sys.exit(1)
