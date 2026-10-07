import sys
from pathlib import Path


input_path = Path(sys.argv[1])
output_path = input_path.with_suffix(".asm")

with input_path.open(encoding="utf-8") as source, \
     output_path.open("w", encoding="utf-8") as output:
    
    for raw_line in source:
        line = raw_line.split("//", 1)[0].strip()
        if not line:
            continue

        parts = line.split()

        if(parts[0] == "push"):

            if(parts[1] == "constant"):

                output.write(
                    f"@{parts[2]}\n"  
                    "D=A\n"
                    "@SP\n"
                    "A=M\n"
                    "M=D\n"
                    "@SP\n"
                    "M=M+1\n"
                )

        if(parts[0] == "add"):

            output.write(
                "@SP\n"
                "M=M-1\n"
                "A=M\n"
                "D=M\n"
                "A=A-1\n"
                "M=D+M\n"
            )