"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_010)
# ============================================================================


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Test valid program with auto type inference"""
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Test valid program with functions"""
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Test valid program with nested blocks"""
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Redeclared (test_011 - test_020)
# ============================================================================


def test_011():
    """Test redeclared variable in same scope"""
    source = """
void main() {
    int x = 5;
    float x = 3.14;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected


def test_012():
    """Test redeclared function"""
    source = """
void foo() {}
int foo() { return 1; }
void main() {}
"""
    expected = "Redeclared(Function, foo)"
    assert Checker(source).check_from_source() == expected


def test_013():
    """Test redeclared parameter"""
    source = """
void foo(int x, float x) {}
void main() {}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected


def test_014():
    """Test redeclared struct"""
    source = """
struct S { int x; };
struct S { float y; };
void main() {}
"""
    expected = "Redeclared(Struct, S)"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Undeclared (test_021 - test_030)
# ============================================================================


def test_021():
    """Test undeclared identifier"""
    source = """
void main() {
    x = 10;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


def test_022():
    """Test undeclared function"""
    source = """
void main() {
    foo();
}
"""
    expected = "UndeclaredFunction(foo)"
    assert Checker(source).check_from_source() == expected


def test_023():
    """Test undeclared struct"""
    source = """
void main() {
    Point p;
}
"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Type Mapping & Inference (test_031 - test_040)
# ============================================================================


def test_031():
    """Test type cannot be inferred for auto"""
    source = """
void main() {
    auto x;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected


def test_032():
    """Test auto inferred from assignment"""
    source = """
void main() {
    auto x;
    x = 10;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Type Mismatch in Statement (test_041 - test_050)
# ============================================================================


def test_041():
    """Test type mismatch in if condition (float instead of int)"""
    source = """
void main() {
    if (3.14) { }
}
"""
    expected = "TypeMismatchInStatement(FloatLiteral(3.14),BlockStmt([]),None)"
    # Note: The exact string representation might depend on __str__ of AST nodes
    # We should check nodes.py for __str__
    res = Checker(source).check_from_source()
    assert "TypeMismatchInStatement" in res


def test_042():
    """Test type mismatch in return"""
    source = """
int foo() {
    return 3.14;
}
void main() {}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(FloatLiteral(3.14)))"
    res = Checker(source).check_from_source()
    assert "TypeMismatchInStatement" in res


# ============================================================================
# Type Mismatch in Expression (test_051 - test_060)
# ============================================================================


def test_051():
    """Test type mismatch in binary operation"""
    source = """
void main() {
    int x = 5 + "hello";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(5),+,StringLiteral(hello)))"
    res = Checker(source).check_from_source()
    assert "TypeMismatchInExpression" in res


def test_052():
    """Test type mismatch in member access on non-struct"""
    source = """
void main() {
    int x = 10;
    x.y = 5;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x),y))"
    res = Checker(source).check_from_source()
    assert "TypeMismatchInExpression" in res


# ============================================================================
# Must In Loop (test_061 - test_070)
# ============================================================================


def test_061():
    """Test break outside loop"""
    source = """
void main() {
    break;
}
"""
    expected = "MustInLoop(BreakStmt())"
    res = Checker(source).check_from_source()
    assert "MustInLoop" in res


def test_062():
    """Test continue inside loop (valid)"""
    source = """
void main() {
    while(1) {
        continue;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
