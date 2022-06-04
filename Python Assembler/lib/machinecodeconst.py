#
# @author:Don Dennis
# machinecodeconst.py
#
# Constants and variable declaring various
# machine instructions


class MachineCodeConst:
    # Definition of opcodes used in assembly language instructions
    INSTR_LUI = 'lui'
    INSTR_AUIPC = 'auipc'
    INSTR_JAL = 'jal'
    INSTR_JALR = 'jalr'
    INSTR_BEQ = 'beq'
    INSTR_BNE = 'bne'
    INSTR_BLT = 'blt'
    INSTR_BGE = 'bge'
    INSTR_BLTU = 'bltu'
    INSTR_BGEU = 'bgeu'
    INSTR_LB = 'lb'
    INSTR_LH = 'lh'
    INSTR_LW = 'lw'
    INSTR_LBU = 'lbu'
    INSTR_LHU = 'lhu'
    INSTR_SB = 'sb'
    INSTR_SH = 'sh'
    INSTR_SW = 'sw'
    INSTR_ADDI = 'addi'
    INSTR_SLTI = 'slti'
    INSTR_SLTIU = 'sltiu'
    INSTR_XORI = 'xori'
    INSTR_ORI = 'ori'
    INSTR_ANDI = 'andi'
    INSTR_SLLI = 'slli'
    INSTR_SRLI = 'srli'
    INSTR_SRAI = 'srai'
    INSTR_ADD = 'add'
    INSTR_SUB = 'sub'
    INSTR_SLL = 'sll'
    INSTR_SLT = 'slt'
    INSTR_SLTU = 'sltu'
    INSTR_XOR = 'xor'
    INSTR_SRL = 'srl'
    INSTR_SRA = 'sra'
    INSTR_OR = 'or'
    INSTR_AND = 'and'
    # compressed type R1
    INSTR_CADD = 'cadd'
    INSTR_CMV = 'cmv'
    # compressed type I1
    INSTR_CADDI = 'caddi'
    INSTR_CLUI = 'clui'
    INSTR_CSLLI = 'cslli'
    INSTR_CLI = 'cli'
    # compressed type I2
    INSTR_CSRLI = 'csrli'
    INSTR_CSRAI = 'csrai'
    INSTR_CANDI = 'candi'

    # compressed type R2
    INSTR_CSUB = 'csub'
    INSTR_CXOR = 'cxor'
    INSTR_COR = 'cor'
    INSTR_CAND = 'cand'
    # compressed load store
    INSTR_CLW = 'clw'
    INSTR_CSW = 'csw'
    # floating point

    # All reserved opcodes
    ALL_INSTR = [INSTR_LUI, INSTR_AUIPC, INSTR_JAL,
                 INSTR_JALR, INSTR_BEQ, INSTR_BNE, INSTR_BLT,
                 INSTR_BGE, INSTR_BLTU, INSTR_BGEU, INSTR_LB,
                 INSTR_LH, INSTR_LW, INSTR_LBU, INSTR_LHU,
                 INSTR_SB, INSTR_SH, INSTR_SW, INSTR_ADDI,
                 INSTR_SLTI, INSTR_SLTIU, INSTR_XORI,
                 INSTR_ORI, INSTR_ANDI, INSTR_SLLI,
                 INSTR_SRLI, INSTR_SRAI, INSTR_ADD,
                 INSTR_SUB, INSTR_SLL, INSTR_SLT,
                 INSTR_SLTU, INSTR_XOR, INSTR_SRL,
                 INSTR_SRA, INSTR_OR, INSTR_AND,
                 INSTR_CADDI,
                 INSTR_CADD, INSTR_CMV,
                 INSTR_CLW, INSTR_CSW, INSTR_CSUB, INSTR_CXOR, INSTR_COR,
                 INSTR_CAND, INSTR_CSRLI, INSTR_CSRAI, INSTR_CANDI,
                 INSTR_CLUI, INSTR_CSLLI, INSTR_CLI
                 ]
    # All instruction in a type
    INSTR_TYPE_U = [INSTR_LUI, INSTR_AUIPC]
    INSTR_TYPE_UJ = [INSTR_JAL]
    INSTR_TYPE_S = [INSTR_SW, INSTR_SB, INSTR_SH]
    INSTR_TYPE_SB = [INSTR_BEQ, INSTR_BNE, INSTR_BLT,
                     INSTR_BLTU, INSTR_BGE, INSTR_BGEU]
    INSTR_TYPE_I = [INSTR_ADDI, INSTR_SLTI, INSTR_SLTIU,
                    INSTR_ORI, INSTR_XORI, INSTR_ANDI,
                    INSTR_SLLI, INSTR_SRLI, INSTR_SRAI,
                    INSTR_JALR, INSTR_LW, INSTR_LB,
                    INSTR_LH, INSTR_LBU, INSTR_LHU]
    INSTR_TYPE_R = [INSTR_ADD, INSTR_SUB, INSTR_SLL,
                    INSTR_SLT, INSTR_SLTU, INSTR_XOR,
                    INSTR_SRL, INSTR_SRA, INSTR_OR, INSTR_AND]
    INSTR_TYPE_CI1 = [INSTR_CADDI,
                      INSTR_CLUI,
                      INSTR_CSLLI,
                      INSTR_CLI
                      ]
    INSTR_TYPE_CI2 = [INSTR_CSRLI,
                      INSTR_CSRAI,
                      INSTR_CANDI,
                      ]

    INSTR_TYPE_CR1 = [INSTR_CADD,
                      INSTR_CMV
                      ]
    INSTR_TYPE_CR2 = [INSTR_CSUB,
                      INSTR_CXOR,
                      INSTR_COR,
                      INSTR_CAND
                      ]
    INSTR_TYPE_CLS = [INSTR_CLW,
                      INSTR_CSW
                      ]

    # Binary Opcodes
    BOP_LUI = '0110111'
    BOP_AUIPC = '0010111'
    BOP_JAL = '1101111'
    BOP_JALR = '1100111'
    BOP_BRANCH = '1100011'
    BOP_LOAD = '0000011'
    BOP_STORE = '0100011'
    BOP_ARITHI = '0010011'
    BOP_ARITH = '0110011'
    # Not supported
    # [FENCE, FENCE.I]
    BOP_MISCMEM = '0001111'
    # [ ECALL, EBREAK, CSRRW, CSRRS, cSRRC, CSRRWI, CSRRSI, CSRRCI]
    BOP_SYSTEM = '1110011'
    # Compressed
    BOP_CI = '01'
    BOP_CR = '10'
    BOP_CLS = '00'

    # The instruction in each distinct binary opcode
    INSTR_BOP_LUI = [INSTR_LUI]
    INSTR_BOP_AUIPC = [INSTR_AUIPC]
    INSTR_BOP_JAL = [INSTR_JAL]
    INSTR_BOP_JALR = [INSTR_JALR]
    INSTR_BOP_BRANCH = [INSTR_BEQ, INSTR_BNE, INSTR_BLT,
                        INSTR_BLTU, INSTR_BGE, INSTR_BGEU]
    INSTR_BOP_LOAD = [INSTR_LW, INSTR_LB,
                      INSTR_LH, INSTR_LBU, INSTR_LHU]
    INSTR_BOP_STORE = [INSTR_SW, INSTR_SB, INSTR_SH]
    INSTR_BOP_ARITHI = [INSTR_ADDI, INSTR_SLTI, INSTR_SLTIU,
                        INSTR_ORI, INSTR_XORI, INSTR_ANDI,
                        INSTR_SLLI, INSTR_SRLI, INSTR_SRAI]
    INSTR_BOP_ARITH = [INSTR_ADD, INSTR_SUB, INSTR_SLL,
                       INSTR_SLT, INSTR_SLTU, INSTR_XOR,
                       INSTR_SRL, INSTR_SRA, INSTR_OR, INSTR_AND]
    INSTR_BOP_CI1 = [INSTR_CADDI,
                     INSTR_CLUI,
                     INSTR_CSLLI,
                     INSTR_CLI
                     ]
    INSTR_BOP_CI2 = [INSTR_CSRLI,
                     INSTR_CSRAI,
                     INSTR_CANDI,
                     ]
    INSTR_BOP_CR1 = [INSTR_CADD,
                     INSTR_CMV,
                     INSTR_CSLLI
                     ]
    INSTR_BOP_CR2 = [INSTR_CSUB,
                     INSTR_CXOR,
                     INSTR_COR,
                     INSTR_CAND
                     ]
    INSTR_BOP_CLS = [INSTR_CLW,
                     INSTR_CSW
                     ]

    # FUNCT for each instruction type
    FUNCT3_ARITHI = {
        INSTR_ADDI: '000',
        INSTR_SLTI: '010',
        INSTR_SLTIU: '011',
        INSTR_ORI: '110',
        INSTR_XORI: '100',
        INSTR_ANDI: '111',
        INSTR_SLLI: '001',
        INSTR_SRLI: '101',
        INSTR_SRAI: '101'
    }

    FUNCT3_JALR = {
        INSTR_JALR: '000'
    }

    FUNCT3_LOAD = {
        INSTR_LB: '000',
        INSTR_LH: '001',
        INSTR_LW: '010',
        INSTR_LBU: '100',
        INSTR_LHU: '101'
    }

    FUNCT3_ARITH = {
        INSTR_ADD: '000',
        INSTR_SUB: '000',
        INSTR_SLL: '001',
        INSTR_SLT: '010',
        INSTR_SLTU: '011',
        INSTR_XOR: '100',
        INSTR_SRL: '101',
        INSTR_SRA: '101',
        INSTR_OR: '110',
        INSTR_AND: '111'
    }

    FUNCT7_ARITH = {
        INSTR_ADD: '0000000',
        INSTR_SUB: '0100000',
        INSTR_SLL: '0000000',
        INSTR_SLT: '0000000',
        INSTR_SLTU: '0000000',
        INSTR_XOR: '0000000',
        INSTR_SRL: '0000000',
        INSTR_SRA: '0100000',
        INSTR_OR: '0000000',
        INSTR_AND: '0000000'
    }

    FUNCT3_STORE = {
        INSTR_SB: '000',
        INSTR_SH: '001',
        INSTR_SW: '010'
    }

    FUNCT3_BRANCH = {
        INSTR_BEQ: '000',
        INSTR_BNE: '001',
        INSTR_BLT: '100',
        INSTR_BGE: '101',
        INSTR_BLTU: '110',
        INSTR_BGEU: '111'
    }
    # compressed
    FUNCT3_C = {
        INSTR_CADDI: '000',
        INSTR_CLI: '010',
        INSTR_CLUI: '011',
        INSTR_CSRLI: '100',
        INSTR_CSRAI: '100',
        INSTR_CANDI: '100',
        INSTR_CSLLI: '000',
        INSTR_CLW: '010',
        INSTR_CSW: '110'
    }

    FUNCT4_C = {
        INSTR_CADD: '1001',
        INSTR_CMV: '1000',
        INSTR_CSUB: '1000',
        INSTR_COR: '1000',
        INSTR_CXOR: '1000',
        INSTR_CAND: '1000',
    }

    FUNCT21_C = {
        INSTR_CSUB: '11',
        INSTR_COR: '11',
        INSTR_CXOR: '11',
        INSTR_CAND: '11',
        INSTR_CANDI: '10',
        INSTR_CSRLI: '00',
        INSTR_CSRAI: '01'
    }
    FUNCT22_C = {
        INSTR_CSUB: '00',
        INSTR_COR: '10',
        INSTR_CXOR: '01',
        INSTR_CAND: '11'
    }
