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
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [Identifier(a), Identifier(b), Identifier(c)]))]))])")
    assert str(ASTGenerator(source).generate()) == expected
