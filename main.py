textoutput = []
saida = []
arq = open('input.txt', 'r+')
texto =arq.readlines()

for instrucao in texto:
      op=int(instrucao[0:6],2)
      rs=int(instrucao[6:11],2)
      rt=int(instrucao[11:16],2)
      rd=int(instrucao[16:21],2)
      shamt=int(instrucao[21:26],2)
      funct=int(instrucao[26:32],2)
      imm =int(instrucao[16:32],2)
      mult=int(instrucao[26:32],2)
      code =int(instrucao[6:26],2)
      sh=int(instrucao[16:26],2)
      target=int(instrucao[6:32],2)

if op == 0 and funct == 32:
  funct=("ADD")
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==8 and imm ==0:
  imm="ADDI"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt)) 

elif op==9 and imm ==0:
  imm="ADDIU"
  textoutput.append("{} ${} ${}".format(imm,rs,rt))

elif op==0 and funct ==33:
  funct="ADDU"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==36:
  funct="AND"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==4 and imm ==0:
  imm="BEQ"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==20 and imm ==0:
  imm="BEQl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==1:
  imm="BGEz"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==33:
  imm="bgezal"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==35:
  imm="bgezall"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm==3:
  imm="BGEZl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==7 and imm ==0:
  imm="BGTZ"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==23 and imm ==0:
  imm="BGETZl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==6 and imm ==0:
  imm="BLEZ"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==22 and imm ==0:
  imm="BLEZl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==0:
  imm="BLTz"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==32:
  imm="BLTZAl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==34:
  imm="BLTZALl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==2:
  imm="BLTZl"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==5 and imm ==0:
  imm="BNE"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==21 and imm ==0:
  imm="BNEL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))
  
elif op==0 and funct ==1:
  funct="BREAK"
  textoutput.append("{} ${}".format(funct,code))

elif op==0 and funct ==44:
  funct="DADD"
  textoutput.append("{} ${} ${} ${}".format(funct,rd,rs,rt))

elif op==24 and  imm==0:
  imm="DADDi"
  textoutput.append("{} ${} ${}".format(imm,rs,rt))

elif op==25 and  imm==0:
  imm="DADDIu"
  textoutput.append("{} ${} ${}".format(imm,rs,rt))

elif op==0 and funct ==45:
  funct="DADDu"
  textoutput.append("{} ${} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==30:
  funct="DDIv"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==31:
  funct="DDIVu"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==25:
  funct="DIV"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==27:
  funct="DIVV"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==28:
  funct="MULt"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==29:
  funct="DMULTu"
  textoutput.append("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==56:
  funct="DSLL"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==60:
  funct="DSLL32"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==20:
  funct="DSLLv"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==59:
  funct="DSRA"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==63:
  funct="DSRA32"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==23:
  funct="DSRAv"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==58:
  funct="DSRl"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==62:
  funct="DSRL32"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==22:
  funct="DSRLv"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==46:
  funct="DSUB"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==47:
  funct="DSUBU"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==2 and target ==0:
  target="J"
  textoutput.append("{} ".format(target))

elif op==3 and target ==0:
  target="JAL"
  textoutput.append("{} ".format(target))

elif op==0 and funct ==9:
  funct="JALR"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==32 and imm ==0:
  imm="LB"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==36 and imm ==0:
  imm="LBU"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==53 and imm ==0:
  imm="LD"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==26 and imm ==0:
  imm="LDL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==27 and imm ==0:
  imm="LDR"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==33 and imm ==0:
  imm="LH"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==37 and imm ==0:
  imm="LHU"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==48 and imm ==0:
  imm="LL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==13 and imm ==0:
  imm="LUI"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==35 and imm ==0:
  imm="LW"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==34 and imm ==0:
  imm="LWL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==36 and imm ==0:
  imm="LWR"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==39 and imm ==0:
  imm="LWU"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==34 and imm ==0:
  imm="LWL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==0 and funct ==18:
  funct="MFLO"
  textoutput.append("{} ${}  ".format(funct,rd))

elif op==0 and funct ==11:
  funct="MOVN"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==17:
  funct="MTHI"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==24:
  funct="MULT"
  textoutput.append("{} ${} ${} ${} ".format(funct,rs,rt,sh))

elif op==0 and funct ==25:
  funct="MULTU"
  textoutput.append("{} ${} ${} ${} ".format(funct,rs,rt,sh))

elif op==0 and funct ==39:
  funct="MULT"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==24:
  funct="NOR"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==37:
  funct="OR"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==13 and imm ==0:
  imm="ORI"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==51 and imm ==0:
  imm="PREF"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==40 and imm ==0:
  imm="SB"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==56 and imm ==0:
  imm="SC"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==51 and imm ==0:
  imm="SCD"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==63 and imm ==0:
  imm="SD"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==44 and imm ==0:
  imm="SDL"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==45 and imm ==0:
  imm="SDR"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==41 and imm ==0:
  imm="SH"
  textoutput.append("{} ${} ${} ".format(imm,rs,rt))

elif op==0 and funct ==0:
  funct="SLL"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==4:
  funct="SLLV"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==41:
  funct="SLT"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==10 and imm ==0:
  imm="SLTI"
  textoutput.append("{} ${}  ${} ".format(imm,rs,rt))

elif op==11 and imm ==0:
  imm="SLTIU"
  textoutput.append("{} ${}  ${} ".format(imm,rs,rt))

elif op==0 and funct ==43:
  funct="SLTU"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==3:
  funct="SRA"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==7:
  funct="SRAV"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==2:
  funct="SRL"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==5:
  funct="SRLV"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==34:
  funct="SUB"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==35:
  funct="SUBU"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==43 and imm ==0:
  imm="Sw"
  textoutput.append("{} ${} ${}  ".format(imm,rs,rt))

elif op==44 and imm ==0:
  imm="SWL"
  textoutput.append("{} ${} ${}  ".format(imm,rs,rt))

elif op==46 and imm ==0:
  imm="SWR"
  textoutput.append("{} ${} ${}  ".format(imm,rs,rt))

elif op==0 and funct ==12:
  funct="SYSCALL"
  textoutput.append("{} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==52:
  funct="TEQ"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==1 and rt ==0:
  rt="TEQI"
  textoutput.append("{} ${} ${}  ".format(imm,rs,rt))

elif op==0 and funct ==48:
  funct="TGE"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==1 and imm ==0:
  imm="TEQI"
  textoutput.append("{} ${} ${}  ".format(imm,rs,rt))

elif op==0 and funct ==49:
  funct="TGEU"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==50:
  funct="TLT"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==51:
  funct="TLTu"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==54:
  funct="TNE"
  textoutput.append("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==38:
  funct="XOR"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==14 and imm ==0:
  imm="XORI"
  textoutput.append("{} ${}  ${} ".format(imm,rs,rt))

elif op==17 and funct ==10:
  funct="CEIL.L.FMT"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==34:
  funct="sub"
  textoutput.append("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and imm ==35:
  imm="subu"
  textoutput.append("{} ${} ${} ${} ".format(imm,rs,rt))

print("Converting binary to Assembly ...")
arq_saida = open('saida.txt', 'w')
arq_saida.writelines(textoutput)

print(textoutput)
arq_saida.close()





