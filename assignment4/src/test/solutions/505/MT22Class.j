.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_5
	istore_1
Label2:
	iload_1
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	isub
	istore_1
	iload_1
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <clinit>()V
	iconst_5
	putstatic MT22Class/b I
	return
.limit stack 1
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
