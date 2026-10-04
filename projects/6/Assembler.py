
import sys
from pathlib import Path

symbolDict = {f"R{i}": i for i in range(16)}
symbolDict.update({
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
})

destDict = {
    "":"000",
    "M":"001",
    "D":"010",
    "MD":"011",
    "A":"100",
    "AM":"101",
    "AD":"110",
    "AMD":"111"
}

compDict = {
    "0":"0101010",
    "1":"0111111",
    "-1":"0111010",
    "D":"0001100",
    "A":"0110000",
    "M":"1110000",
    "!D":"0001101",
    "!A":"0110001",
    "!M":"1110001",
    "-D":"0001111",
    "-A":"0110011",
    "-M":"1110011",
    "D+1":"0011111",
    "A+1":"0110111",
    "M+1":"1110111",
    "D-1":"0001110",
    "A-1":"0110010",
    "M-1":"1110010",
    "D+A":"0000010",
    "D+M":"1000010",
    "D-A":"0010011",
    "D-M":"1010011",
    "A-D":"0000111",
    "M-D":"1000111",
    "D&A":"0000000",
    "D&M":"1000000",
    "D|A":"0010101",
    "D|M":"1010101"
}

jumpDict = {
    "":"000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"
}

def encode_A(address):
    if not 0 <= address < 2**15:
        raise ValueError("A instruction address should fit into 15 bit")
    
    return "0" + format(address,"015b")

def encode_C(comp, dest="", jump=""):
    return "111" + compDict[comp] + destDict[dest] + jumpDict[jump]

lines = []

input_path = Path(sys.argv[1])
output_path = input_path.with_suffix(".hack")

with open(input_path, encoding="utf-8") as source:
    for raw_line in source:
        line = raw_line.split("//", 1)[0].strip()
        if not line:
            continue
        lines.append(line)

counter = 0

for line in lines:
    if(line.startswith("(")):
        symbol = line[1:-1]
        symbolDict[symbol] = counter
    else:
        counter += 1

next_variable_address = 16

with open(output_path, "w", encoding="utf-8") as output:
    
    for line in lines:
        if(line.startswith("(")):
            continue

        if(line.startswith("@")):
            value = line[1:]
            if value.isdigit():
                address = int(value)
            else:
                if value not in symbolDict:
                    symbolDict[value] = next_variable_address
                    next_variable_address += 1

                address = symbolDict[value]

            bits = encode_A(address)
        
        else:
            dest=""
            jump=""
            remaining = line

            if ';' in remaining:
                remaining, jump = remaining.split(';', 1)

            if '=' in remaining:
                dest, remaining = remaining.split('=', 1)            

            comp = remaining

            bits = encode_C(comp,dest,jump)

        output.write(bits + '\n')