#include "mips.h"

/******************************************************************************
 *      DO NOT MODIFY THE CODE BELOW
 ******************************************************************************/
#ifndef CS2100_ROUTINE_MASK_OUT
uint32_t _PC;
int32_t _RF[32] = {0};
int32_t _DataMemory[MAX_MEM >> 2] = {0};

// All the control signals needed
bool _RegDst;
bool _ALUSrc;
bool _MemtoReg;
bool _RegWrite;
bool _MemRead;
bool _MemWrite;
bool _Branch;
uint8_t _ALUOp;
uint8_t _ALUCtrl;

void RegFile(uint8_t RR1, uint8_t RR2, uint8_t WR, int32_t WD, int32_t *RD1,
             int32_t *RD2, bool RegWrite) {
  // Because we need to send out multiple outputs,
  // we will use passing by pointers.
  *RD1 = (RR1 > 0) ? _RF[RR1] : 0;
  *RD2 = (RR2 > 0) ? _RF[RR2] : 0;

  if (RegWrite && WR)
    _RF[WR] = WD;
}

int32_t Memory(uint32_t Address, int32_t WrData, bool MemRead, bool MemWrite) {
  // We can do a sanity check here.
  // You can at most do one memory operation.
  // Will assume that "error" raises hell.
  if (MemRead && MemWrite) {
    error("Cannot do both read and write at the same time.");
  }

  if (!(MemRead || MemWrite)) {
    return 0;
  }

  if ((Address > MAX_MEM) || (Address > MAX_MEM)) {
    error("Address %u is out of range. Simulator exiting...\n", Address);
  }

  if (MemRead) {
    return _DataMemory[Address >> 2];
  }

  if (MemWrite) {
    _DataMemory[Address >> 2] = WrData;
  }

  return 0;
}
#endif
/******************************************************************************
 *      DO NOT MIDIFY THE CODE ABOVE
 ******************************************************************************/

// Here starts your code for Assignment 2 Part A
// If you need to define some macros, you can do so below this comment.

#ifndef ASSIGNMENT2_QUESTION1A

uint8_t mux_u8(bool ctrl, uint8_t in0, uint8_t in1) {
  if (ctrl) {
    return in1;
  } else {
    return in0;
  }
}

uint32_t mux_u32(bool ctrl, uint32_t in0, uint32_t in1) {
  if (ctrl) {
    return in1;
  } else {
    return in0;
  }
}

int32_t mux_i32(bool ctrl, int32_t in0, int32_t in1) {
  if (ctrl) {
    return in1;
  } else {
    return in0;
  }
}

#endif // End of Assignment 2, Question 1a

#ifndef ASSIGNMENT2_QUESTION1B

void decode(uint32_t in, struct instr *insn) {
  insn->opcode = (in >> 26) & 0x3F; // Bits 31-26
  insn->rs = (in >> 21) & 0x1F;     // Bits 25-21
  insn->rt = (in >> 16) & 0x1F;     // Bits 20-16
  insn->rd = (in >> 11) & 0x1F;     // Bits 15-11
  insn->shamt = (in >> 6) & 0x1F;   // Bits 10-6
  insn->funct = in & 0x3F;          // Bits 5-0
  insn->immed = in & 0xFFFF;        // Bits 15-0
  insn->address = in & 0x3FFFFFF;   // Bits 25-0
}

#endif // End of Assignment 2, Question 1b

#ifndef ASSIGNMENT2_QUESTION2A
void Control(uint8_t opcode, bool *_RegDst, bool *_ALUSrc, bool *_MemtoReg,
             bool *_RegWrite, bool *_MemRead, bool *_MemWrite, bool *_Branch,
             uint8_t *_ALUOp) {
  // Default values
  *_RegDst = false;
  *_ALUSrc = false;
  *_MemtoReg = false;
  *_RegWrite = false;
  *_MemRead = false;
  *_MemWrite = false;
  *_Branch = false;
  *_ALUOp = 0;

  // Set control signals based on the opcode
  switch (opcode) {
  case 0: // R-type instructions
    *_RegDst = true;
    *_ALUSrc = false;
    *_RegWrite = true;
    *_ALUOp = 2;
    break;
  case 35: // lw
    *_MemRead = true;
    *_MemtoReg = true;
    *_ALUOp = 0;
    break;
  case 43: // sw
    *_MemWrite = true;
    break;
  case 4: // beq
    *_ALUOp = 1;
    *_Branch = true;
    break;
  default:
    // Handle other opcodes if necessary
    break;
  }
}

#endif // End of Assignment 2, Question 2a

#ifndef ASSIGNMENT2_QUESTION2B
uint8_t ALUControl(uint8_t _ALUOp, uint8_t _funct) {
  if (_ALUOp == 2) { // R-type instruction
    // Need to decode the funct code.
    switch (_funct) {
    case 0x20:    // add
    case 0x21:    // addu
      return 2;   // ALU to perform Add
    case 0x22:    // sub
    case 0x23:    // subu
      return 6;   // ALU to perform Sub
    case 0x24:    // and
      return 0;   // ALU to perform And
    case 0x25:    // or
      return 1;   // ALU to perform Or
    case 0x27:    // nor
      return 0xC; // Nor
    case 0x2A:    // slt
      return 7;   // ALU to perform Set Less Than
    default:
      // Handle any other funct values if necessary
      // Raise an error if none of the cases match.
      error("Unknown funct code: 0x%X", _funct);
      break;
    }
  } else { // Non R-type
    if (_ALUOp == 0)
      return 2; // ALU to perform Add
    if (_ALUOp == 1)
      return 6; // ALU to perform Sub
  }

  // If no matching case is found, return a default value or raise an error.
  return -1; // You can return -1 as an error indicator if needed.
}

#endif // End of Assignment 2, Question 2b

#ifndef ASSIGNMENT2_QUESTION2C
int32_t ALU(int32_t in0, int32_t in1, uint8_t ALUControl, bool *ALUiszero) {
  int32_t result;

  switch (ALUControl) {
  case 0:
    result = in0 & in1;
    break;
  case 1:
    result = in0 | in1;
    break;
  case 2:
    result = in0 + in1;
    break;
  case 6:
    result = in0 - in1;
    break;
  case 7:
    result = (int32_t)(in0 < in1);
    break;
  case 12:
    result = ~(in0 | in1);
    break;
  default:
    // Handle any other ALUControl values as needed.
    // Return an error code or raise an error if necessary.
    break;
  }

  *ALUiszero = (result == 0);
  return result;
}

#endif // End of Assignment 2, Question 2c

#ifndef ASSIGNMENT2_QUESTION3

void execute(uint32_t instruction) {
  // Decode stage
  struct instr decoded_instr;
  decode(instruction, &decoded_instr);

  // Control unit
  bool RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch;
  uint8_t ALUOp;
  Control(decoded_instr.opcode, &RegDst, &ALUSrc, &MemtoReg, &RegWrite,
          &MemRead, &MemWrite, &Branch, &ALUOp);

  // Register file read
  int32_t RD1, RD2;
  if (decoded_instr.rs > 0) {
    RegFile(decoded_instr.rs, decoded_instr.rt, 0, 0, &RD1, &RD2, false);
  } else {
    error("Invalid register access.");
    return; // Exit the execute method due to the error
  }

  // ALU calculation
  int32_t ALU_result;
  bool ALU_is_zero;
  uint8_t ALUOpControl = ALUControl(ALUOp, decoded_instr.funct);
  if (ALUSrc) {
    ALU_result = ALU(RD1, decoded_instr.immed, ALUOpControl, &ALU_is_zero);
  } else {
    ALU_result = ALU(RD1, RD2, ALUOpControl, &ALU_is_zero);
  }

  // Memory stage (only for load and store instructions)
  int32_t MemData;
  if (MemRead) {
    if (ALU_result >= 0 && ALU_result < MAX_MEM) {
      MemData = Memory(ALU_result, 0, true, false);
    } else {
      error("Invalid memory read address.");
      return; // Exit the execute method due to the error
    }
  } else if (MemWrite) {
    if (ALU_result >= 0 && ALU_result < MAX_MEM) {
      Memory(ALU_result, RD2, false, true);
    } else {
      error("Invalid memory write address.");
      return; // Exit the execute method due to the error
    }
  }

  // Write-back stage
  int32_t WriteData = MemtoReg ? MemData : ALU_result;
  int32_t WriteReg = RegDst ? decoded_instr.rd : decoded_instr.rt;

  if (RegWrite) {
    int32_t RD1 = -1; // Sentinel value to indicate "no value"
    int32_t RD2 = -1; // Sentinel value to indicate "no value"

    if (WriteReg > 0) {
      if (decoded_instr.rs > 0) {
        RD1 = _RF[decoded_instr.rs]; // Read from source register 1
      }

      if (decoded_instr.rt > 0) {
        RD2 = _RF[decoded_instr.rt]; // Read from source register 2
      }

      if (RD1 != -1 && RD2 != -1) {
        RegFile(0, 0, WriteReg, WriteData, &RD1, &RD2, true);
      } else {
        // Handle sentinel values indicating "no value"
        error("Sentinel value in RD1 or RD2.");
        return; // Exit the execute method due to the error
      }
    } else {
      // Handle invalid register write access (e.g., raise an error)
      error("Invalid register write access.");
      return; // Exit the execute method due to the error
    }
  }

  // Update the PC
  if (Branch && ALU_is_zero) {
    _PC += (decoded_instr.immed << 2);
  } else {
    _PC += 4;
  }
}

#endif // End of Assignment 2, Question 3