01 IF PEEK($D9) <> 80 THEN SYS $FF5F :REM SWITCH TO 80 CHARACTER MODE
02 REM IF PEEK($D9) <> 40 THEN SYS $FF5F :REM SWITCH TO 40 CHARACTER MODE

10 REM BLANKS THE SCREEN
20 FOR X = 0 TO 80-1 :REM EACH 'LINE' IS ACTUALY 128 CHARACTERS LONG
30   FOR Y = 0 TO 60-1
40     VPOKE 0, Y*256 + X*2, $20   :REM THIS SETS THE CHARACTER TO " "
50     VPOKE 0, Y*256 + X*2 + 1, 0 :REM THIS SETS THE COLOUR (ON THE PALLET)
60 NEXT Y,X

100 REM COLOURS MODE 0 (DEFAULT)
101 VPOKE $F, $2000, $01 :REM SETS COLOUR MODE TO MODE-0 (DEFAULT)
110 FOR Y = 0 TO 15   :REM HIGH 4-BITS ARE BACKGROUND COLOUR
120   FOR X = 0 TO 15 :REM LOW 4-BITS ARE FOREGROUND COLOUR
130     VPOKE 0, Y*256 + X*2, $38
140     VPOKE 0, Y*256 + X*2 + 1, Y*16 + X
150 NEXT X,Y
160 GOSUB 1000
170 PRINT "TEST 1 COMPLETE"

200 REM COLOURS MODE 1
210 VPOKE $F, $2000, $21 :REM SETS COLOUR MODE TO MODE-1
220 FOR Y = 0 TO 15
230   FOR X = 0 TO 15
240     VPOKE 0, Y*256 + X*2, $38
250     VPOKE 0, Y*256 + X*2 + 1, Y*16 + X
260 NEXT X,Y
270 GOSUB 1000
280 PRINT "TEST 2 COMPLETE"

300 REM CHANGING THE PALLET
301 VPOKE $F, $2000, $01 :REM SETS COLOUR MODE TO MODE-0
302 REM PALLET IS STORED AS 256 2-BYTE ENTRIES STARTING AT $F1000
303 REM BYTE 0, HIGH 4-BITS IS GREEN VALUE
304 REM BYTE 0, LOW 4-BITS IS BLUE VALUE
305 REM BYTE 1, LOW 4-BITS IS RED VALUE
310 FOR I = 0 TO 15 :REM THIS SETS THE FIRST 16 ENTRIES AS A GREEN SCALE
320   VPOKE $F, $1000 + I*2, I*16
330   VPOKE $F, $1000 + I*2 + 1, 0
340 NEXT
350 FOR Y = 0 TO 15
360   FOR X = 0 TO 15
370     VPOKE 0, Y*256 + X*2, $38
380     VPOKE 0, Y*256 + X*2 + 1, Y*16 + X
390 NEXT X,Y
400 GOSUB 1000
410 PRINT "TEST 3 COMPLETE"

510 END

1000 REM WAIT FUNCTION, COUNTS TO 2^12
1010 J = 0
1010 I = 0
1020 FOR I = 0 TO 2^12
1030   J = J + 1
1040 NEXT
1050 RETURN
