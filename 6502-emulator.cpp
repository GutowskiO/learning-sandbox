#include <stdio.h>
#include <stdlib.h>


// http://www.6502.org/users/obelisk/
// https://en.wikipedia.org/wiki/MOS_Technology_6502
// https://www.masswerk.at/6502/6502_instruction_set.html
// https://sta.c64.org/cbm64mem.html 
// https://www.c64-wiki.com/wiki/Reset_(Process)

using Byte = unsigned char;
using Word = unsigned short;

using u32 = unsigned int;

struct Mem {
	static u32 constexpr MAX_MEM = 1024 * 64; // 64KB memory
	Byte Data[MAX_MEM];

	void Initialise() {
		for (u32 i = 0; i < MAX_MEM; ++i) {
			Data[i] = 0; // clear memory
		}
	}
	// rad 1 byte from memory
	Byte operator[](u32 Address) const {

		return Data[Address];
		
	}
	// write 1 byte to memory
	Byte& operator[](u32 Address) {

		return Data[Address];

	}
};

struct CPU {
	Word PC; // program counter
	Byte SP; // stack pointer

	Byte A, X, Y; // registers

	Byte C : 1; //status flag
	Byte Z : 1; // zero flag
	Byte I : 1; // interrupt disable
	Byte D : 1; // decimal mode
	Byte B : 1; // break command
	Byte V : 1; // overflow flag
	Byte N : 1; // negative flag

	void Reset(Mem& memory) {
		PC = 0xFFFC; // reset vector
		SP = 0xFF; // stack pointer starts at 0xFF
		D = 0; // decimal mode off
		A = X = Y = 0; // registers cleared
		C = Z = I = B = V = N = 0; // status flags cleared
		memory.Initialise();
	}

	Byte FetchByte(u32& Cycles, Mem& memory) {

		Byte Data = memory[PC];
		PC++;
		Cycles--;
		return Data;
	}

	static constexpr Byte
		INS_LDA_IM = 0xA9; // Load Accumulator Immediate

	void Execute(u32 Cycles, Mem& memory) {
		while (Cycles > 0) {
			Byte Ins = FetchByte(Cycles, memory);
			switch (Ins)
			{
			case INS_LDA_IM: { // Load Accumulator Immediate
				Byte Value =
					FetchByte(Cycles, memory);
				A = Value; // Load value into accumulator
				Z = (A == 0);
				N = (A & 0b10000000) != 0; // set negative flag if bit 7 is set
				break;
			}
			default: {
				printf("Instruction not handled %d", Ins);
			} break;
			}
		}
	}
};

int main() {
	Mem mem;
	CPU cpu;
	cpu.Reset(mem);
	mem[0xFFFC] = CPU::INS_LDA_IM; // Set the reset vector to point to LDA immediate instruction
	mem[0xFFFD] = 0x42; // Load immediate value 0x42
	cpu.Execute(2, mem);
	 
	return 0;
}