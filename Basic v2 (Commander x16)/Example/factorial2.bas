10 FOR X = 0 TO 10
20   Y = 0
30   GOSUB 1000
40   PRINT X; "!    ="; Y
50 NEXT
60 END

1000 REM FACTORIAL, INPUT (X), OUTPUT (Y)
1010 A = 1
1020 FOR I = 1 TO X
1030   A = A * I
1040 NEXT
1050 Y = A
1060 RETURN
