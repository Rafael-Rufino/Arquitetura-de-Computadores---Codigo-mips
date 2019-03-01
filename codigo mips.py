
instrucao=input("digite os 32 bits: ")
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


#00100010000100001000010000000000
#00000010000100001000010000100000
#################################################################################
#print("${} ${} ${} ${} ${} {}".format(op,rs,rt,rd,shamt,funct))
#print("${}".format(op))
#print("${}".format(rs))
#print("${}".format(rt))
#print("${}".format(rd))
#print("${}".format(shamt))
#print("{}".format(funct))
#################################################################################

if op == 0 and funct == 32:
  funct=("ADD")
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==8 and imm ==0:
  imm="ADDI"
  print("{} ${} ${} ".format(imm,rs,rt))
  #00010000000100001000010000000000

elif op==9 and imm ==0:
  imm="ADDIU"
  print("{} ${} ${}".format(imm,rs,rt))

elif op==0 and funct ==33:
  funct="ADDU"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==36:
  funct="AND"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))



elif op==4 and imm ==0:
  imm="BEQ"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==20 and imm ==0:
  imm="BEQl"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==1:
  imm="BGEz"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==1 and imm ==33:
  imm="bgezal"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==35:
  imm="bgezall"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm==3:
  imm="BGEZl"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==7 and imm ==0:
  imm="BGTZ"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==23 and imm ==0:
  imm="BGETZl"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==6 and imm ==0:
  imm="BLEZ"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==22 and imm ==0:
  imm="BLEZl"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==0:
  imm="BLTz"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==1 and imm ==32:
  imm="BLTZAl"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==1 and imm ==34:
  imm="BLTZALl"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==1 and imm ==2:
  imm="BLTZl"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==5 and imm ==0:
  imm="BNE"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==21 and imm ==0:
  imm="BNEL"
  print("{} ${} ${} ".format(imm,rs,rt))
  
elif op==0 and funct ==1:
  funct="BREAK"
  print("{} ${}".format(funct,code))

elif op==0 and funct ==44:
  funct="DADD"
  print("{} ${} ${} ${}".format(funct,rd,rs,rt))

elif op==24 and  imm==0:
  imm="DADDi"
  print("{} ${} ${}".format(imm,rs,rt))

elif op==25 and  imm==0:
  imm="DADDIu"
  print("{} ${} ${}".format(imm,rs,rt))

elif op==0 and funct ==45:
  funct="DADDu"
  print("{} ${} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==30:
  funct="DDIv"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==31:
  funct="DDIVu"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==25:
  funct="DIV"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==27:
  funct="DIVV"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==28:
  funct="MULt"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0  and funct ==29:
  funct="DMULTu"
  print("{} ${} ${}".format(funct,rd,rs,rt))

elif op==0 and funct ==56:
  funct="DSLL"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==60:
  funct="DSLL32"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==20:
  funct="DSLLv"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==59:
  funct="DSRA"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==63:
  funct="DSRA32"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==23:
  funct="DSRAv"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==58:
  funct="DSRl"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==62:
  funct="DSRL32"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==22:
  funct="DSRLv"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==46:
  funct="DSUB"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==47:
  funct="DSUBU"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))



elif op==2 and target ==0:
  target="J"
  print("{} ".format(target))



elif op==3 and target ==0:
  target="JAL"
  print("{} ".format(target))

elif op==0 and funct ==9:
  funct="JALR"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==32 and imm ==0:
  imm="LB"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==36 and imm ==0:
  imm="LBU"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==53 and imm ==0:
  imm="LD"
  print("{} ${} ${} ".format(imm,rs,rt))



elif op==26 and imm ==0:
  imm="LDL"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==27 and imm ==0:
  imm="LDR"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==33 and imm ==0:
  imm="LH"
  print("{} ${} ${} ".format(imm,rs,rt))



elif op==37 and imm ==0:
  imm="LHU"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==48 and imm ==0:
  imm="LL"
  print("{} ${} ${} ".format(imm,rs,rt))



elif op==13 and imm ==0:
  imm="LUI"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==35 and imm ==0:
  imm="LW"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==34 and imm ==0:
  imm="LWL"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==36 and imm ==0:
  imm="LWR"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==39 and imm ==0:
  imm="LWU"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==34 and imm ==0:
  imm="LWL"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==0 and funct ==18:
  funct="MFLO"
  print("{} ${}  ".format(funct,rd))



elif op==0 and funct ==11:
  funct="MOVN"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==17:
  funct="MTHI"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==24:
  funct="MULT"
  print("{} ${} ${} ${} ".format(funct,rs,rt,sh))


elif op==0 and funct ==25:
  funct="MULTU"
  print("{} ${} ${} ${} ".format(funct,rs,rt,sh))


elif op==0 and funct ==39:
  funct="MULT"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==24:
  funct="NOR"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))



elif op==0 and funct ==37:
  funct="OR"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))



elif op==13 and imm ==0:
  imm="ORI"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==51 and imm ==0:
  imm="PREF"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==40 and imm ==0:
  imm="SB"
  print("{} ${} ${} ".format(imm,rs,rt))



elif op==56 and imm ==0:
  imm="SC"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==51 and imm ==0:
  imm="SCD"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==63 and imm ==0:
  imm="SD"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==44 and imm ==0:
  imm="SDL"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==45 and imm ==0:
  imm="SDR"
  print("{} ${} ${} ".format(imm,rs,rt))


elif op==41 and imm ==0:
  imm="SH"
  print("{} ${} ${} ".format(imm,rs,rt))

elif op==0 and funct ==0:
  funct="SLL"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==4:
  funct="SLLV"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==41:
  funct="SLT"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==10 and imm ==0:
  imm="SLTI"
  print("{} ${}  ${} ".format(imm,rs,rt))

elif op==11 and imm ==0:
  imm="SLTIU"
  print("{} ${}  ${} ".format(imm,rs,rt))



elif op==0 and funct ==43:
  funct="SLTU"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==3:
  funct="SRA"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==7:
  funct="SRAV"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==2:
  funct="SRL"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==5:
  funct="SRLV"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))


elif op==0 and funct ==34:
  funct="SUB"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==35:
  funct="SUBU"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==43 and imm ==0:
  imm="Sw"
  print("{} ${} ${}  ".format(imm,rs,rt))


elif op==44 and imm ==0:
  imm="SWL"
  print("{} ${} ${}  ".format(imm,rs,rt))

elif op==46 and imm ==0:
  imm="SWR"
  print("{} ${} ${}  ".format(imm,rs,rt))


elif op==0 and funct ==12:
  funct="SYSCALL"
  print("{} ${} ".format(funct,rd,rs,rt))

elif op==0 and funct ==52:
  funct="TEQ"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))


elif op==1 and rt ==0:
  rt="TEQI"
  print("{} ${} ${}  ".format(imm,rs,rt))

elif op==0 and funct ==48:
  funct="TGE"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==1 and imm ==0:
  imm="TEQI"
  print("{} ${} ${}  ".format(imm,rs,rt))


elif op==0 and funct ==49:
  funct="TGEU"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==50:
  funct="TLT"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))


elif op==0 and funct ==51:
  funct="TLTu"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))


elif op==0 and funct ==54:
  funct="TNE"
  print("{} ${} ${} ${} ".format(funct,code,rs,rt))

elif op==0 and funct ==38:
  funct="XOR"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==14 and imm ==0:
  imm="XORI"
  print("{} ${}  ${} ".format(imm,rs,rt))

elif op==17 and funct ==10:
  funct="CEIL.L.FMT"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

#parei aqui pagina 245

elif op==0 and funct ==34:
  funct="sub"
  print("{} ${} ${} ${} ".format(funct,rd,rs,rt))

elif op==0 and imm ==35:
  imm="subu"
  print("{} ${} ${} ${} ".format(imm,rs,rt))





 
#0 0 0 0 0 0 0 0 0 0  0   0   0  0  0 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0    
#1 2 3 4 5 6 7 8 9 10 11, 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32




# opção teste pra primeira instrução add.
#00000010000100001000010000011000
#00000010000100001000010000100000
#b=len(a)
#print((b))
