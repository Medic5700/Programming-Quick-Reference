010 FOR I = 0 TO 10 :REM THE RANGE IS INCLUSIVE
020   PRINT "LOOP O ITERATION "; I
030 NEXT :REM NEXT IS REQUIRED TO CLOSE OUT THE LOOP
040 PRINT "=================================================================="

100 FOR I = 0 TO 10
110   PRINT "LOOP 1 ITERATION"; I
120 NEXT I
130 PRINT "=================================================================="

200 REM NESTED LOOPS
201 FOR I = 0 TO 10
202   FOR J = 0 TO 10
203     PRINT "LOOP 2 ITERATION"; I; J
204   NEXT J
205 NEXT I
206 PRINT "=================================================================="

210 REM NEXT CAN WORK FOR MULTIPLE LOOPS AT THE SAME TIME
211 FOR I = 0 TO 10
212   FOR J = 0 TO 10
213     PRINT "LOOP 3 ITERATION"; I; J
214 NEXT J,I :REM VARIABLE ORDER MATTERS (NEXT I,J) WILL NOT WORK
215 PRINT "=================================================================="

300 REM INCREMENTING WITH STEP
310 FOR I = 0 TO 100 STEP 10
320   PRINT "LOOP 4 ITERATION"; I
330 NEXT
340 PRINT "=================================================================="

400 REM EXAMPLE OF LOOPING STRUCTURE WITHOUT A FOR LOOP
410 I = 0
420 IF I > 10 THEN GOTO 460
430   PRINT "LOOP 5 ITERATION"; I
440   I = I + 1
450 GOTO 420
460 PRINT "=================================================================="

