010 REM THERE ARE TWO VERY DIFFERENT WAYS TO DO FUNCTIONS

020 REM A SUBROUTINE IS VERY SIMPLE AND LIMITED, IT LITTERALLY JUMPS TO A
021 REM LINE AND THEN BACK, BUT THERE IS NO BUILT IN WAY TO TRANSFER
022 REM VARIABLES AND RESULTS BACK AND FORTH, WHICH MUST BE DONE BY THE
023 REM PROGRAMMER. ALL VARIABLES ARE AVAILABLE AT ANY TIME ANYWHERE IN THE
024 REM PROGRAM, WHICH IS A WAY TO MORE DATA TO A SUBROUTINE
025 FOR I = 0 TO 10
026   X = I
027   Y = 0
028   GOSUB 1000
029   PRINT I; " = "; Y
030 NEXT
040 PRINT "=================================================================="

1000 REM A SUBROUTINE, IT TAKES IN THE VARIABLE X, OUTPUT IS THE VARIABLE Y
1001 REM CAN ALSO BE ANY INSTRUCTIONS
1002 REM NOTE: LINE NUMBERING IS OUT OF ORDER FOR EASE OF READING
1010 Y = X^2 - 1
1020 RETURN
1030 REM RETURN ENDS THE SUBROUTINE AND RETURNS TO WHERE IT WAS CALLED FROM
1040 REM NOTE: YOU WILL NEED TO USE THE 'END' COMMAND SOMEWHERE BEFORE THIS
1050 REM AS BASIC WILL JUST KEEP GOING THROUGH THE LINE NUMBERS UNTIL IT GETS
1060 REM TO THE RETURN, WHICH WILL CAUSE AN ERROR SINCE NOTHING CALLED IT

100 REM AN ACTUAL FUNCTION IS VERY LIMITED, LITTERALLY A SINGLE MATH EXPRESSION
110 DEF FN FUNC1(X) = X^2 - 1
111 REM NOTE: CAN'T NAME A FUNCTION 'FUNCTION'
120 FOR I = 0 TO 10
130   X = FN FUNC1(I) :REM CALLING THE FUNCTION
140   PRINT I; " = "; X
150 NEXT
160 PRINT "=================================================================="
170 END
