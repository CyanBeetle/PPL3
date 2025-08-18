.source HLang.java
.class public HLang
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_3
	istore_2
.var 3 is c I from Label0 to Label1
	bipush 10
	istore_3
.var 4 is d I from Label0 to Label1
	iconst_2
	istore 4
.var 5 is result I from Label0 to Label1
	iload_1
	iload_2
	iadd
	iload_3
	iload 4
	isub
	imul
	istore 5
	iload 5
	invokestatic io/int2str(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
.limit stack 3
.limit locals 6
.end method

.method public <init>()V
.var 0 is this LHLang; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
