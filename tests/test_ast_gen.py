from tests.utils import ASTGenerator

def test_ast_gen_001():
    source = "int a;"
    expected = "AST Generation Error: Error on line 1 col 5: ;"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_002():
    source = "float b;"
    expected = "AST Generation Error: Error on line 1 col 7: ;"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_003():
    source = "string c;"
    expected = "AST Generation Error: Error on line 1 col 8: ;"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_004():
    source = "auto d = 1;"
    expected = "AST Generation Error: Error on line 1 col 7: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_005():
    source = "auto d = 1.5;"
    expected = "AST Generation Error: Error on line 1 col 7: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_006():
    source = "auto d = \"hi\";"
    expected = "AST Generation Error: Error on line 1 col 7: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_007():
    source = "int a = 5;"
    expected = "AST Generation Error: Error on line 1 col 6: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_008():
    source = "float b = 3.14;"
    expected = "AST Generation Error: Error on line 1 col 8: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_009():
    source = "string c = \"world\";"
    expected = "AST Generation Error: Error on line 1 col 9: ="
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_010():
    source = "Point p;"
    expected = "AST Generation Error: Error on line 1 col 7: ;"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_011():
    source = "void main() { 1 + 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(1), +, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_012():
    source = "void main() { 1 - 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(1), -, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_013():
    source = "void main() { 1 * 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(1), *, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_014():
    source = "void main() { 1 / 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(1), /, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_015():
    source = "void main() { 1 % 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(1), %, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_016():
    source = "void main() { a + b * c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_017():
    source = "void main() { (a + b) * c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_018():
    source = "void main() { a - b - c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), -, Identifier(b)), -, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_019():
    source = "void main() { a / b / c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), /, Identifier(b)), /, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_020():
    source = "void main() { a * b % c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), %, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_021():
    source = "void main() { -a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(-Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_022():
    source = "void main() { +a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(+Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_023():
    source = "void main() { !a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(!Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_024():
    source = "void main() { ++a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_025():
    source = "void main() { --a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(--Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_026():
    source = "void main() { a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_027():
    source = "void main() { a--; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)--))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_028():
    source = "void main() { !-a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(!PrefixOp(-Identifier(a))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_029():
    source = "void main() { -++a--; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(-PrefixOp(++PostfixOp(Identifier(a)--))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_030():
    source = "void main() { !a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(!PostfixOp(Identifier(a)++)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_031():
    source = "void main() { a < b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), <, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_032():
    source = "void main() { a > b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), >, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_033():
    source = "void main() { a <= b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), <=, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_034():
    source = "void main() { a >= b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), >=, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_035():
    source = "void main() { a == b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), ==, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_036():
    source = "void main() { a != b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), !=, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_037():
    source = "void main() { a < b == c > d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), ==, BinaryOp(Identifier(c), >, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_038():
    source = "void main() { a <= b != c >= d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), <=, Identifier(b)), !=, BinaryOp(Identifier(c), >=, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_039():
    source = "void main() { a == b == c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), ==, Identifier(b)), ==, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_040():
    source = "void main() { a != b != c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), !=, Identifier(b)), !=, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_041():
    source = "void main() { a && b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), &&, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_042():
    source = "void main() { a || b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), ||, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_043():
    source = "void main() { a || b && c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_044():
    source = "void main() { a && b || c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), &&, Identifier(b)), ||, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_045():
    source = "void main() { a || b || c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), ||, Identifier(b)), ||, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_046():
    source = "void main() { a && b && c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), &&, Identifier(b)), &&, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_047():
    source = "void main() { !a && !b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(PrefixOp(!Identifier(a)), &&, PrefixOp(!Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_048():
    source = "void main() { !(a || b); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(!BinaryOp(Identifier(a), ||, Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_049():
    source = "void main() { a < b && c > d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), &&, BinaryOp(Identifier(c), >, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_050():
    source = "void main() { a == b || c != d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(Identifier(a), ==, Identifier(b)), ||, BinaryOp(Identifier(c), !=, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_051():
    source = "void main() { a = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_052():
    source = "void main() { a = b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_053():
    source = "void main() { a.b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_054():
    source = "void main() { a.b.c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_055():
    source = "void main() { a = a + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_056():
    source = "void main() { a = (b = c); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_057():
    source = "void main() { a.b = c.d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = MemberAccess(Identifier(c).d)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_058():
    source = "void main() { a = f(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = FuncCall(f, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_059():
    source = "void main() { a.b = f().c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = MemberAccess(FuncCall(f, []).c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_060():
    source = "void main() { a = b = c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_061():
    source = "void f() {}"
    expected = "Program([FuncDecl(VoidType(), f, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_062():
    source = "int f() { return 1; }"
    expected = "Program([FuncDecl(IntType(), f, [], [ReturnStmt(return IntLiteral(1))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_063():
    source = "float f() { return 1.5; }"
    expected = "Program([FuncDecl(FloatType(), f, [], [ReturnStmt(return FloatLiteral(1.5))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_064():
    source = "string f() { return \"abc\"; }"
    expected = "Program([FuncDecl(StringType(), f, [], [ReturnStmt(return StringLiteral('abc'))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_065():
    source = "auto f() { return 1; }"
    expected = "Program([FuncDecl(auto, f, [], [ReturnStmt(return IntLiteral(1))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_066():
    source = "void main() { f(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_067():
    source = "void main() { f(1); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [IntLiteral(1)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_068():
    source = "void main() { f(1, 2); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [IntLiteral(1), IntLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_069():
    source = "void main() { f(a, b+1); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [Identifier(a), BinaryOp(Identifier(b), +, IntLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_070():
    source = "void main() { f(g(1)); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [FuncCall(g, [IntLiteral(1)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_071():
    source = "struct P {};"
    expected = "Program([StructDecl(P, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_072():
    source = "struct P { int x; };"
    expected = "Program([StructDecl(P, [MemberDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_073():
    source = "struct P { int x; float y; };"
    expected = "Program([StructDecl(P, [MemberDecl(IntType(), x), MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_074():
    source = "struct P { string s; Point p; };"
    expected = "Program([StructDecl(P, [MemberDecl(StringType(), s), MemberDecl(StructType(Point), p)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_075():
    source = "void main() { Point p = Point{1, 2}; }"
    expected = "AST Generation Error: Error on line 1 col 29: {"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_076():
    source = "void main() { p = Point{x, y}; }"
    expected = "AST Generation Error: Error on line 1 col 23: {"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_077():
    source = "void main() { p = Point{}; }"
    expected = "AST Generation Error: Error on line 1 col 23: {"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_078():
    source = "void main() { f(a.b); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [MemberAccess(Identifier(a).b)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_079():
    source = "void main() { f().a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(MemberAccess(FuncCall(f, []).a))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_080():
    source = "void main() { a.b.c.d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_081():
    source = "void main() { if (1) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_082():
    source = "void main() { if (a) a=1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_083():
    source = "void main() { if (a) {a=1;} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then BlockStmt([ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_084():
    source = "void main() { if (a) a=1; else a=2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(a) = IntLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_085():
    source = "void main() { if (a) {a=1;} else {a=2;} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then BlockStmt([ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(a) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_086():
    source = "void main() { if (a) if (b) c=1; else c=2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(c) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_087():
    source = "void main() { while (1) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_088():
    source = "void main() { while (a) a=1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_089():
    source = "void main() { while (a<b) { a=a+1; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while BinaryOp(Identifier(a), <, Identifier(b)) do BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_090():
    source = "void main() { while (1) break; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BreakStmt())])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_091():
    source = "void main() { for (;;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_092():
    source = "void main() { for (int i=0;;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_093():
    source = "void main() { for (;i<10;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_094():
    source = "void main() { for (;;i=i+1) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_095():
    source = "void main() { for (int i=0; i<10; i = i+1) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_096():
    source = "void main() { switch (a) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_097():
    source = "void main() { switch (a) { case 1: break; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_098():
    source = "void main() { switch (a) { default: } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_099():
    source = "void main() { switch (a) { case 1: a=1; case 2: a=2; default: a=3; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))]), CaseStmt(case IntLiteral(2): [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(2)))])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(3)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_100():
    source = "int fib(int n) { if (n<=1) return n; return fib(n-1)+fib(n-2); }"
    expected = "Program([FuncDecl(IntType(), fib, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), <=, IntLiteral(1)) then ReturnStmt(return Identifier(n))), ReturnStmt(return BinaryOp(FuncCall(fib, [BinaryOp(Identifier(n), -, IntLiteral(1))]), +, FuncCall(fib, [BinaryOp(Identifier(n), -, IntLiteral(2))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

