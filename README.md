Substitute string in compile time.

why
we can use a hashed code to standand for a string when we do log or something like this on 
a memory compact system which will save the memory and time.

how
1.use a script to do the replacement before compile.
2.use some tricky macro in code when compile.

benefit
1.smaller string.

If we use a 16bit hash code, it can delegate 65536 strings, which is enough for a small system.
So if the log is logger then 16bit(2 byte), it is worth to do that.

key point
1.ordinary string
2.string with fmt
3.string as %s
