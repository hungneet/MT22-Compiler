.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_2
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_3
	istore_2
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc a is less than b
	invokestatic io/printString(Ljava/lang/String;)V
Label4:
	iload_1
	iload_2
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	ldc a is rather than b
	invokestatic io/printString(Ljava/lang/String;)V
Label7:
	iload_1
	iload_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	ldc a is equal b
	invokestatic io/printString(Ljava/lang/String;)V
Label10:
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
