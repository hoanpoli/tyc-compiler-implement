"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_block_comment():
    """9. Line comment"""
    tokenizer = Tokenizer("/* this is block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """10. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_11_plus_minus():
    """11. Mixed: plus and minus"""
    tokenizer = Tokenizer("5+10-15")
    assert tokenizer.get_tokens_as_string() == "5,+,10,-,15,<EOF>"


def test_12_mul_div():
    """12. Mixed: multiplication and division"""
    tokenizer = Tokenizer("6*3/2")
    assert tokenizer.get_tokens_as_string() == "6,*,3,/,2,<EOF>"


def test_13_mod():
    """13. Mixed: mod"""
    tokenizer = Tokenizer("10%3")
    assert tokenizer.get_tokens_as_string() == "10,%,3,<EOF>"


def test_14_inc():
    """14. Mixed: increment"""
    tokenizer = Tokenizer("x++")
    assert tokenizer.get_tokens_as_string() == "x,++,<EOF>"


def test_15_dec():
    """15. Mixed: decrement"""
    tokenizer = Tokenizer("void main() { x = -++a--; }")
    assert tokenizer.get_tokens_as_string() == "void,main,(,),{,x,=,-,++,a,--,;,},<EOF>"


def test_16_equal():
    assert Tokenizer("a==b").get_tokens_as_string() == "a,==,b,<EOF>"


def test_17_not_equal():
    assert Tokenizer("a!=b").get_tokens_as_string() == "a,!=,b,<EOF>"


def test_18_and_or():
    assert Tokenizer("a&&b||c").get_tokens_as_string() == "a,&&,b,||,c,<EOF>"


def test_19_relational():
    assert Tokenizer("a<=b").get_tokens_as_string() == "a,<=,b,<EOF>"


def test_20_assign_chain():
    assert Tokenizer("a=b=c").get_tokens_as_string() == "a,=,b,=,c,<EOF>"


def test_21_parentheses():
    assert Tokenizer("(a)").get_tokens_as_string() == "(,a,),<EOF>"


def test_22_braces():
    assert Tokenizer("{ }").get_tokens_as_string() == "{,},<EOF>"


def test_23_comma():
    assert Tokenizer("a,b,c").get_tokens_as_string() == "a,,,b,,,c,<EOF>"


def test_24_dot():
    assert Tokenizer("p.x").get_tokens_as_string() == "p,.,x,<EOF>"


def test_25_call_empty():
    assert Tokenizer("f()").get_tokens_as_string() == "f,(,),<EOF>"


def test_26_call_args():
    assert Tokenizer("f(1,2)").get_tokens_as_string() == "f,(,1,,,2,),<EOF>"


def test_27_nested_call():
    assert Tokenizer("f(g(x))").get_tokens_as_string() == "f,(,g,(,x,),),<EOF>"


def test_28_block():
    assert Tokenizer("{x;}").get_tokens_as_string() == "{,x,;,},<EOF>"


def test_29_colon():
    assert Tokenizer(":").get_tokens_as_string() == ":,<EOF>"


def test_30_switch_case():
    assert Tokenizer("case 1:").get_tokens_as_string() == "case,1,:,<EOF>"


def test_31_if():
    assert Tokenizer("if").get_tokens_as_string() == "if,<EOF>"


def test_32_else():
    assert Tokenizer("else").get_tokens_as_string() == "else,<EOF>"


def test_33_for():
    assert Tokenizer("for").get_tokens_as_string() == "for,<EOF>"


def test_34_while():
    assert Tokenizer("while").get_tokens_as_string() == "while,<EOF>"


def test_35_switch():
    assert Tokenizer("switch").get_tokens_as_string() == "switch,<EOF>"


def test_36_default():
    assert Tokenizer("default").get_tokens_as_string() == "default,<EOF>"


def test_37_break():
    assert Tokenizer("break").get_tokens_as_string() == "break,<EOF>"


def test_38_continue():
    assert Tokenizer("continue").get_tokens_as_string() == "continue,<EOF>"


def test_39_return():
    assert Tokenizer("return").get_tokens_as_string() == "return,<EOF>"


def test_40_struct():
    assert Tokenizer("struct").get_tokens_as_string() == "struct,<EOF>"


def test_41_void():
    assert Tokenizer("void").get_tokens_as_string() == "void,<EOF>"


def test_42_float_kw():
    assert Tokenizer("float").get_tokens_as_string() == "float,<EOF>"


def test_43_string_kw():
    assert Tokenizer("string").get_tokens_as_string() == "string,<EOF>"


def test_44_auto_decl():
    assert Tokenizer("auto x;").get_tokens_as_string() == "auto,x,;,<EOF>"


def test_45_var_assign():
    assert Tokenizer("x=10;").get_tokens_as_string() == "x,=,10,;,<EOF>"


def test_46_member_assign():
    assert Tokenizer("p.x=1;").get_tokens_as_string() == "p,.,x,=,1,;,<EOF>"


def test_47_postfix_member():
    assert Tokenizer("p.x++;").get_tokens_as_string() == "p,.,x,++,;,<EOF>"


def test_48_prefix_member():
    assert Tokenizer("++p.x;").get_tokens_as_string() == "++,p,.,x,;,<EOF>"


def test_49_function_member():
    assert Tokenizer("print(p.x);").get_tokens_as_string() == "print,(,p,.,x,),;,<EOF>"


def test_50_nested_member():
    assert Tokenizer("a.b.c").get_tokens_as_string() == "a,.,b,.,c,<EOF>"


def test_51_empty_string():
    assert Tokenizer('""').get_tokens_as_string() == ",<EOF>"


def test_52_tab_escape():
    assert Tokenizer('"a\\tb"').get_tokens_as_string() == "a\\tb,<EOF>"


def test_53_newline_escape_illegal():
    assert Tokenizer('"a\nb"').get_tokens_as_string() == "Unclosed String: a"


def test_54_quote_escape():
    assert (
        Tokenizer('"He said: \\"Hi\\""').get_tokens_as_string()
        == 'He said: \\"Hi\\",<EOF>'
    )


def test_55_backslash_escape():
    assert Tokenizer('"C:\\\\path"').get_tokens_as_string() == "C:\\\\path,<EOF>"


def test_56_multiple_escapes():
    assert Tokenizer('"\\t\\n"').get_tokens_as_string() == "\\t\\n,<EOF>"


def test_57_string_with_space():
    assert Tokenizer('"hello world"').get_tokens_as_string() == "hello world,<EOF>"


def test_58_string_punctuation():
    assert Tokenizer('"a,b;c"').get_tokens_as_string() == "a,b;c,<EOF>"


def test_59_string_in_expr():
    assert Tokenizer('print("x");').get_tokens_as_string() == "print,(,x,),;,<EOF>"


def test_60_string_concat_like():
    assert Tokenizer('"a""b"').get_tokens_as_string() == "a,b,<EOF>"


def test_61_string_with_single_quote():
    assert Tokenizer("'a'").get_tokens_as_string() == "Error Token '"


def test_62_unprintable_ascii():
    assert Tokenizer('"\x01"').get_tokens_as_string() == "\x01,<EOF>"

def test_63_id_case_sensitive():
        assert Tokenizer("Var var VAR").get_tokens_as_string() == "Var,var,VAR,<EOF>"


def test_64_int_zero():
    assert Tokenizer("0").get_tokens_as_string() == "0,<EOF>"


def test_65_negative_int():
    assert Tokenizer("-123").get_tokens_as_string() == "-,123,<EOF>"


def test_66_member_access_complex():
    assert Tokenizer("a.b.c().d").get_tokens_as_string() == "a,.,b,.,c,(,),.,d,<EOF>"


def test_67_multiple_lines():
    assert (
        Tokenizer("int x;\nfloat y;").get_tokens_as_string()
        == "int,x,;,float,y,;,<EOF>"
    )


def test_68_tab_ws():
    assert Tokenizer("int\tx;").get_tokens_as_string() == "int,x,;,<EOF>"


def test_69_form_feed():
    assert Tokenizer("int\fx;").get_tokens_as_string() == "int,x,;,<EOF>"


def test_70_mixed_operators():
    assert Tokenizer("x%y==0").get_tokens_as_string() == "x,%,y,==,0,<EOF>"


def test_71_illegal_escape():
    assert (
        Tokenizer('"a\\q"').get_tokens_as_string() == "Illegal Escape In String: a\\q"
    )


def test_72_illegal_escape_mid():
    assert (
        Tokenizer('"abc\\9xyz"').get_tokens_as_string()
        == "Illegal Escape In String: abc\\9"
    )


def test_73_unclosed_string_eof():
    assert Tokenizer('"abc').get_tokens_as_string() == "Unclosed String: abc"


def test_74_unclosed_string_newline():
    assert Tokenizer('"a\nb"').get_tokens_as_string() == "Unclosed String: a"


def test_75_unclosed_string_cr():
    assert Tokenizer('"a\rb"').get_tokens_as_string() == "Unclosed String: a"


def test_76_only_quote():
    assert Tokenizer('"').get_tokens_as_string() == "Unclosed String: "


def test_77_escape_before_eof():
    assert Tokenizer('"a\\').get_tokens_as_string() == "Unclosed String: a"


def test_78_illegal_escape_backslash():
    assert Tokenizer('"\\x"').get_tokens_as_string() == "Illegal Escape In String: \\x"


def test_79_illegal_escape_hex():
    assert (
        Tokenizer('"\\x01"').get_tokens_as_string() == "Illegal Escape In String: \\x"
    )


def test_80_comment_then_error():
    assert (
        Tokenizer('//cmt\n"a\\q"').get_tokens_as_string()
        == "Illegal Escape In String: a\\q"
    )


def test_81_error_char_hash():
    assert Tokenizer("#").get_tokens_as_string() == "Error Token #"


def test_82_error_char_at():
    assert Tokenizer("@").get_tokens_as_string() == "Error Token @"


def test_83_float_no_integer():
    assert Tokenizer(".5").get_tokens_as_string() == ".5,<EOF>"


def test_84_float_no_decimal():
    assert Tokenizer("1.").get_tokens_as_string() == "1.,<EOF>"


def test_85_float_exponent():
    assert Tokenizer("1e10").get_tokens_as_string() == "1e10,<EOF>"


def test_86_expression_precedence():
    assert Tokenizer("a||b&&c").get_tokens_as_string() == "a,||,b,&&,c,<EOF>"


def test_87_full_decl():
    assert (
        Tokenizer("int x=1+2*3;").get_tokens_as_string() == "int,x,=,1,+,2,*,3,;,<EOF>"
    )


def test_88_for_like():
    assert (
        Tokenizer("for(i=0;i<10;i++)").get_tokens_as_string()
        == "for,(,i,=,0,;,i,<,10,;,i,++,),<EOF>"
    )


def test_89_switch_like():
    assert Tokenizer("switch(x)").get_tokens_as_string() == "switch,(,x,),<EOF>"


def test_90_case_stmt():
    assert Tokenizer("case 10:").get_tokens_as_string() == "case,10,:,<EOF>"


def test_91_default_stmt():
    assert Tokenizer("default:").get_tokens_as_string() == "default,:,<EOF>"


def test_92_break_stmt():
    assert Tokenizer("break;").get_tokens_as_string() == "break,;,<EOF>"


def test_93_continue_stmt():
    assert Tokenizer("continue;").get_tokens_as_string() == "continue,;,<EOF>"


def test_94_return_stmt():
    assert Tokenizer("return x;").get_tokens_as_string() == "return,x,;,<EOF>"


def test_95_nested_blocks():
    assert Tokenizer("{{x;}}").get_tokens_as_string() == "{,{,x,;,},},<EOF>"


def test_96_chained_assign():
    assert Tokenizer("a=b=c=1").get_tokens_as_string() == "a,=,b,=,c,=,1,<EOF>"


def test_97_function_call_chain():
    assert Tokenizer("f(a,b(c))").get_tokens_as_string() == "f,(,a,,,b,(,c,),),<EOF>"


def test_98_postfix_chain():
    assert Tokenizer("x++++").get_tokens_as_string() == "x,++,++,<EOF>"


def test_99_complex_member_call():
    assert Tokenizer("a.b().c").get_tokens_as_string() == "a,.,b,(,),.,c,<EOF>"


def test_100_mixed_all():
    assert (
        Tokenizer('auto x=print("hi\\n");').get_tokens_as_string()
        == "auto,x,=,print,(,hi\\n,),;,<EOF>"
    )
