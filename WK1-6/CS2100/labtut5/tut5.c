


// q3 ---------------------
#include <stdint.h>

// Define the struct for an instruction
struct insn {
  // Common fields for all instruction types
  uint6_t opcode;

  // Fields specific to R-type instructions
  uint5_t rs;
  uint5_t rt;
  uint5_t rd;
  uint5_t shamt;
  uint6_t funct;

  // Fields specific to I-type instructions
  int16_t immediate;

  // Fields specific to J-type instructions
  uint26_t targetaddress;
};

// q4 ---------------------
#include <stdbool.h>
#include <stdint.h>

void Control(uint6_t opcode, bool *_RegDst, bool *_MemRead, bool *_MemtoReg,
             uint2_t *_ALUOp, bool *_MemWrite, bool *_ALUSrc, bool *_RegWrite) {

  // Default values for the signals
  *_RegDst = false;
  *_MemRead = false;
  *_MemtoReg = false;
  *_ALUOp = 0;
  *_MemWrite = false;
  *_ALUSrc = false;
  *_RegWrite = false;

  // Compute the signals based on the opcode
  switch (opcode) {
  case 0x00: // R-type instruction
    *_RegDst = true;
    *_ALUOp = 0x0;
    *_RegWrite = true;
    break;
  case 0x23: // Load word (LW)
    *_MemRead = true;
    *_MemtoReg = true;
    *_ALUSrc = true;
    *_RegWrite = true;
    break;
  case 0x2B: // Store word (SW)
    *_MemWrite = true;
    *_ALUSrc = true;
    break;
  // Add more cases for other opcodes as needed
  default:
    // Handle unsupported opcodes or provide default values
    break;
  }
}

// q5 ----------------
#include <stdint.h>

uint4_t ALUControl(uint2_t _ALUOp, uint6_t _funct) {
  // Default ALU control signal
  uint4_t aluControlSignal = 0;

  // Determine ALU control signal based on _ALUOp and _funct
  if (_ALUOp == 0) {
    // R-type instruction
    switch (_funct) {
    case 0x20:                // Add
      aluControlSignal = 0x2; // 0010
      break;
    case 0x22:                // Subtract
      aluControlSignal = 0x6; // 0110
      break;
    case 0x24:                // AND
      aluControlSignal = 0x0; // 0000
      break;
    case 0x25:                // OR
      aluControlSignal = 0x1; // 0001
      break;
    case 0x2A:                // Set on Less Than
      aluControlSignal = 0x7; // 0111
      break;
    default:
      // Handle unsupported _funct values or provide a default value
      break;
    }
  } else if (_ALUOp == 1) {
    // I-type instruction with ALUOp = 01 (e.g., LW, SW)
    aluControlSignal = 0x2; // 0010 (Add)
  } else if (_ALUOp == 2) {
    // I-type instruction with ALUOp = 10 (e.g., BEQ)
    aluControlSignal = 0x6; // 0110 (Subtract)
  } else if (_ALUOp == 3) {
    // I-type instruction with ALUOp = 11 (e.g., Immediate operations)
    // You can set the ALU control signal for I-type ALU operations here.
    // Adjust this part based on your specific architecture.
  }

  return aluControlSignal;
}


// q6 -----------------
#include <stdbool.h>
#include <stdint.h>

int32_t ALU(int32_t in0, int32_t in1, uint4_t ALUControl, bool *ALUiszero) {
  int32_t result = 0;

  switch (ALUControl) {
  case 0x0: // ALUControl = 0000 (AND)
    result = in0 & in1;
    break;
  case 0x1: // ALUControl = 0001 (OR)
    result = in0 | in1;
    break;
  case 0x2: // ALUControl = 0010 (ADD)
    result = in0 + in1;
    break;
  case 0x6: // ALUControl = 0110 (SUB)
    result = in0 - in1;
    break;
  case 0x7: // ALUControl = 0111 (SLT: Set on Less Than)
    result = (in0 < in1) ? 1 : 0;
    break;
    // Add more cases for other ALUControl values as needed

  default:
    // Handle unsupported ALUControl values or provide a default behavior
    break;
  }

  // Set ALUiszero based on the result
  *ALUiszero = (result == 0);

  return result;
}