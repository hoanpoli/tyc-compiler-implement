"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


def test1_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """void main() {
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test2_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """"""
    expected = "Program([])"
    assert str(ASTGenerator(source).generate()) == expected

def test3_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """void main() {
    foo(a, b, c);
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(Identifier(foo), [Identifier(a), Identifier(b), Identifier(c)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test4_if_no_else():
    source = """
void main() {
    if (a) {
        b = 1;
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then BlockStmt([ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test5_if_else():
    source = """
void main() {
    if (a) 
        b = 1;
    else 
        b = 2;
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(b) = IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test6_while_basic():
    source = """
void main() {
    while (i < 10) {
        i = i + 1;
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test7_for_full():
    source = """
void main() {
    for (int i = 0; i < 10; i = i + 1) {
        printInt(i);
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(Identifier(printInt), [Identifier(i)]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test8_for_no_init():
    source = """
void main() {
    for (; i < 10; i++) {
        i = i + 2;
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(2))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test9_break_in_while():
    source = """
void main() {
    while (1) {
        break;
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test10_continue_in_for():
    source = """
void main() {
    for (int i = 0; i < 10; i++) {
        continue;
    }
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ContinueStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test11_return_with_value():
    source = """
int foo() {
    return 5;
}"""
    expected = "Program([FuncDecl(IntType(), foo, [], BlockStmt([ReturnStmt(return IntLiteral(5))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test12_return_void():
    source = """
void main() {
    return;
}"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test13_nested_if():
    source = """
void main() {
    if (a)
        if (b)
            c = 1;
        else
            c = 2;
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(c) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test14_struct():
    source = """
struct Point {
    int x;
    int y;
};"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test16_function_no_return_type():
    source = """
add(int x, int y) {
    return x + y;
}"""
    expected = "Program([FuncDecl(auto, add, [Param(IntType(), x), Param(IntType(), y)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test17_function_void_type():
    source = """
void main() {
    auto x = 10;
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x = IntLiteral(10))]))])"
    assert str(ASTGenerator(source).generate()) == expected
