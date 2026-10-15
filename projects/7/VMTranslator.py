import sys
from pathlib import Path


input_path = Path(sys.argv[1])
output_path = input_path.with_suffix(".asm")

with input_path.open(encoding="utf-8") as source, \
     output_path.open("w", encoding="utf-8") as output:

    eq_counter = 0
    gt_counter = 0
    lt_counter = 0
    
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

            if(parts[1] == "local"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@LCL\n"
                    "A=D+M\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )
                

            if(parts[1] == "argument"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@ARG\n"
                    "A=D+M\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )

            if(parts[1] == "this"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@THIS\n"
                    "A=D+M\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )

            if(parts[1] == "that"):
                
                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@THAT\n"
                    "A=D+M\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )

            if(parts[1] == "temp"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@R5\n"
                    "A=D+A\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )

            if(parts[1] == "pointer"):

                if(parts[2] == "0"):
                    
                    output.write(
                        "@THIS\n"
                        "D=M\n"

                        "@SP\n"
                        "A=M\n"
                        "M=D\n"

                        "@SP\n"
                        "M=M+1\n"
                    )
                
                else:

                    output.write(
                        "@THAT\n"
                        "D=M\n"

                        "@SP\n"
                        "A=M\n"
                        "M=D\n"

                        "@SP\n"
                        "M=M+1\n"
                    )

            if(parts[1] == "static"):
                
                file_name = input_path.stem
                index = parts[2]

                output.write(
                    f"@{file_name}.{index}\n"
                    "D=M\n"

                    "@SP\n"
                    "A=M\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M+1\n"
                )

        if(parts[0] == "pop"):

            if(parts[1] == "local"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@LCL\n"
                    "M=D+M\n"

                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    "@LCL\n"
                    "A=M\n"
                    "M=D\n"

                    f"@{parts[2]}\n"
                    "D=A\n"                    

                    "@LCL\n"
                    "M=M-D\n"

                    "@SP\n"
                    "M=M-1\n"
                )

            if(parts[1] == "argument"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@ARG\n"
                    "M=D+M\n"

                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    "@ARG\n"
                    "A=M\n"
                    "M=D\n"

                    f"@{parts[2]}\n"
                    "D=A\n"                    

                    "@ARG\n"
                    "M=M-D\n"

                    "@SP\n"
                    "M=M-1\n"
                )

            if(parts[1] == "this"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@THIS\n"
                    "M=D+M\n"

                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    "@THIS\n"
                    "A=M\n"
                    "M=D\n"

                    f"@{parts[2]}\n"
                    "D=A\n"                    

                    "@THIS\n"
                    "M=M-D\n"

                    "@SP\n"
                    "M=M-1\n"
                )

            if(parts[1] == "that"):

                output.write(
                    f"@{parts[2]}\n"
                    "D=A\n"

                    "@THAT\n"
                    "M=D+M\n"

                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    "@THAT\n"
                    "A=M\n"
                    "M=D\n"

                    f"@{parts[2]}\n"
                    "D=A\n"                    

                    "@THAT\n"
                    "M=M-D\n"

                    "@SP\n"
                    "M=M-1\n"
                )

            if(parts[1] == "temp"):

                target = 5 + int(parts[2])

                output.write(
                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    f"@R{target}\n"
                    "M=D\n"
                    
                    "@SP\n"
                    "M=M-1\n"
                )

            if(parts[1] == "pointer"):

                if(parts[2] == "0"):

                    output.write(
                        "@SP\n"
                        "A=M-1\n"
                        "D=M\n"

                        "@THIS\n"
                        "M=D\n"

                        "@SP\n"
                        "M=M-1\n"
                    )

                else:

                    output.write(
                        "@SP\n"
                        "A=M-1\n"
                        "D=M\n"

                        "@THAT\n"
                        "M=D\n"

                        "@SP\n"
                        "M=M-1\n"
                    )
            
            if(parts[1] == "static"):
                
                file_name = input_path.stem
                index = parts[2]

                output.write(
                    "@SP\n"
                    "A=M-1\n"
                    "D=M\n"

                    f"@{file_name}.{index}\n"
                    "M=D\n"

                    "@SP\n"
                    "M=M-1\n"
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

        if(parts[0] == "sub"):

            output.write(
                "@SP\n"
                "M=M-1\n"
                "A=M\n"
                "D=M\n"
                "A=A-1\n"
                "M=M-D\n"
            )

        if(parts[0] == "neg"):

            output.write(
                "@SP\n"
                "A=M\n"
                "A=A-1\n"
                "M=-M\n"
            )


        if(parts[0] == "eq"):

            output.write(
                "@SP\n"
                "M=M-1\n"
                "A=M\n"
                "D=M\n"
                "A=A-1\n"
                "D=D-M\n"
                
                f"@EQ_TRUE_{eq_counter}\n"
                "D;JEQ\n"
                
                f"@EQ_FALSE_{eq_counter}\n"
                "D;JNE\n"
                
                f"(EQ_TRUE_{eq_counter})\n"
                "D=-1\n"
                f"@EQ_END_{eq_counter}\n"
                "0;JMP\n"
                
                f"(EQ_FALSE_{eq_counter})\n"
                "D=0\n"
                f"@EQ_END_{eq_counter}\n"
                "0;JMP\n"
                
                f"(EQ_END_{eq_counter})\n"
                "@SP\n"
                "A=M-1\n"
                "M=D\n"
            )
            eq_counter += 1

        if(parts[0] == "gt"):

            output.write(
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "D=M\n"
                
                f"@GT_X_NEG_{gt_counter}\n"
                "D;JLT\n"
                
                "@SP\n"
                "A=M-1\n"
                "D=M\n"

                f"@GT_TRUE_{gt_counter}\n"
                "D;JLT\n"

                f"@GT_COMPARE_{gt_counter}\n"
                "0;JMP\n"


                f"(GT_X_NEG_{gt_counter})\n"
                
                "@SP\n"
                "A=M-1\n"
                "D=M\n"                

                f"@GT_FALSE_{gt_counter}\n"
                "D;JGE\n"

                f"@GT_COMPARE_{gt_counter}\n"
                "0;JMP\n"

                f"(GT_COMPARE_{gt_counter})\n"
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "D=M\n"

                "@SP\n"
                "A=M-1\n"
                "D=D-M\n"
                
                f"@GT_TRUE_{gt_counter}\n"
                "D;JGT\n"
                
                f"@GT_FALSE_{gt_counter}\n"
                "D;JLE\n"
                
                f"(GT_TRUE_{gt_counter})\n"
                "D=-1\n"
                f"@GT_END_{gt_counter}\n"
                "0;JMP\n"
                
                f"(GT_FALSE_{gt_counter})\n"
                "D=0\n"
                f"@GT_END_{gt_counter}\n"
                "0;JMP\n"
                
                f"(GT_END_{gt_counter})\n"
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "M=D\n"
                "@SP\n"
                "M=M-1\n"
            )
            gt_counter += 1

        if(parts[0] == "lt"):

            output.write(
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "D=M\n"
                
                f"@LT_X_NEG_{lt_counter}\n"
                "D;JLT\n"
                
                "@SP\n"
                "A=M-1\n"
                "D=M\n"

                f"@LT_FALSE_{lt_counter}\n"
                "D;JLT\n"

                f"@LT_COMPARE_{lt_counter}\n"
                "0;JMP\n"


                f"(LT_X_NEG_{lt_counter})\n"
                
                "@SP\n"
                "A=M-1\n"
                "D=M\n"                

                f"@LT_TRUE_{lt_counter}\n"
                "D;JGE\n"

                f"@LT_COMPARE_{lt_counter}\n"
                "0;JMP\n"

                f"(LT_COMPARE_{lt_counter})\n"
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "D=M\n"

                "@SP\n"
                "A=M-1\n"
                "D=D-M\n"
                
                f"@LT_TRUE_{lt_counter}\n"
                "D;JLT\n"
                
                f"@LT_FALSE_{lt_counter}\n"
                "D;JGE\n"
                
                f"(LT_TRUE_{lt_counter})\n"
                "D=-1\n"
                f"@LT_END_{lt_counter}\n"
                "0;JMP\n"
                
                f"(LT_FALSE_{lt_counter})\n"
                "D=0\n"
                f"@LT_END_{lt_counter}\n"
                "0;JMP\n"
                
                f"(LT_END_{lt_counter})\n"
                "@SP\n"
                "A=M-1\n"
                "A=A-1\n"
                "M=D\n"
                "@SP\n"
                "M=M-1\n"
            )
            lt_counter += 1

        if(parts[0] == "not"):

            output.write(
                "@SP\n"
                "A=M-1\n"
                "M=!M\n"
            )

        if(parts[0] == "and"):

            output.write(
                "@SP\n"
                "M=M-1\n"
                "A=M\n"
                "D=M\n"

                "A=A-1\n"
                "D=D&M\n"
                "M=D\n"
            )

        if(parts[0] == "or"):

            output.write(
                "@SP\n"
                "M=M-1\n"
                "A=M\n"
                "D=M\n" 
                
                "A=A-1\n"
                "D=D|M\n"
                "M=D\n"
            )