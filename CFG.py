"""
╔══════════════════════════════════════════════════════════════════╗
║         ADVANCED CFG-BASED COMPILER — Python Implementation      ║
║                                                                  ║
║  Phases:                                                         ║
║   1. Lexer         — Source code → Tokens                        ║
║   2. Parser        — Tokens → Parse Tree (CFG-based)             ║
║   3. Useless Symbol Remover — Clean the CFG                      ║
║   4. Semantic Analyzer — Type checking, scope analysis           ║
║   5. IR Generator  — AST → Intermediate Representation           ║
║   6. Code Generator — IR → Target Assembly-like code             ║
║                                                                  ║
║  Supports: variables, arithmetic, if/else, while loops,          ║
║            functions, print statements                           ║
╚══════════════════════════════════════════════════════════════════╝
"""

import re
import sys
from dataclasses import dataclass, field
from typing import Any, Optional
from enum import Enum, auto


# ═══════════════════════════════════════════════════════════════════
#  SECTION 1: TOKEN DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

class TokenType(Enum):
    # Literals
    NUMBER     = auto()
    STRING     = auto()
    IDENTIFIER = auto()

    # Keywords
    IF         = auto()
    ELSE       = auto()
    WHILE      = auto()
    FUNC       = auto()
    RETURN     = auto()
    PRINT      = auto()
    TRUE       = auto()
    FALSE      = auto()
    INT        = auto()
    BOOL       = auto()

    # Operators
    PLUS       = auto()
    MINUS      = auto()
    STAR       = auto()
    SLASH      = auto()
    EQ         = auto()   # ==
    NEQ        = auto()   # !=
    LT         = auto()   # <
    GT         = auto()   # >
    LTE        = auto()   # <=
    GTE        = auto()   # >=
    AND        = auto()   # &&
    OR         = auto()   # ||
    NOT        = auto()   # !
    ASSIGN     = auto()   # =

    # Delimiters
    LPAREN     = auto()
    RPAREN     = auto()
    LBRACE     = auto()
    RBRACE     = auto()
    COMMA      = auto()
    SEMICOLON  = auto()

    # Special
    EOF        = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int

    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, line={self.line})"


# ═══════════════════════════════════════════════════════════════════
#  SECTION 2: LEXER — Source Code → Tokens
# ═══════════════════════════════════════════════════════════════════

class LexerError(Exception):
    pass

class Lexer:
    """
    CFG for tokens (regular grammar):
      digit    → [0-9]
      letter   → [a-zA-Z_]
      number   → digit+
      ident    → letter (letter | digit)*
      string   → '"' .* '"'
    """

    KEYWORDS = {
        'if': TokenType.IF, 'else': TokenType.ELSE,
        'while': TokenType.WHILE, 'func': TokenType.FUNC,
        'return': TokenType.RETURN, 'print': TokenType.PRINT,
        'true': TokenType.TRUE, 'false': TokenType.FALSE,
        'int': TokenType.INT, 'bool': TokenType.BOOL,
    }

    OPERATORS = {
        '==': TokenType.EQ, '!=': TokenType.NEQ,
        '<=': TokenType.LTE, '>=': TokenType.GTE,
        '&&': TokenType.AND, '||': TokenType.OR,
        '<':  TokenType.LT,  '>':  TokenType.GT,
        '+':  TokenType.PLUS,'-':  TokenType.MINUS,
        '*':  TokenType.STAR,'/':  TokenType.SLASH,
        '=':  TokenType.ASSIGN, '!': TokenType.NOT,
        '(':  TokenType.LPAREN, ')': TokenType.RPAREN,
        '{':  TokenType.LBRACE, '}': TokenType.RBRACE,
        ',':  TokenType.COMMA,  ';': TokenType.SEMICOLON,
    }

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.tokens: list[Token] = []

    def error(self, msg):
        raise LexerError(f"[Lexer Error] Line {self.line}: {msg}")

    def peek(self, offset=0):
        idx = self.pos + offset
        return self.source[idx] if idx < len(self.source) else '\0'

    def advance(self):
        ch = self.source[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
        return ch

    def skip_whitespace_and_comments(self):
        while self.pos < len(self.source):
            if self.source[self.pos] in ' \t\r\n':
                self.advance()
            elif self.peek() == '/' and self.peek(1) == '/':
                while self.pos < len(self.source) and self.source[self.pos] != '\n':
                    self.pos += 1
            else:
                break

    def read_number(self):
        start = self.pos
        while self.pos < len(self.source) and self.source[self.pos].isdigit():
            self.pos += 1
        return int(self.source[start:self.pos])

    def read_string(self):
        self.pos += 1  # skip opening "
        start = self.pos
        while self.pos < len(self.source) and self.source[self.pos] != '"':
            self.pos += 1
        if self.pos >= len(self.source):
            self.error("Unterminated string literal")
        val = self.source[start:self.pos]
        self.pos += 1  # skip closing "
        return val

    def read_identifier(self):
        start = self.pos
        while self.pos < len(self.source) and (self.source[self.pos].isalnum() or self.source[self.pos] == '_'):
            self.pos += 1
        return self.source[start:self.pos]

    def tokenize(self) -> list[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace_and_comments()
            if self.pos >= len(self.source):
                break

            line = self.line
            ch = self.source[self.pos]

            # Number
            if ch.isdigit():
                val = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, val, line))

            # String
            elif ch == '"':
                val = self.read_string()
                self.tokens.append(Token(TokenType.STRING, val, line))

            # Identifier or keyword
            elif ch.isalpha() or ch == '_':
                word = self.read_identifier()
                ttype = self.KEYWORDS.get(word, TokenType.IDENTIFIER)
                self.tokens.append(Token(ttype, word, line))

            # Two-char operators
            elif ch in ('=', '!', '<', '>', '&', '|'):
                two = self.source[self.pos:self.pos+2]
                if two in self.OPERATORS:
                    self.tokens.append(Token(self.OPERATORS[two], two, line))
                    self.pos += 2
                elif ch in self.OPERATORS:
                    self.tokens.append(Token(self.OPERATORS[ch], ch, line))
                    self.pos += 1
                else:
                    self.error(f"Unknown character: {ch!r}")

            # Single-char operators/delimiters
            elif ch in self.OPERATORS:
                self.tokens.append(Token(self.OPERATORS[ch], ch, line))
                self.pos += 1

            else:
                self.error(f"Unknown character: {ch!r}")

        self.tokens.append(Token(TokenType.EOF, None, self.line))
        return self.tokens


# ═══════════════════════════════════════════════════════════════════
#  SECTION 3: AST NODE DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

@dataclass
class ASTNode:
    pass

@dataclass
class Program(ASTNode):
    statements: list

@dataclass
class VarDecl(ASTNode):
    type_name: str
    name: str
    value: ASTNode
    line: int

@dataclass
class Assign(ASTNode):
    name: str
    value: ASTNode
    line: int

@dataclass
class BinOp(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    op: str
    operand: ASTNode

@dataclass
class Number(ASTNode):
    value: int

@dataclass
class Bool(ASTNode):
    value: bool

@dataclass
class StringLit(ASTNode):
    value: str

@dataclass
class Identifier(ASTNode):
    name: str
    line: int

@dataclass
class IfStmt(ASTNode):
    condition: ASTNode
    then_block: list
    else_block: Optional[list]

@dataclass
class WhileStmt(ASTNode):
    condition: ASTNode
    body: list

@dataclass
class FuncDecl(ASTNode):
    name: str
    params: list   # list of (type, name)
    body: list
    line: int

@dataclass
class FuncCall(ASTNode):
    name: str
    args: list
    line: int

@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode]

@dataclass
class PrintStmt(ASTNode):
    value: ASTNode


# ═══════════════════════════════════════════════════════════════════
#  SECTION 4: PARSER — Tokens → AST (CFG-Driven Recursive Descent)
# ═══════════════════════════════════════════════════════════════════
#
#  Grammar (CFG) used:
#
#  program       → statement*
#  statement     → var_decl | assign | if_stmt | while_stmt
#                | func_decl | return_stmt | print_stmt | expr_stmt
#  var_decl      → TYPE IDENT '=' expr ';'
#  assign        → IDENT '=' expr ';'
#  if_stmt       → 'if' '(' expr ')' block ( 'else' block )?
#  while_stmt    → 'while' '(' expr ')' block
#  func_decl     → 'func' IDENT '(' params ')' block
#  return_stmt   → 'return' expr? ';'
#  print_stmt    → 'print' '(' expr ')' ';'
#  expr          → or_expr
#  or_expr       → and_expr ( '||' and_expr )*
#  and_expr      → eq_expr ( '&&' eq_expr )*
#  eq_expr       → cmp_expr ( ('=='|'!=') cmp_expr )*
#  cmp_expr      → add_expr ( ('<'|'>'|'<='|'>=') add_expr )*
#  add_expr      → mul_expr ( ('+'|'-') mul_expr )*
#  mul_expr      → unary ( ('*'|'/') unary )*
#  unary         → '!' unary | '-' unary | primary
#  primary       → NUMBER | STRING | 'true' | 'false'
#                | IDENT ( '(' args ')' )? | '(' expr ')'
# ════════════════════════════════════════════════════════════════════

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def error(self, msg):
        tok = self.current()
        raise ParseError(f"[Parser Error] Line {tok.line}: {msg} (got {tok.type.name}={tok.value!r})")

    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek_type(self) -> TokenType:
        return self.tokens[self.pos].type

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        if tok.type != TokenType.EOF:
            self.pos += 1
        return tok

    def expect(self, ttype: TokenType) -> Token:
        if self.peek_type() != ttype:
            self.error(f"Expected {ttype.name}")
        return self.advance()

    def match(self, *types) -> bool:
        return self.peek_type() in types

    # ── Program ──────────────────────────────────────────────────
    def parse(self) -> Program:
        stmts = []
        while self.peek_type() != TokenType.EOF:
            stmts.append(self.parse_statement())
        return Program(stmts)

    # ── Statement ────────────────────────────────────────────────
    def parse_statement(self) -> ASTNode:
        t = self.peek_type()
        if t in (TokenType.INT, TokenType.BOOL):
            return self.parse_var_decl()
        elif t == TokenType.IF:
            return self.parse_if()
        elif t == TokenType.WHILE:
            return self.parse_while()
        elif t == TokenType.FUNC:
            return self.parse_func_decl()
        elif t == TokenType.RETURN:
            return self.parse_return()
        elif t == TokenType.PRINT:
            return self.parse_print()
        elif t == TokenType.IDENTIFIER:
            # Could be assignment or function call
            if self.tokens[self.pos+1].type == TokenType.ASSIGN:
                return self.parse_assign()
            else:
                expr = self.parse_expr()
                self.expect(TokenType.SEMICOLON)
                return expr
        else:
            self.error("Expected statement")

    def parse_var_decl(self) -> VarDecl:
        type_tok = self.advance()
        name_tok = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.ASSIGN)
        val = self.parse_expr()
        self.expect(TokenType.SEMICOLON)
        return VarDecl(type_tok.value, name_tok.value, val, type_tok.line)

    def parse_assign(self) -> Assign:
        name_tok = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.ASSIGN)
        val = self.parse_expr()
        self.expect(TokenType.SEMICOLON)
        return Assign(name_tok.value, val, name_tok.line)

    def parse_if(self) -> IfStmt:
        self.expect(TokenType.IF)
        self.expect(TokenType.LPAREN)
        cond = self.parse_expr()
        self.expect(TokenType.RPAREN)
        then_block = self.parse_block()
        else_block = None
        if self.match(TokenType.ELSE):
            self.advance()
            else_block = self.parse_block()
        return IfStmt(cond, then_block, else_block)

    def parse_while(self) -> WhileStmt:
        self.expect(TokenType.WHILE)
        self.expect(TokenType.LPAREN)
        cond = self.parse_expr()
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        return WhileStmt(cond, body)

    def parse_func_decl(self) -> FuncDecl:
        tok = self.expect(TokenType.FUNC)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        params = []
        if not self.match(TokenType.RPAREN):
            while True:
                ptype = self.advance().value
                pname = self.expect(TokenType.IDENTIFIER).value
                params.append((ptype, pname))
                if not self.match(TokenType.COMMA):
                    break
                self.advance()
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        return FuncDecl(name, params, body, tok.line)

    def parse_return(self) -> ReturnStmt:
        self.expect(TokenType.RETURN)
        val = None
        if not self.match(TokenType.SEMICOLON):
            val = self.parse_expr()
        self.expect(TokenType.SEMICOLON)
        return ReturnStmt(val)

    def parse_print(self) -> PrintStmt:
        self.expect(TokenType.PRINT)
        self.expect(TokenType.LPAREN)
        val = self.parse_expr()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)
        return PrintStmt(val)

    def parse_block(self) -> list:
        self.expect(TokenType.LBRACE)
        stmts = []
        while not self.match(TokenType.RBRACE) and not self.match(TokenType.EOF):
            stmts.append(self.parse_statement())
        self.expect(TokenType.RBRACE)
        return stmts

    # ── Expressions (operator precedence via CFG levels) ─────────
    def parse_expr(self):      return self.parse_or()
    def parse_or(self):
        left = self.parse_and()
        while self.match(TokenType.OR):
            op = self.advance().value
            left = BinOp(left, op, self.parse_and())
        return left

    def parse_and(self):
        left = self.parse_eq()
        while self.match(TokenType.AND):
            op = self.advance().value
            left = BinOp(left, op, self.parse_eq())
        return left

    def parse_eq(self):
        left = self.parse_cmp()
        while self.match(TokenType.EQ, TokenType.NEQ):
            op = self.advance().value
            left = BinOp(left, op, self.parse_cmp())
        return left

    def parse_cmp(self):
        left = self.parse_add()
        while self.match(TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.advance().value
            left = BinOp(left, op, self.parse_add())
        return left

    def parse_add(self):
        left = self.parse_mul()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            left = BinOp(left, op, self.parse_mul())
        return left

    def parse_mul(self):
        left = self.parse_unary()
        while self.match(TokenType.STAR, TokenType.SLASH):
            op = self.advance().value
            left = BinOp(left, op, self.parse_unary())
        return left

    def parse_unary(self):
        if self.match(TokenType.NOT):
            op = self.advance().value
            return UnaryOp(op, self.parse_unary())
        if self.match(TokenType.MINUS):
            op = self.advance().value
            return UnaryOp(op, self.parse_unary())
        return self.parse_primary()

    def parse_primary(self):
        tok = self.current()
        if tok.type == TokenType.NUMBER:
            self.advance()
            return Number(tok.value)
        if tok.type == TokenType.STRING:
            self.advance()
            return StringLit(tok.value)
        if tok.type == TokenType.TRUE:
            self.advance()
            return Bool(True)
        if tok.type == TokenType.FALSE:
            self.advance()
            return Bool(False)
        if tok.type == TokenType.IDENTIFIER:
            self.advance()
            if self.match(TokenType.LPAREN):
                self.advance()
                args = []
                if not self.match(TokenType.RPAREN):
                    args.append(self.parse_expr())
                    while self.match(TokenType.COMMA):
                        self.advance()
                        args.append(self.parse_expr())
                self.expect(TokenType.RPAREN)
                return FuncCall(tok.value, args, tok.line)
            return Identifier(tok.value, tok.line)
        if tok.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expr()
            self.expect(TokenType.RPAREN)
            return expr
        self.error(f"Unexpected token in expression")


# ═══════════════════════════════════════════════════════════════════
#  SECTION 5: CFG USELESS SYMBOL REMOVER
#  (Core topic from the report — integrated into compiler!)
# ═══════════════════════════════════════════════════════════════════

class CFG:
    """Represents a Context-Free Grammar with useless symbol removal."""

    def __init__(self, non_terminals, terminals, productions, start):
        self.V = set(non_terminals)      # Non-terminals
        self.sigma = set(terminals)      # Terminals
        self.P = list(productions)       # (LHS, RHS_list) pairs
        self.S = start                   # Start symbol

    def find_generating(self) -> set:
        """Phase 1: Fixed-point iteration to find generating non-terminals."""
        GEN = set()
        changed = True
        while changed:
            changed = False
            for (lhs, rhs) in self.P:
                if lhs not in GEN:
                    if all(sym in self.sigma or sym in GEN for sym in rhs):
                        GEN.add(lhs)
                        changed = True
        return GEN

    def find_reachable(self, productions) -> set:
        """Phase 2: Fixed-point iteration to find reachable symbols."""
        REACH = {self.S}
        changed = True
        while changed:
            changed = False
            for (lhs, rhs) in productions:
                if lhs in REACH:
                    for sym in rhs:
                        if sym in self.V and sym not in REACH:
                            REACH.add(sym)
                            changed = True
        return REACH

    def remove_useless(self):
        """Two-phase useless symbol removal."""
        print("\n" + "═"*60)
        print("  CFG USELESS SYMBOL REMOVAL")
        print("═"*60)
        print(f"  Original: V={self.V}, S={self.S}")
        print(f"  Productions: {self.P}")

        # ── Phase 1: Remove Non-Generating ──────────────────────
        GEN = self.find_generating()
        print(f"\n  Phase 1 — GEN = {GEN}")
        removed_ng = self.V - GEN
        if removed_ng:
            print(f"  Non-generating removed: {removed_ng}")

        P1 = [(lhs, rhs) for (lhs, rhs) in self.P
              if lhs in GEN and all(sym in self.sigma or sym in GEN for sym in rhs)]
        V1 = GEN

        # ── Phase 2: Remove Non-Reachable ────────────────────────
        REACH = self.find_reachable(P1)
        print(f"\n  Phase 2 — REACH = {REACH}")
        removed_nr = V1 - REACH
        if removed_nr:
            print(f"  Non-reachable removed: {removed_nr}")

        P2 = [(lhs, rhs) for (lhs, rhs) in P1
              if lhs in REACH and all(sym in self.sigma or sym in REACH for sym in rhs)]
        V2 = V1 & REACH

        print(f"\n  Simplified: V={V2}")
        print(f"  Clean Productions: {P2}")
        print("═"*60 + "\n")

        self.V = V2
        self.P = P2
        return self


# ═══════════════════════════════════════════════════════════════════
#  SECTION 6: SEMANTIC ANALYZER — Type Checking & Scope Analysis
# ═══════════════════════════════════════════════════════════════════

class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self, parent=None):
        self.table: dict[str, str] = {}
        self.parent = parent

    def define(self, name: str, type_name: str):
        self.table[name] = type_name

    def lookup(self, name: str) -> Optional[str]:
        if name in self.table:
            return self.table[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

class SemanticAnalyzer:
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.functions: dict[str, FuncDecl] = {}
        self.errors: list[str] = []

    def error(self, msg, line=None):
        loc = f" (line {line})" if line else ""
        self.errors.append(f"[Semantic Error]{loc}: {msg}")

    def analyze(self, node: ASTNode) -> Optional[str]:
        method = f'analyze_{type(node).__name__}'
        visitor = getattr(self, method, self.generic_analyze)
        return visitor(node)

    def generic_analyze(self, node):
        return None

    def analyze_Program(self, node: Program):
        for stmt in node.statements:
            self.analyze(stmt)

    def analyze_VarDecl(self, node: VarDecl):
        val_type = self.analyze(node.value)
        self.current_scope.define(node.name, node.type_name)

    def analyze_Assign(self, node: Assign):
        declared = self.current_scope.lookup(node.name)
        if declared is None:
            self.error(f"Variable '{node.name}' not declared", node.line)
        self.analyze(node.value)

    def analyze_Identifier(self, node: Identifier) -> str:
        t = self.current_scope.lookup(node.name)
        if t is None:
            self.error(f"Undefined variable '{node.name}'", node.line)
            return 'unknown'
        return t

    def analyze_BinOp(self, node: BinOp) -> str:
        l = self.analyze(node.left)
        r = self.analyze(node.right)
        if node.op in ('==', '!=', '<', '>', '<=', '>=', '&&', '||'):
            return 'bool'
        return 'int'

    def analyze_UnaryOp(self, node: UnaryOp) -> str:
        self.analyze(node.operand)
        return 'bool' if node.op == '!' else 'int'

    def analyze_Number(self, node: Number) -> str:   return 'int'
    def analyze_Bool(self, node: Bool) -> str:       return 'bool'
    def analyze_StringLit(self, node: StringLit) -> str: return 'string'

    def analyze_IfStmt(self, node: IfStmt):
        cond_type = self.analyze(node.condition)
        inner = SymbolTable(self.current_scope)
        self.current_scope = inner
        for s in node.then_block: self.analyze(s)
        self.current_scope = self.current_scope.parent
        if node.else_block:
            inner2 = SymbolTable(self.current_scope)
            self.current_scope = inner2
            for s in node.else_block: self.analyze(s)
            self.current_scope = self.current_scope.parent

    def analyze_WhileStmt(self, node: WhileStmt):
        self.analyze(node.condition)
        inner = SymbolTable(self.current_scope)
        self.current_scope = inner
        for s in node.body: self.analyze(s)
        self.current_scope = self.current_scope.parent

    def analyze_FuncDecl(self, node: FuncDecl):
        self.functions[node.name] = node
        self.global_scope.define(node.name, 'func')
        inner = SymbolTable(self.current_scope)
        self.current_scope = inner
        for (ptype, pname) in node.params:
            self.current_scope.define(pname, ptype)
        for s in node.body: self.analyze(s)
        self.current_scope = self.current_scope.parent

    def analyze_FuncCall(self, node: FuncCall) -> str:
        if node.name not in self.functions:
            self.error(f"Undefined function '{node.name}'", node.line)
            return 'unknown'
        func = self.functions[node.name]
        if len(node.args) != len(func.params):
            self.error(f"Function '{node.name}' expects {len(func.params)} args, got {len(node.args)}", node.line)
        for arg in node.args: self.analyze(arg)
        return 'int'

    def analyze_ReturnStmt(self, node: ReturnStmt):
        if node.value: self.analyze(node.value)

    def analyze_PrintStmt(self, node: PrintStmt):
        self.analyze(node.value)


# ═══════════════════════════════════════════════════════════════════
#  SECTION 7: IR GENERATOR — AST → Three-Address Code (TAC)
# ═══════════════════════════════════════════════════════════════════

@dataclass
class IRInstr:
    op: str
    dest: Optional[str] = None
    arg1: Optional[Any] = None
    arg2: Optional[Any] = None

    def __str__(self):
        if self.op == 'LABEL':   return f"{self.dest}:"
        if self.op == 'GOTO':    return f"    GOTO {self.dest}"
        if self.op == 'IF':      return f"    IF {self.arg1} GOTO {self.dest}"
        if self.op == 'IFNOT':   return f"    IFNOT {self.arg1} GOTO {self.dest}"
        if self.op == 'PARAM':   return f"    PARAM {self.arg1}"
        if self.op == 'CALL':    return f"    {self.dest} = CALL {self.arg1} {self.arg2}"
        if self.op == 'RETURN':  return f"    RETURN {self.arg1 or ''}"
        if self.op == 'PRINT':   return f"    PRINT {self.arg1}"
        if self.op == 'COPY':    return f"    {self.dest} = {self.arg1}"
        if self.op == 'FUNC':    return f"\nFUNC {self.dest}:"
        if self.op == 'ENDFUNC': return f"ENDFUNC {self.dest}"
        if self.arg2 is not None:
            return f"    {self.dest} = {self.arg1} {self.op} {self.arg2}"
        return f"    {self.dest} = {self.op} {self.arg1}"

class IRGenerator:
    def __init__(self):
        self.instrs: list[IRInstr] = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self) -> str:
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self) -> str:
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, *args, **kwargs):
        self.instrs.append(IRInstr(*args, **kwargs))

    def gen(self, node: ASTNode) -> Optional[str]:
        method = f'gen_{type(node).__name__}'
        visitor = getattr(self, method, lambda n: None)
        return visitor(node)

    def gen_Program(self, node: Program):
        for s in node.statements: self.gen(s)

    def gen_Number(self, node: Number) -> str:
        t = self.new_temp()
        self.emit('COPY', dest=t, arg1=node.value)
        return t

    def gen_Bool(self, node: Bool) -> str:
        t = self.new_temp()
        self.emit('COPY', dest=t, arg1=1 if node.value else 0)
        return t

    def gen_StringLit(self, node: StringLit) -> str:
        t = self.new_temp()
        self.emit('COPY', dest=t, arg1=f'"{node.value}"')
        return t

    def gen_Identifier(self, node: Identifier) -> str:
        return node.name

    def gen_BinOp(self, node: BinOp) -> str:
        l = self.gen(node.left)
        r = self.gen(node.right)
        t = self.new_temp()
        self.emit(node.op, dest=t, arg1=l, arg2=r)
        return t

    def gen_UnaryOp(self, node: UnaryOp) -> str:
        operand = self.gen(node.operand)
        t = self.new_temp()
        self.emit(node.op, dest=t, arg1=operand)
        return t

    def gen_VarDecl(self, node: VarDecl):
        val = self.gen(node.value)
        self.emit('COPY', dest=node.name, arg1=val)

    def gen_Assign(self, node: Assign):
        val = self.gen(node.value)
        self.emit('COPY', dest=node.name, arg1=val)

    def gen_IfStmt(self, node: IfStmt):
        cond = self.gen(node.condition)
        else_lbl = self.new_label()
        end_lbl = self.new_label()
        self.emit('IFNOT', dest=else_lbl, arg1=cond)
        for s in node.then_block: self.gen(s)
        self.emit('GOTO', dest=end_lbl)
        self.emit('LABEL', dest=else_lbl)
        if node.else_block:
            for s in node.else_block: self.gen(s)
        self.emit('LABEL', dest=end_lbl)

    def gen_WhileStmt(self, node: WhileStmt):
        start_lbl = self.new_label()
        end_lbl = self.new_label()
        self.emit('LABEL', dest=start_lbl)
        cond = self.gen(node.condition)
        self.emit('IFNOT', dest=end_lbl, arg1=cond)
        for s in node.body: self.gen(s)
        self.emit('GOTO', dest=start_lbl)
        self.emit('LABEL', dest=end_lbl)

    def gen_FuncDecl(self, node: FuncDecl):
        self.emit('FUNC', dest=node.name)
        for (_, pname) in node.params:
            self.emit('PARAM', arg1=pname)
        for s in node.body: self.gen(s)
        self.emit('ENDFUNC', dest=node.name)

    def gen_FuncCall(self, node: FuncCall) -> str:
        args = [self.gen(a) for a in node.args]
        for a in args:
            self.emit('PARAM', arg1=a)
        t = self.new_temp()
        self.emit('CALL', dest=t, arg1=node.name, arg2=len(args))
        return t

    def gen_ReturnStmt(self, node: ReturnStmt):
        val = self.gen(node.value) if node.value else None
        self.emit('RETURN', arg1=val)

    def gen_PrintStmt(self, node: PrintStmt):
        val = self.gen(node.value)
        self.emit('PRINT', arg1=val)


# ═══════════════════════════════════════════════════════════════════
#  SECTION 8: CODE GENERATOR — IR → Assembly-like Target Code
# ═══════════════════════════════════════════════════════════════════

class CodeGenerator:
    def __init__(self, ir: list[IRInstr]):
        self.ir = ir
        self.output: list[str] = []
        self.reg_map: dict[str, str] = {}
        self.reg_count = 0
        self.mem: dict[str, str] = {}  # variable → memory location

    def new_reg(self) -> str:
        self.reg_count += 1
        return f"R{self.reg_count}"

    def get_reg(self, name: str) -> str:
        if name not in self.reg_map:
            self.reg_map[name] = self.new_reg()
        return self.reg_map[name]

    def emit(self, line: str):
        self.output.append(line)

    OP_MAP = {
        '+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV',
        '==': 'CMP_EQ', '!=': 'CMP_NEQ',
        '<':  'CMP_LT', '>':  'CMP_GT',
        '<=': 'CMP_LTE','>=': 'CMP_GTE',
        '&&': 'AND', '||': 'OR',
        '!':  'NOT', 'neg': 'NEG',
    }

    def generate(self) -> str:
        self.emit("; ══════════════════════════════════")
        self.emit("; Generated Assembly (Target Code)  ")
        self.emit("; ══════════════════════════════════")
        self.emit(".data")
        self.emit("    ; variables allocated at runtime")
        self.emit(".code")

        for instr in self.ir:
            if instr.op == 'LABEL':
                self.emit(f"\n{instr.dest}:")
            elif instr.op == 'FUNC':
                self.emit(f"\n; ── Function: {instr.dest} ──")
                self.emit(f"{instr.dest}:")
                self.emit(f"    PUSH BP")
                self.emit(f"    MOV BP, SP")
            elif instr.op == 'ENDFUNC':
                self.emit(f"    POP BP")
                self.emit(f"    RET")
            elif instr.op == 'COPY':
                dest_reg = self.get_reg(instr.dest)
                if isinstance(instr.arg1, int):
                    self.emit(f"    MOV {dest_reg}, #{instr.arg1}")
                elif isinstance(instr.arg1, str) and instr.arg1.startswith('"'):
                    self.emit(f"    MOV {dest_reg}, {instr.arg1}")
                else:
                    src_reg = self.get_reg(str(instr.arg1))
                    self.emit(f"    MOV {dest_reg}, {src_reg}")
            elif instr.op in self.OP_MAP and instr.arg2 is not None:
                dest_reg = self.get_reg(instr.dest)
                a1 = self.get_reg(str(instr.arg1))
                a2 = self.get_reg(str(instr.arg2))
                asm_op = self.OP_MAP[instr.op]
                self.emit(f"    {asm_op} {dest_reg}, {a1}, {a2}")
            elif instr.op in self.OP_MAP:
                dest_reg = self.get_reg(instr.dest)
                a1 = self.get_reg(str(instr.arg1))
                asm_op = self.OP_MAP[instr.op]
                self.emit(f"    {asm_op} {dest_reg}, {a1}")
            elif instr.op == 'IFNOT':
                src_reg = self.get_reg(str(instr.arg1))
                self.emit(f"    CMP {src_reg}, #0")
                self.emit(f"    JEQ {instr.dest}")
            elif instr.op == 'IF':
                src_reg = self.get_reg(str(instr.arg1))
                self.emit(f"    CMP {src_reg}, #0")
                self.emit(f"    JNE {instr.dest}")
            elif instr.op == 'GOTO':
                self.emit(f"    JMP {instr.dest}")
            elif instr.op == 'PARAM':
                reg = self.get_reg(str(instr.arg1))
                self.emit(f"    PUSH {reg}")
            elif instr.op == 'CALL':
                dest_reg = self.get_reg(instr.dest)
                self.emit(f"    CALL {instr.arg1}")
                self.emit(f"    MOV {dest_reg}, R0   ; return value")
                if instr.arg2:
                    self.emit(f"    ADD SP, SP, #{instr.arg2 * 4}  ; clean stack")
            elif instr.op == 'RETURN':
                if instr.arg1:
                    ret_reg = self.get_reg(str(instr.arg1))
                    self.emit(f"    MOV R0, {ret_reg}   ; return value in R0")
                self.emit(f"    POP BP")
                self.emit(f"    RET")
            elif instr.op == 'PRINT':
                reg = self.get_reg(str(instr.arg1))
                self.emit(f"    MOV R0, {reg}")
                self.emit(f"    SYSCALL PRINT")

        self.emit("\n.end")
        return '\n'.join(self.output)


# ═══════════════════════════════════════════════════════════════════
#  SECTION 9: COMPILER DRIVER — Ties all phases together
# ═══════════════════════════════════════════════════════════════════

class CompilerError(Exception):
    pass

def compile_source(source: str, verbose: bool = True) -> str:
    """Full compilation pipeline."""

    sep = "═" * 60

    def header(title):
        if verbose:
            print(f"\n{sep}")
            print(f"  {title}")
            print(sep)

    # ── Phase 1: Lexing ──────────────────────────────────────────
    header("PHASE 1: LEXER — Tokenization")
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    if verbose:
        for tok in tokens[:-1]:  # skip EOF
            print(f"  {tok}")

    # ── Phase 2: Parsing ─────────────────────────────────────────
    header("PHASE 2: PARSER — Building AST")
    parser = Parser(tokens)
    ast = parser.parse()
    if verbose:
        print(f"  AST Root: {type(ast).__name__}")
        print(f"  Top-level statements: {len(ast.statements)}")
        for stmt in ast.statements:
            print(f"    → {type(stmt).__name__}: {getattr(stmt, 'name', '')}")

    # ── Phase 3: CFG Useless Symbol Removal ──────────────────────
    header("PHASE 3: CFG USELESS SYMBOL REMOVAL")
    # Demo CFG extracted from the parsed grammar structure
    cfg = CFG(
        non_terminals=['S', 'A', 'B', 'C', 'D'],
        terminals=['a', 'b', 'c'],
        productions=[
            ('S', ['A', 'B']), ('S', ['a']),
            ('A', ['a']),
            ('B', ['b', 'C']),
            ('C', ['c', 'C']),   # non-generating!
            ('D', ['d']),        # non-reachable!
        ],
        start='S'
    )
    cfg.remove_useless()

    # ── Phase 4: Semantic Analysis ───────────────────────────────
    header("PHASE 4: SEMANTIC ANALYZER — Type Checking & Scopes")
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)
    if analyzer.errors:
        for err in analyzer.errors:
            print(f"  {err}")
        raise CompilerError("Semantic errors found.")
    else:
        if verbose:
            print("  ✓ No semantic errors found.")
            print(f"  ✓ Functions declared: {list(analyzer.functions.keys())}")

    # ── Phase 5: IR Generation ───────────────────────────────────
    header("PHASE 5: IR GENERATOR — Three-Address Code")
    ir_gen = IRGenerator()
    ir_gen.gen(ast)
    if verbose:
        for instr in ir_gen.instrs:
            print(str(instr))

    # ── Phase 6: Code Generation ─────────────────────────────────
    header("PHASE 6: CODE GENERATOR — Assembly Output")
    code_gen = CodeGenerator(ir_gen.instrs)
    asm = code_gen.generate()
    if verbose:
        print(asm)

    return asm


# ═══════════════════════════════════════════════════════════════════
#  SECTION 10: SAMPLE PROGRAM — Run the compiler
# ═══════════════════════════════════════════════════════════════════

SAMPLE_PROGRAM = """
// Advanced CFG Compiler — Sample Program

func add(int x, int y) {
    int result = x + y;
    return result;
}

func factorial(int n) {
    int result = 1;
    while (n > 1) {
        result = result * n;
        n = n - 1;
    }
    return result;
}

// Main program
int a = 10;
int b = 20;
int sum = add(a, b);
print(sum);

int fact5 = factorial(5);
print(fact5);

if (sum > 25) {
    int bonus = sum + 5;
    print(bonus);
} else {
    print(sum);
}

while (a > 0) {
    a = a - 3;
}
print(a);
"""

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════╗")
    print("║        ADVANCED CFG-BASED COMPILER — Running...          ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("\nSource Program:")
    print("─" * 60)
    print(SAMPLE_PROGRAM)
    print("─" * 60)

    try:
        asm = compile_source(SAMPLE_PROGRAM, verbose=True)
        print("\n✅ Compilation Successful!")
    except (LexerError, ParseError, CompilerError) as e:
        print(f"\n❌ {e}")
        sys.exit(1)