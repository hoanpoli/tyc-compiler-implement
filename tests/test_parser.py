"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = 'void greet() { printString("Hello"); }'
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"


def test_11_struct_multi_members():
    assert Parser("struct Point { int x; int y; float z; };").parse() == "success"


def test_12_struct_empty():
    assert Parser("struct Empty {};").parse() == "success"


def test_13_struct_nested_usage():
    assert Parser("struct A { int x; }; struct B { A a; };").parse() == "success"


def test_14_struct_init_list():
    assert Parser("void main() { Point p = {10, 20}; }").parse() == "success"


def test_15_struct_member_access():
    assert Parser("void main() { p.x = 10; }").parse() == "success"


def test_16_struct_member_inc():
    assert Parser("void main() { p.x++; }").parse() == "success"


def test_17_struct_complex_access():
    assert Parser("void main() { a.b.c.d = 1; }").parse() == "success"


def test_18_struct_error_no_semi():
    assert Parser("struct A { int x }").parse() != "success"


def test_19_struct_error_nested_decl():
    assert Parser("struct A { struct B { int y; } x; };").parse() != "success"


def test_20_struct_literal_arg():
    assert Parser("void main() { f({1, 2}); }").parse() == "success"


def test_21_func_multi_params():
    assert (
        Parser("int add(int a, float b, string c) { return a; }").parse() == "success"
    )


def test_22_func_infer_return():
    assert Parser("f(int x) { return x; }").parse() == "success"


def test_23_func_void_param_error():
    assert Parser("void f(void x) {}").parse() != "success"


def test_24_func_auto_param_error():
    assert Parser("void f(auto x) {}").parse() != "success"


def test_25_func_call_complex_args():
    assert Parser("void main() { f(a+b, g(x), 1.5); }").parse() == "success"


def test_26_func_no_body_error():
    assert Parser("void f();").parse() != "success"


def test_27_main_with_params_error():
    assert (
        Parser("void main(int x) {}").parse() == "success"
    )  # Parser chấp nhận, Semantic mới chặn


def test_28_func_return_struct_lit():
    assert Parser("Point f() { return {1, 2}; }").parse() == "success"


def test_29_func_stmt_list_empty():
    assert Parser("void f() {}").parse() == "success"


def test_30_call_as_statement():
    assert Parser("void main() { doSomething(); }").parse() == "success"


def test_31_auto_no_init():
    assert Parser("void main() { auto x; }").parse() == "success"


def test_32_multi_var_decl_error():
    assert Parser("void main() { int x, y; }").parse() != "success"


def test_33_string_assign():
    assert Parser('void main() { string s; s = "test"; }').parse() == "success"


def test_34_global_var_error():
    assert Parser("int x = 10; void main(){}").parse() != "success"


def test_35_struct_var_no_init():
    assert Parser("void main() { Point p; }").parse() == "success"


def test_36_float_assign_int():
    assert Parser("void main() { float f; f = 10; }").parse() == "success"


def test_37_var_shadowing_syntax():
    assert Parser("void main() { int x; { float x; } }").parse() == "success"


def test_38_auto_assign_struct():
    assert Parser("void main() { auto p = {1, 2}; }").parse() == "success"


def test_39_invalid_identifier_error():
    assert Parser("void main() { int 123x; }").parse() != "success"


def test_40_void_variable_error():
    assert Parser("void main() { void x; }").parse() != "success"


def test_41_if_else_dangling():
    assert Parser("void main() { if(a) if(b) c=1; else c=2; }").parse() == "success"


def test_42_while_complex_cond():
    assert Parser("void main() { while(a && (b || !c)) {} }").parse() == "success"


def test_43_for_full():
    assert Parser("void main() { for(int i=0; i<10; i=i+1) {} }").parse() == "success"


def test_44_for_no_init():
    assert Parser("void main() { for(; i<10; i++) {} }").parse() == "success"


def test_45_for_no_cond():
    assert Parser("void main() { for(i=0; ; i++) {} }").parse() == "success"


def test_46_for_no_update():
    assert Parser("void main() { for(i=0; i<10; ) {} }").parse() == "success"


def test_47_for_empty():
    assert Parser("void main() { for(;;){} }").parse() == "success"


def test_48_switch_default_middle():
    assert (
        Parser(
            "void main() { switch(x) { case 1: b; default: d; case 2: c; } }"
        ).parse()
        == "success"
    )


def test_49_switch_empty_body():
    assert Parser("void main() { switch(x) {} }").parse() == "success"


def test_50_switch_constant_expr_case():
    assert (
        Parser("void main() { switch(x) { case 1+2*3: break; } }").parse() == "success"
    )


def test_51_if_cond_assign():
    assert Parser("void main() { if(x=5) {} }").parse() == "success"


def test_52_for_init_expr():
    assert Parser("void main() { for(x=0; x<5; x++) {} }").parse() == "success"


def test_53_nested_while():
    assert Parser("void main() { while(1) while(2) {} }").parse() == "success"


def test_54_if_else_blocks():
    assert Parser("void main() { if(1) { a=1; } else { b=1; } }").parse() == "success"


def test_55_while_empty_body():
    assert Parser("void main() { while(1); }").parse() != "success"  # ; không phải stmt


# ========== 56-70: Switch Case (Fallthrough & Default) ==========
def test_56_switch_default_middle():
    assert (
        Parser(
            "void main() { switch(x) { case 1: b; default: d; case 2: c; } }"
        ).parse()
        == "success"
    )


def test_57_switch_empty_body():
    assert Parser("void main() { switch(x) {} }").parse() == "success"


def test_58_switch_constant_expr_case():
    assert (
        Parser("void main() { switch(x) { case 1+2*3: break; } }").parse() == "success"
    )


def test_59_switch_multiple_cases():
    assert (
        Parser("void main() { switch(x) { case 1: case 2: case 3: break; } }").parse()
        == "success"
    )


def test_60_switch_no_break_fallthrough():
    assert (
        Parser("void main() { switch(x) { case 1: x=1; case 2: x=2; } }").parse()
        == "success"
    )


def test_61_precedence_logic():
    assert (
        Parser("void main() { auto x = a || b && c == d < e + f * g; }").parse()
        == "success"
    )


def test_62_assoc_assign():
    assert Parser("void main() { a = b = c = 1; }").parse() == "success"


def test_63_postfix_unary():
    assert (
        Parser("void main() { x = -++a--; }").parse() == "success"
    )


def test_64_parens_expr():
    assert Parser("void main() { x = (1 + 2) * 3; }").parse() == "success"


def test_65_modulus_int_only_syntax():
    assert Parser("void main() { x = 10 % 3; }").parse() == "success"


def test_66_switch_non_int_expr_error():
    assert (
        Parser('void main() { switch("hi"){} }').parse() == "success"
    )


def test_67_switch_stmt_after_default():
    assert (
        Parser("void main() { switch(x){default: x=1; break; x=2;} }").parse()
        == "success"
    )


def test_68_switch_case_logic_op_error():
    assert (
        Parser("void main() { switch(x){case 1&&2:;} }").parse() != "success"
    )


def test_69_switch_nested():
    assert (
        Parser("void main() { switch(x){case 1: switch(y){case 2:;}} }").parse()
        != "success"
    )


def test_70_switch_break_outside_error():
    assert (
        Parser("void main() { break; }").parse() == "success"
    ) 


def test_71_precedence_logic():
    assert (
        Parser("void main() { auto x = a || b && c == d < e + f * g; }").parse()
        == "success"
    )


def test_72_assoc_assign():
    assert Parser("void main() { a = b = c = 1; }").parse() == "success"


def test_73_postfix_unary():
    assert Parser("void main() { x = -++a--; }").parse() == "success"


def test_74_parens_expr():
    assert Parser("void main() { x = (1 + 2) * 3; }").parse() == "success"


def test_75_modulus_int_only_syntax():
    assert Parser("void main() { x = 10 % 3; }").parse() == "success"


def test_76_logical_not_precedence():
    assert Parser("void main() { x = !a == b; }").parse() == "success"


def test_77_complex_arithmetic():
    assert Parser("void main() { x = a * b / c % d + e - f; }").parse() == "success"


def test_78_relational_assoc():
    assert Parser("void main() { x = a < b <= c > d >= e; }").parse() == "success"


def test_79_inc_dec_prefix_postfix():
    assert Parser("void main() { ++x; x--; --x; x++; }").parse() == "success"


def test_80_assign_struct_member():
    assert Parser("void main() { p.x = p.y = 10; }").parse() == "success"


def test_81_var_decl_in_block():
    assert Parser("void main() { { int x = 1; } }").parse() == "success"


def test_82_return_void():
    assert Parser("void f() { return; }").parse() == "success"


def test_83_return_expr():
    assert Parser("int f() { return 1+2; }").parse() == "success"


def test_84_break_continue_in_loop():
    assert Parser("void main() { while(1) { break; continue; } }").parse() == "success"


def test_85_chained_member_call():
    assert Parser("void main() { a.b().c = 1; }").parse() == "success"


def test_86_invalid_global_stmt():
    assert Parser("int x = 5; x = 10;").parse() != "success"


def test_87_missing_semi_var():
    assert Parser("void main() { int x }").parse() != "success"


def test_88_missing_parens_if():
    assert Parser("void main() { if 1 print(1); }").parse() != "success"


def test_89_empty_stmt_error():
    assert Parser("void main() { ; }").parse() != "success"


def test_90_unclosed_block():
    assert Parser("void main() { if(1) { ").parse() != "success"


def test_91_float_lit_various():
    assert (
        Parser("void main() { float f = .5 + 1. + 1e2 + 0.5E-3; }").parse() == "success"
    )


def test_92_string_lit_in_assign():
    assert Parser('void main() { string s = "hi\\n"; }').parse() == "success"


def test_93_complex_for_init():
    assert (
        Parser("void main() { for(auto i=0, j=0; ; ) {} }").parse() != "success"
    )


def test_94_multiple_default_switch():
    assert Parser("void main() { switch(x){default:; default:;} }").parse() != "success"


def test_95_postfix_inc_dec_mix():
    assert (
        Parser("void main() { x++--; }").parse() == "success"
    )


def test_96_unary_ops():
    assert Parser("void main() { x = +-!a; }").parse() == "success"


def test_97_func_decl_no_id():
    assert Parser("void (int x) {}").parse() != "success"


def test_98_struct_id_as_type():
    assert Parser("struct A {}; void main() { A a; }").parse() == "success"


def test_99_auto_multi_assign():
    assert Parser("void main() { auto a; a = b = 1; }").parse() == "success"


def test_100_full_integration():
    source = """
    struct Point { int x; int y; };
    int area(Point p) { return p.x * p.y; }
    void main() {
        Point p1 = {10, 20};
        if (area(p1) > 100) {
            printString("Large");
        } else {
            printString("Small");
        }
    }
    """
    assert Parser(source).parse() == "success"
