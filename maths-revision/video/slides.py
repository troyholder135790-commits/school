# -*- coding: utf-8 -*-
"""Slide definitions for the revision video. Each scene = (section, title, body_html, narration)."""

def eq(s, cls=""):
    return f'<div class="eq {cls}">{s}</div>'

def cards(items):
    out = '<div class="cards">'
    for n, t, b in items:
        out += f'<div class="card"><span class="n">{n}</span><span class="t">{t}</span><span class="b">{b}</span></div>'
    return out + '</div>'

def steps(items):
    return '<div class="steps">' + ''.join(f'<div class="st">{i}</div>' for i in items) + '</div>'

def note(t, kind="tip"):
    return f'<div class="note {kind}">{t}</div>'

A = "Chapter 8 · Factorising"
B = "Algebraic Fractions"
C = "Chapter 13 · Pythagoras"

SCENES = [

("Grade 9 Mathematics", "Factorising &amp; Pythagoras",
 '<div class="hero">Everything you need for tomorrow&rsquo;s test</div>'
 + cards([("8", "Chapter 8", "Factorising fully &amp; algebraic fractions"),
          ("13", "Chapter 13", "The Theorem of Pythagoras")])
 + note("Every single question on your worksheet is worked out in this video.", "tip"),
 "Welcome. This is your full revision for tomorrow's maths test. We are covering two chapters. Chapter eight, factorising. And chapter thirteen, the theorem of Pythagoras. Every question on your worksheet is worked out in this video. Let's go."),

(A, "The Golden Order",
 '<div class="hero">Factorising is not guessing. It is a decision tree.</div>'
 + cards([("1", "Common factor?", "Take out the HCF. ALWAYS do this first."),
          ("2", "Two terms?", "Difference of two squares"),
          ("3", "Three terms?", "Trinomial"),
          ("4", "Four terms?", "Group in pairs")]),
 "Start with the most important idea in chapter eight. Factorising is not guessing. It is a decision tree with four checks, and you do them in this order, every single time. One. Is there a common factor? Two. Are there two terms? Three. Are there three terms? Four. Are there four terms?"),

(A, "Count the terms",
 steps(['<b>Step 1.</b> Take out the highest common factor &mdash; numbers <i>and</i> letters.',
        '<b>Step 2.</b> Now count what is left inside the bracket.',
        '<b>2 terms</b> &rarr; difference of two squares &nbsp;<span class="m">a&sup2; &minus; b&sup2; = (a &minus; b)(a + b)</span>',
        '<b>3 terms</b> &rarr; trinomial &nbsp;<span class="m">x&sup2; + bx + c</span>',
        '<b>4 terms</b> &rarr; group into two pairs']),
 "Check one is always first. Take out the highest common factor, numbers and letters. Then count what is left in the bracket. Two terms means difference of two squares. Three terms means a trinomial. Four terms means group them in pairs."),

(A, "&ldquo;Factorise FULLY&rdquo; &mdash; the trap",
 '<div class="hero">After every step, look at each bracket <u>again</u>.</div>'
 + eq('8(x<sup>4</sup> &minus; 1)', "bad")
 + '<div class="lbl bad">Not finished &mdash; this bracket still factorises!</div>'
 + note("Students lose marks every single year by stopping too early. Faktoriseer volledig = keep going.", "warn"),
 "And here is the trap. When the question says factorise fully, you must look at every bracket again after each step. Students lose marks every year by stopping too early."),

(A, "Rule 1 &mdash; Common Factor",
 eq('ka + kb = k(a + b)', "big")
 + steps(['Find the <b>highest common factor</b> of every term.',
          'Write it <b>outside</b> a bracket.',
          '<b>Divide</b> each original term by it to get what goes inside.',
          'For letters, take the <b>lowest power</b> that appears in every term.']),
 "Rule one. Common factor. Find the highest common factor of every term, write it outside a bracket, and divide each term by it. For letters, take the lowest power that appears in every term."),

(A, "Worked: (d)(1) &nbsp; 7x + 14",
 steps(['HCF of 7 and 14 is <b>7</b>. There is no <span class="m">x</span> in both terms, so no letter comes out.',
        '<span class="m">7x &divide; 7 = x</span> &nbsp;&nbsp; <span class="m">14 &divide; 7 = 2</span>'])
 + eq('7x + 14 = <span class="hl">7(x + 2)</span>'),
 "Seven x plus fourteen. The highest common factor of seven and fourteen is seven. Seven x divided by seven is x. Fourteen divided by seven is two. So the answer is seven, bracket, x plus two."),

(A, "Worked: (d)(7) &nbsp; 4a&sup2; + 3a",
 steps(['Numbers: HCF of 4 and 3 is just 1 &mdash; nothing comes out.',
        'Letters: <span class="m">a&sup2;</span> and <span class="m">a</span> &rarr; lowest power is <b><span class="m">a</span></b>.',
        '<span class="m">4a&sup2; &divide; a = 4a</span> &nbsp;&nbsp; <span class="m">3a &divide; a = 3</span>'])
 + eq('4a&sup2; + 3a = <span class="hl">a(4a + 3)</span>'),
 "Four a squared plus three a. Four and three have no common number factor. But both terms contain an a. Take out the lowest power, which is a. Four a squared divided by a is four a. Three a divided by a is three. Answer: a, bracket, four a plus three."),

(A, "Rule 2 &mdash; Difference of Two Squares",
 eq('a&sup2; &minus; b&sup2; = (a &minus; b)(a + b)', "big")
 + '<div class="hero">All three conditions must be true:</div>'
 + cards([("i", "Two terms", "exactly two"),
          ("ii", "A MINUS between them", "not a plus"),
          ("iii", "Both perfect squares", "you can square root both")]),
 "Rule two. Difference of two squares. a squared minus b squared equals, bracket a minus b, bracket a plus b. Three conditions, and all must be true. Two terms. A minus sign between them. And both terms are perfect squares."),

(A, "A SUM of squares does NOT factorise",
 eq('a&sup2; + b&sup2;', "bad") + '<div class="lbl bad">PRIME &mdash; leave it alone</div>'
 + eq('a&sup2; &minus; b&sup2;', "good") + '<div class="lbl good">= (a &minus; b)(a + b)</div>'
 + note("This is a favourite trap question. Only the MINUS version breaks apart.", "warn"),
 "Very important. A sum of two squares does not factorise. a squared plus b squared is prime. Only the minus version breaks apart. This is a favourite trap question."),

(A, "Worked: (d)(10) &nbsp; 4m&sup2; &minus; 1",
 steps(['Two terms &check; &nbsp; minus sign &check; &nbsp; both perfect squares &check;',
        '<span class="m">&radic;(4m&sup2;) = 2m</span> &nbsp;&nbsp;and&nbsp;&nbsp; <span class="m">&radic;1 = 1</span>'])
 + eq('4m&sup2; &minus; 1 = <span class="hl">(2m &minus; 1)(2m + 1)</span>'),
 "Four m squared minus one. Two terms, a minus sign, and both are perfect squares. The square root of four m squared is two m. The square root of one is one. So it factorises to, bracket two m minus one, bracket two m plus one."),

(A, "Worked: (d)(21) &nbsp; 8x&#8312; &minus; 8",
 steps(['<b>Step 1 &mdash; common factor FIRST:</b> take out 8'])
 + eq('= 8(x<sup>8</sup> &minus; 1)')
 + steps(['<b>Step 2 &mdash; two terms, minus, both squares.</b> To square root a power, <b>halve it</b>: <span class="m">&radic;(x<sup>8</sup>) = x<sup>4</sup></span>'])
 + eq('= 8(x<sup>4</sup> &minus; 1)(x<sup>4</sup> + 1)'),
 "Now the big one. Eight x to the eighth, minus eight. Step one, always common factor first. Take out eight. That leaves x to the eighth minus one. Step two, that bracket has two terms, a minus, and both are perfect squares. Remember, to square root a power you halve it. So we get x to the fourth minus one, times x to the fourth plus one."),

(A, "(d)(21) continued &mdash; keep going!",
 steps(['<b>Step 3 &mdash; look again:</b> <span class="m">x<sup>4</sup> &minus; 1</span> is STILL a difference of squares'])
 + eq('= 8(x&sup2; &minus; 1)(x&sup2; + 1)(x<sup>4</sup> + 1)')
 + steps(['<b>Step 4 &mdash; look again:</b> <span class="m">x&sup2; &minus; 1</span> is STILL a difference of squares'])
 + eq('<span class="hl">= 8(x &minus; 1)(x + 1)(x&sup2; + 1)(x<sup>4</sup> + 1)</span>')
 + note("Stop here: x&sup2;+1 and x&#8308;+1 are SUMS of squares.", "tip"),
 "Step three, look again. x to the fourth minus one is still a difference of squares. That gives x squared minus one, times x squared plus one. Step four, look again. x squared minus one is still a difference of squares. So the final answer is eight, x minus one, x plus one, x squared plus one, x to the fourth plus one. We stop there, because the plus brackets are sums of squares."),

(A, "Rule 3 &mdash; Trinomials",
 eq('x&sup2; + bx + c', "big")
 + '<div class="hero">Find two numbers that:</div>'
 + cards([("&times;", "MULTIPLY to give c", "the last number"),
          ("+", "ADD to give b", "the middle number")])
 + eq('= (x + first)(x + second)'),
 "Rule three. Trinomials. For x squared plus b x plus c, you need two numbers that multiply to give c, the last number, and add to give b, the middle number."),

(A, "The Sign Table &mdash; learn this",
 '<table class="sg"><tr><th>Last sign</th><th>Middle sign</th><th>Brackets</th><th>The two numbers</th></tr>'
 '<tr><td>+</td><td>+</td><td>( + )( + )</td><td><b>ADD</b> to the middle number</td></tr>'
 '<tr><td>+</td><td>&minus;</td><td>( &minus; )( &minus; )</td><td><b>ADD</b> to the middle number</td></tr>'
 '<tr><td>&minus;</td><td>+</td><td>( + )( &minus; )</td><td><b>SUBTRACT</b>; bigger one is <b>+</b></td></tr>'
 '<tr><td>&minus;</td><td>&minus;</td><td>( + )( &minus; )</td><td><b>SUBTRACT</b>; bigger one is <b>&minus;</b></td></tr></table>'
 + note("Last sign PLUS &rarr; both brackets take the MIDDLE sign, numbers ADD. &nbsp; Last sign MINUS &rarr; one of each, numbers SUBTRACT, and the BIGGER number takes the middle sign.", "tip"),
 "Learn this sign table and the guessing disappears. If the last sign is plus, both brackets take the middle sign, and the two numbers add up to the middle number. If the last sign is minus, you get one plus and one minus, the numbers have a difference equal to the middle number, and the bigger number takes the middle sign."),

(A, "All four questions use 27",
 '<div class="hero">Factor pairs of 27:</div>'
 + eq('1 &times; 27 &nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp; 3 &times; 9', "big")
 + cards([("+", "3 + 9 = 12", "gives the +12 and &minus;12 questions"),
          ("&minus;", "9 &minus; 3 = 6", "gives the +6 and &minus;6 questions")]),
 "All four trinomial questions on your worksheet use twenty seven. Its factor pairs are one times twenty seven, and three times nine. Three plus nine is twelve. Nine minus three is six. Those are the only two numbers you need."),

(A, "(d)(22) and (d)(23)",
 '<div class="split"><div>'
 + eq('x&sup2; + 12x + 27')
 + steps(['Last <b>+</b>, middle <b>+</b> &rarr; both brackets <b>+</b>', 'Need &times;27, +12 &rarr; <b>3 and 9</b>'])
 + eq('<span class="hl">= (x + 3)(x + 9)</span>')
 + '</div><div>'
 + eq('k&sup2; &minus; 12k + 27')
 + steps(['Last <b>+</b>, middle <b>&minus;</b> &rarr; both brackets <b>&minus;</b>', 'Need &times;27, +12 &rarr; <b>3 and 9</b>'])
 + eq('<span class="hl">= (k &minus; 3)(k &minus; 9)</span>')
 + '</div></div>',
 "x squared plus twelve x plus twenty seven. The last sign is plus and the middle sign is plus, so both brackets are plus. Three and nine. The answer is x plus three, x plus nine. Next one. k squared minus twelve k plus twenty seven. The last sign is plus and the middle sign is minus, so both brackets are minus. The answer is k minus three, k minus nine."),

(A, "(d)(24) and (d)(25)",
 '<div class="split"><div>'
 + eq('a&sup2; + 6a &minus; 27')
 + steps(['Last <b>&minus;</b> &rarr; one <b>+</b>, one <b>&minus;</b>', 'Difference of 6 &rarr; <b>9 and 3</b>', 'Middle is <b>+</b> &rarr; bigger (9) is <b>+</b>'])
 + eq('<span class="hl">= (a + 9)(a &minus; 3)</span>')
 + '</div><div>'
 + eq('y&sup2; &minus; 6y &minus; 27')
 + steps(['Last <b>&minus;</b> &rarr; one <b>+</b>, one <b>&minus;</b>', 'Difference of 6 &rarr; <b>9 and 3</b>', 'Middle is <b>&minus;</b> &rarr; bigger (9) is <b>&minus;</b>'])
 + eq('<span class="hl">= (y &minus; 9)(y + 3)</span>')
 + '</div></div>',
 "a squared plus six a minus twenty seven. The last sign is minus, so one bracket is plus and one is minus. A difference of six, so nine and three. The middle sign is plus, so the bigger number, nine, is positive. The answer is a plus nine, a minus three. Now, y squared minus six y minus twenty seven. Same numbers, but the middle sign is minus, so the bigger number, nine, is negative. The answer is y minus nine, y plus three."),

(A, "Always check by multiplying back",
 eq('(y &minus; 9)(y + 3)')
 + steps(['<span class="m">= y&sup2; + 3y &minus; 9y &minus; 27</span>',
          '<span class="m">= y&sup2; &minus; 6y &minus; 27</span> &nbsp; <span class="good">&check; correct</span>'])
 + note("Five seconds of FOIL catches every single sign error. Do it every time.", "tip"),
 "Always check by multiplying back out. y minus nine, times y plus three, gives y squared plus three y minus nine y minus twenty seven, which is y squared minus six y minus twenty seven. Correct. That takes five seconds and it catches every sign error."),

(A, "Rule 4a &mdash; a bracket can be a common factor",
 eq('4x(a + b) + 3(a + b)')
 + steps(['The bracket <span class="m">(a + b)</span> appears in <b>both</b> terms &rarr; take it out.',
          'What is left over: <span class="m">4x</span> from the first term, <span class="m">+3</span> from the second.'])
 + eq('<span class="hl">= (a + b)(4x + 3)</span>'),
 "Rule four. A whole bracket can be a common factor. Four x, bracket a plus b, plus three, bracket a plus b. The bracket a plus b is in both terms, so take it out. What is left is four x plus three. So the answer is a plus b, times four x plus three."),

(A, "Rule 4b &mdash; the SIGN FLIP trick",
 eq('(1 &minus; x) = &minus;(x &minus; 1)', "big")
 + eq('(&minus;4 &minus; x) = &minus;(x + 4)', "big")
 + note("If two brackets are the SAME BUT BACKWARDS, take a &minus;1 out of one of them so they match. This is worth a lot of marks.", "warn"),
 "Now the sign flip trick, and this one is worth a lot of marks. One minus x is the same as minus, bracket x minus one. If two brackets are the same but backwards, take a minus one out of one of them so that they match."),

(A, "Worked: (e)(4) &nbsp; x&sup2;(x &minus; 1) + 4(1 &minus; x)",
 steps(['Brackets are backwards: <span class="m">(x &minus; 1)</span> vs <span class="m">(1 &minus; x)</span>',
        '<b>Flip:</b> <span class="m">4(1 &minus; x) = &minus;4(x &minus; 1)</span>',
        '<span class="m">= x&sup2;(x &minus; 1) &minus; 4(x &minus; 1)</span> &nbsp; &rarr; brackets match',
        'Take out <span class="m">(x &minus; 1)</span>: &nbsp; <span class="m">= (x &minus; 1)(x&sup2; &minus; 4)</span>',
        '<b>Factorise FULLY</b> &mdash; <span class="m">x&sup2; &minus; 4</span> is a difference of squares!'])
 + eq('<span class="hl">= (x &minus; 1)(x &minus; 2)(x + 2)</span>'),
 "x squared, bracket x minus one, plus four, bracket one minus x. The brackets are backwards. So flip the second one. Four, bracket one minus x, becomes minus four, bracket x minus one. Now they match. Take out x minus one, and we get x minus one, times x squared minus four. But wait. Factorise fully. x squared minus four is a difference of squares. So the final answer is x minus one, x minus two, x plus two."),

(A, "Worked: &nbsp; x&sup2;(x + 4) + 9(&minus;4 &minus; x)",
 steps(['<span class="m">(&minus;4 &minus; x) = &minus;(4 + x) = &minus;(x + 4)</span>',
        '<span class="m">= x&sup2;(x + 4) &minus; 9(x + 4)</span>',
        '<span class="m">= (x + 4)(x&sup2; &minus; 9)</span> &nbsp; &rarr; still factorises!'])
 + eq('<span class="hl">= (x + 4)(x &minus; 3)(x + 3)</span>'),
 "Same idea here. x squared, bracket x plus four, plus nine, bracket minus four minus x. Minus four minus x equals minus, bracket x plus four. So we get x plus four, times x squared minus nine. And x squared minus nine factorises again. The final answer is x plus four, x minus three, x plus three."),

(A, "Rule 4c &mdash; Grouping four terms",
 eq('ax + 3a + bx + 3b')
 + steps(['<b>Pair them:</b> <span class="m">(ax + 3a) + (bx + 3b)</span>',
          '<b>Pair 1</b> take out <span class="m">a</span> &rarr; <span class="m">a(x + 3)</span>',
          '<b>Pair 2</b> take out <span class="m">b</span> &rarr; <span class="m">b(x + 3)</span>',
          'The brackets match &check; &nbsp; take out <span class="m">(x + 3)</span>'])
 + eq('<span class="hl">= (x + 3)(a + b)</span>'),
 "Rule four c. Four terms, so group them in pairs. a x plus three a plus b x plus three b. Pair them up. From the first pair take out a, giving a, bracket x plus three. From the second pair take out b, giving b, bracket x plus three. The brackets match, so take out x plus three. The answer is x plus three, times a plus b."),

(B, "Simplifying fractions &mdash; 3 steps",
 cards([("1", "Factorise the TOP", "numerator"),
        ("2", "Factorise the BOTTOM", "denominator"),
        ("3", "Cancel whole BRACKETS", "not single letters")])
 + note("GOLDEN RULE: you may only cancel FACTORS (things multiplied). You may NEVER cancel TERMS (things added or subtracted).", "warn"),
 "Now algebraic fractions. Three steps, never anything else. Factorise the top. Factorise the bottom. Then cancel whole brackets. And here is the golden rule. You may only cancel factors, things being multiplied. You may never cancel terms, things being added or subtracted."),

(B, "Worked: (i)(2)",
 eq('<span class="frac"><span class="num">x&sup3;y &minus; 4xy&sup2;</span><span>x&sup2;y&sup2;</span></span>')
 + steps(['<b>Top:</b> common factor <span class="m">xy</span> &rarr; <span class="m">xy(x&sup2; &minus; 4y)</span>',
          '<b>Bottom:</b> <span class="m">x&sup2;y&sup2;</span>', 'Cancel one <span class="m">x</span> and one <span class="m">y</span>'])
 + eq('<span class="hl"><span class="frac"><span class="num">x&sup2; &minus; 4y</span><span>xy</span></span></span>'),
 "x cubed y minus four x y squared, all over x squared y squared. The common factor on top is x y. That gives x y, bracket x squared minus four y. Now cancel one x and one y with the bottom. The answer is x squared minus four y, over x y. And do not cancel any further, because that is a subtraction."),

(B, "Worked: (i)(3)",
 eq('<span class="frac"><span class="num">x&sup2; &minus; 9</span><span>x&sup2; &minus; 3x</span></span>')
 + steps(['<b>Top:</b> difference of squares &rarr; <span class="m">(x &minus; 3)(x + 3)</span>',
          '<b>Bottom:</b> common factor <span class="m">x</span> &rarr; <span class="m">x(x &minus; 3)</span>',
          'Cancel <span class="m">(x &minus; 3)</span>'])
 + eq('<span class="hl"><span class="frac"><span class="num">x + 3</span><span>x</span></span></span>'),
 "x squared minus nine, over x squared minus three x. The top is a difference of squares, so x minus three, x plus three. The bottom has a common factor of x, giving x, bracket x minus three. Cancel x minus three. The answer is x plus three, over x."),

(B, "Worked: (i)(4) and (i)(5)",
 '<div class="split"><div>'
 + eq('<span class="frac"><span class="num">x&sup2; &minus; 14x + 24</span><span>x&sup2; &minus; 11x &minus; 12</span></span>')
 + steps(['Top &rarr; <span class="m">(x &minus; 2)(x &minus; 12)</span>', 'Bottom &rarr; <span class="m">(x &minus; 12)(x + 1)</span>'])
 + eq('<span class="hl"><span class="frac"><span class="num">x &minus; 2</span><span>x + 1</span></span></span>')
 + '</div><div>'
 + eq('<span class="frac"><span class="num">x&sup2; &minus; 14x</span><span>x&sup2; &minus; 16x + 28</span></span>')
 + steps(['Top &rarr; <span class="m">x(x &minus; 14)</span>', 'Bottom &rarr; <span class="m">(x &minus; 14)(x &minus; 2)</span>'])
 + eq('<span class="hl"><span class="frac"><span class="num">x</span><span>x &minus; 2</span></span></span>')
 + '</div></div>',
 "x squared minus fourteen x plus twenty four, over x squared minus eleven x minus twelve. The top factorises to x minus two, x minus twelve. The bottom factorises to x minus twelve, x plus one. Cancel x minus twelve. The answer is x minus two, over x plus one. And the last one. x squared minus fourteen x, over x squared minus sixteen x plus twenty eight. The top is x, bracket x minus fourteen. The bottom is x minus fourteen, x minus two. So the answer is x, over x minus two."),

(C, "The Theorem of Pythagoras",
 eq('a&sup2; + b&sup2; = c&sup2;', "big")
 + '<svg viewBox="0 0 420 200" class="dg"><polygon points="40,170 300,170 40,40" fill="#1c2b4a" stroke="#8fb4ff" stroke-width="3"/>'
 '<rect x="40" y="148" width="22" height="22" fill="none" stroke="#ffb454" stroke-width="3"/>'
 '<text x="165" y="195" fill="#cfe0ff" font-size="22">b</text><text x="14" y="110" fill="#cfe0ff" font-size="22">a</text>'
 '<text x="185" y="95" fill="#ffb454" font-size="22" font-weight="bold">c = hypotenuse</text></svg>'
 + note("c is the HYPOTENUSE &mdash; opposite the right angle, and always the LONGEST side.", "tip"),
 "Now chapter thirteen. The theorem of Pythagoras. In a right angled triangle, a squared plus b squared equals c squared, where c is the hypotenuse. The hypotenuse is the side opposite the right angle, and it is always the longest side."),

(C, "ADD or SUBTRACT? This decides your marks",
 cards([("+", "Looking for the HYPOTENUSE", "ADD the two squares, then &radic;"),
        ("&minus;", "Looking for a SHORTER side", "SUBTRACT, then &radic;")])
 + eq('c = &radic;(a&sup2; + b&sup2;) &nbsp;&nbsp;&nbsp;&nbsp; a = &radic;(c&sup2; &minus; b&sup2;)')
 + note("Before you calculate, ASK: is the side I want the longest side of that triangle? Yes &rarr; add. No &rarr; subtract.", "warn"),
 "This is the decision that decides your marks. If you are looking for the hypotenuse, you add the two squares and then square root. If you are looking for a shorter side, you subtract, then square root. So before you calculate, ask yourself: is the side I want the longest side? If yes, add. If no, subtract."),

(C, "Surd form vs decimals",
 steps(['<b>&ldquo;Surd form&rdquo; / &ldquo;wortelvorm&rdquo;</b> &rarr; keep the &radic; sign, do NOT round.',
        'Simplify by splitting off the biggest <b>perfect square</b>:',
        '<span class="m">&radic;98 = &radic;49 &times; &radic;2 = 7&radic;2</span> &nbsp;&nbsp; <span class="m">&radic;50 = 5&radic;2</span> &nbsp;&nbsp; <span class="m">&radic;12 = 2&radic;3</span>',
        '<b>&ldquo;Two decimal places&rdquo;</b> &rarr; use the calculator and round: <span class="m">&radic;87 &asymp; 9,33</span>'])
 + note("Triples worth knowing: 3-4-5 &nbsp; 5-12-13 &nbsp; 8-15-17 &nbsp; 7-24-25 &nbsp; 20-21-29 (and all their multiples)", "tip"),
 "Watch the wording carefully. Surd form, or wortelvorm, means keep the square root sign and do not round off. Simplify it by splitting off the biggest perfect square. Root ninety eight is root forty nine times root two, which is seven root two. But if it says correct to two decimal places, then you use the calculator and round."),

(C, "Exercise 13.1 (d)(1) &mdash; find x",
 '<svg viewBox="0 0 420 230" class="dg">'
 '<polygon points="50,200 250,200 110,45" fill="#1c2b4a" stroke="#8fb4ff" stroke-width="3"/>'
 '<line x1="50" y1="200" x2="200" y2="110" stroke="#ffb454" stroke-width="4"/>'
 '<line x1="110" y1="45" x2="200" y2="110" stroke="#8fb4ff" stroke-width="3"/>'
 '<line x1="200" y1="110" x2="250" y2="200" stroke="#8fb4ff" stroke-width="3"/>'
 '<rect x="228" y="178" width="22" height="22" fill="none" stroke="#ffb454" stroke-width="3"/>'
 '<text x="30" y="212" fill="#fff" font-size="20">A</text><text x="102" y="36" fill="#fff" font-size="20">D</text>'
 '<text x="206" y="104" fill="#fff" font-size="20">C</text><text x="256" y="212" fill="#fff" font-size="20">B</text>'
 '<text x="62" y="120" fill="#cfe0ff" font-size="20">16</text><text x="160" y="68" fill="#cfe0ff" font-size="20">y</text>'
 '<text x="118" y="165" fill="#ffb454" font-size="20">x</text><text x="238" y="150" fill="#cfe0ff" font-size="20">5</text>'
 '<text x="140" y="222" fill="#cfe0ff" font-size="20">12</text></svg>'
 + steps(['In <span class="m">&#9651;ABC</span>: right angle at B, so <b>AC is the hypotenuse</b> &rarr; <b>ADD</b>',
          '<span class="m">x&sup2; = 12&sup2; + 5&sup2; = 144 + 25 = 169</span>'])
 + eq('<span class="hl">x = &radic;169 = 13</span>'),
 "Exercise thirteen point one. Here we have two triangles sharing the side A C. Always solve the triangle where you already know two sides. In triangle A B C, the right angle is at B, A B is twelve and B C is five. A C is opposite the right angle, so A C is the hypotenuse. That means add. x squared equals twelve squared plus five squared, which is one hundred and forty four plus twenty five, equals one hundred and sixty nine. So x equals thirteen."),

(C, "Exercise 13.1 (d)(1) &mdash; now find y",
 steps(['In <span class="m">&#9651;ADC</span>: right angle at C, so <b>AD (16) is the hypotenuse</b>',
        '<span class="m">y</span> is a <b>shorter</b> side &rarr; <b>SUBTRACT</b>',
        '<span class="m">16&sup2; = y&sup2; + 13&sup2;</span>',
        '<span class="m">y&sup2; = 256 &minus; 169 = 87</span>'])
 + eq('<span class="hl">y = &radic;87 &asymp; 9,33</span>')
 + note("You could not find y first &mdash; triangle ADC only had one known side until x gave you the second.", "tip"),
 "Now triangle A D C. The right angle is at C, and A D, which is sixteen, is the hypotenuse. y is a shorter side, so this time we subtract. y squared equals sixteen squared minus thirteen squared, which is two hundred and fifty six minus one hundred and sixty nine, equals eighty seven. So y equals root eighty seven, which is nine comma three three, to two decimal places."),

(C, "The CONVERSE of Pythagoras",
 '<div class="hero">Used to PROVE a triangle is right-angled</div>'
 + eq('If &nbsp; c&sup2; = a&sup2; + b&sup2; &nbsp; then the triangle is right-angled', "big")
 + steps(['Find the <b>longest side</b>',
          'LHS = (longest side)&sup2;',
          'RHS = (short)&sup2; + (other short)&sup2;',
          'If LHS = RHS &rarr; <b>&there4; right-angled</b>, and the 90&deg; is <b>opposite the longest side</b>']),
 "The converse of Pythagoras. This is what you use to prove a triangle is right angled. If the square on the longest side equals the sum of the squares on the other two sides, then the triangle is right angled, and the right angle is opposite the longest side."),

(C, "13.2 (a)(1) &nbsp; AB=20, BC=48, AC=52",
 steps(['Longest side is <b>AC = 52</b>',
        '<b>LHS:</b> <span class="m">52&sup2; = 2704</span>',
        '<b>RHS:</b> <span class="m">20&sup2; + 48&sup2; = 400 + 2304 = 2704</span>',
        '<span class="m">&there4; AC&sup2; = AB&sup2; + BC&sup2;</span>'])
 + eq('<span class="hl">&there4; &#9651;ABC is right-angled, 90&deg; at B</span>')
 + note("B is the vertex OPPOSITE the longest side AC. (This is 5-12-13 &times; 4.)", "tip"),
 "Triangle A B C, with A B twenty, B C forty eight, and A C fifty two. The longest side is A C. Left hand side, fifty two squared is two thousand seven hundred and four. Right hand side, twenty squared plus forty eight squared is four hundred plus two thousand three hundred and four, which is also two thousand seven hundred and four. They are equal, so the triangle is right angled, and the right angle is at B, because B is opposite A C."),

(C, "13.2 (a)(2) &nbsp; c=17, b=8, a=15",
 note("A small letter names the side OPPOSITE the matching capital: a is opposite A, b opposite B, c opposite C.", "tip")
 + steps(['Longest side is <b>c = 17</b>',
          '<b>LHS:</b> <span class="m">17&sup2; = 289</span>',
          '<b>RHS:</b> <span class="m">15&sup2; + 8&sup2; = 225 + 64 = 289</span>'])
 + eq('<span class="hl">&there4; right-angled, 90&deg; at C</span>'),
 "Next one. c is seventeen, b is eight, and a is fifteen. Remember, a small letter names the side opposite the matching capital letter. The longest side is c, seventeen. Seventeen squared is two hundred and eighty nine. Fifteen squared plus eight squared is two hundred and twenty five plus sixty four, which is also two hundred and eighty nine. So it is right angled, and the right angle is at C."),

(C, "Acute or obtuse? The test",
 '<table class="sg"><tr><th>Compare</th><th>The triangle is&hellip;</th><th>Special angle</th></tr>'
 '<tr><td><span class="m">c&sup2; = a&sup2; + b&sup2;</span></td><td><b>Right-angled</b></td><td>90&deg; opposite longest side</td></tr>'
 '<tr><td><span class="m">c&sup2; &lt; a&sup2; + b&sup2;</span></td><td><b>Acute-angled</b> (skerphoekig)</td><td>all angles &lt; 90&deg;</td></tr>'
 '<tr><td><span class="m">c&sup2; &gt; a&sup2; + b&sup2;</span></td><td><b>Obtuse-angled</b> (stomphoekig)</td><td>obtuse angle opposite longest side</td></tr></table>'
 + note("Remember it: the BIGGER the longest side, the more the angle opposite it is stretched OPEN &rarr; obtuse.", "tip"),
 "Now, acute or obtuse. Compare the longest side squared with the sum of the other two squares. If it is equal, the triangle is right angled. If it is less than, the triangle is acute angled. If it is greater than, the triangle is obtuse angled, and the obtuse angle is opposite the longest side. Think of it this way. The bigger the longest side, the more the angle opposite it is stretched open."),

(C, "13.2 (b)(1) &nbsp; AB=24, BC=14, AC=27",
 steps(['Longest side is <b>AC = 27</b>',
        '<span class="m">27&sup2; = 729</span>',
        '<span class="m">24&sup2; + 14&sup2; = 576 + 196 = 772</span>',
        '<span class="m">729 &lt; 772</span> &nbsp; so &nbsp; <span class="m">AC&sup2; &lt; AB&sup2; + BC&sup2;</span>'])
 + eq('<span class="hl">&there4; &#9651;ABC is acute-angled</span>'),
 "Triangle A B C, with A B twenty four, B C fourteen, and A C twenty seven. The longest side is twenty seven. Twenty seven squared is seven hundred and twenty nine. Twenty four squared plus fourteen squared is five hundred and seventy six plus one hundred and ninety six, which is seven hundred and seventy two. Seven hundred and twenty nine is less than seven hundred and seventy two, so the triangle is acute angled."),

(C, "13.2 (b)(2) &nbsp; d=8, e=18, f=13",
 steps(['Longest side is <b>e = 18</b>, and side <span class="m">e</span> is opposite <b>E</b>',
        '<span class="m">18&sup2; = 324</span>',
        '<span class="m">8&sup2; + 13&sup2; = 64 + 169 = 233</span>',
        '<span class="m">324 &gt; 233</span>'])
 + eq('<span class="hl">&there4; obtuse-angled; the obtuse angle is &Ecirc;</span>'),
 "Triangle D E F, with d eight, e eighteen, and f thirteen. The longest side is e, eighteen. Eighteen squared is three hundred and twenty four. Eight squared plus thirteen squared is sixty four plus one hundred and sixty nine, which is two hundred and thirty three. Three hundred and twenty four is greater than two hundred and thirty three, so the triangle is obtuse angled, and the obtuse angle is E, because side e is the longest."),

(C, "Exam Focus p239 (b) &mdash; diagonal of a square",
 '<svg viewBox="0 0 420 200" class="dg"><rect x="120" y="30" width="140" height="140" fill="#1c2b4a" stroke="#8fb4ff" stroke-width="3"/>'
 '<line x1="120" y1="30" x2="260" y2="170" stroke="#ffb454" stroke-width="4"/>'
 '<text x="104" y="26" fill="#fff" font-size="20">A</text><text x="264" y="26" fill="#fff" font-size="20">D</text>'
 '<text x="264" y="188" fill="#fff" font-size="20">C</text><text x="104" y="188" fill="#fff" font-size="20">B</text>'
 '<text x="70" y="105" fill="#cfe0ff" font-size="20">7 cm</text></svg>'
 + steps(['A diagonal always makes a <b>right-angled triangle</b>. All sides of a square are equal.',
          'BD is the hypotenuse &rarr; <b>ADD</b>',
          '<span class="m">BD&sup2; = 7&sup2; + 7&sup2; = 49 + 49 = 98</span>',
          '<span class="m">BD = &radic;98 = &radic;49 &times; &radic;2</span>'])
 + eq('<span class="hl">BD = 7&radic;2 cm</span>'),
 "Exam focus, page two three nine. A B C D is a square with a side of seven centimetres. Find B D in surd form. A diagonal always creates a right angled triangle, and all the sides of a square are equal, so both short sides are seven. B D is the hypotenuse, so we add. Seven squared plus seven squared is forty nine plus forty nine, which is ninety eight. So B D is root ninety eight, which simplifies to seven root two centimetres. Leave it exactly like that. Do not write nine point nine."),

(C, "Exam Focus p239 (c) &mdash; diagonals of a rectangle",
 '<svg viewBox="0 0 420 200" class="dg"><rect x="90" y="35" width="200" height="130" fill="#1c2b4a" stroke="#8fb4ff" stroke-width="3"/>'
 '<line x1="90" y1="35" x2="290" y2="165" stroke="#ffb454" stroke-width="3"/><line x1="290" y1="35" x2="90" y2="165" stroke="#ffb454" stroke-width="3"/>'
 '<circle cx="190" cy="100" r="5" fill="#ffb454"/><text x="196" y="94" fill="#ffb454" font-size="20">E</text>'
 '<text x="74" y="30" fill="#fff" font-size="20">A</text><text x="294" y="30" fill="#fff" font-size="20">D</text>'
 '<text x="294" y="184" fill="#fff" font-size="20">C</text><text x="74" y="184" fill="#fff" font-size="20">B</text>'
 '<text x="175" y="26" fill="#cfe0ff" font-size="20">84</text><text x="58" y="105" fill="#cfe0ff" font-size="20">80</text></svg>'
 + steps(['<span class="m">BC = AD = 84</span> (opposite sides of a rectangle are equal)',
          'AC is the hypotenuse of <span class="m">&#9651;ABC</span> &rarr; <b>ADD</b>',
          '<span class="m">AC&sup2; = 80&sup2; + 84&sup2; = 6400 + 7056 = 13456</span>',
          '<span class="m">AC = &radic;13456 = 116</span>',
          '<b>Diagonals of a rectangle bisect each other</b> &rarr; <span class="m">AE = &frac12; AC</span>'])
 + eq('<span class="hl">AE = 58</span>'),
 "And the last one. A B C D is a rectangle, A D is eighty four, and A B is eighty. Find A E, where E is the point where the diagonals cross. First find the whole diagonal. In triangle A B C, B C equals A D, which is eighty four, and A B is eighty. A C is the hypotenuse, so add. Eighty squared plus eighty four squared is six thousand four hundred plus seven thousand and fifty six, which is thirteen thousand four hundred and fifty six. The square root of that is one hundred and sixteen. Now, the diagonals of a rectangle bisect each other, so A E is half of one hundred and sixteen, which is fifty eight. And notice, the question asked for A E, not A C. Always read the question."),

("Exam Tips", "The mistakes that cost the most marks",
 steps(['Not taking out the <b>common factor first</b>',
        'Stopping before it is <b>fully</b> factorised',
        'Trying to factorise a <b>sum</b> of squares',
        '<b>Sign errors</b> in trinomials &mdash; always FOIL back to check',
        'Cancelling <b>terms</b> instead of <b>factors</b> in a fraction',
        '<b>Adding</b> in Pythagoras when you should <b>subtract</b>',
        'Forgetting the final <b>square root</b>',
        'Answering the <b>wrong quantity</b> (AC instead of AE)']),
 "Before you go, here are the mistakes that cost the most marks. Not taking out the common factor first. Stopping before it is fully factorised. Trying to factorise a sum of squares. Sign errors in trinomials. Cancelling terms instead of factors. Adding in Pythagoras when you should subtract. Forgetting the final square root. And answering the wrong quantity."),

("You're ready", "Say these out loud one more time",
 cards([("8", "Factorising", "Common factor &rarr; 2 terms: diff. of squares &rarr; 3 terms: trinomial &rarr; 4 terms: group in pairs. Then check every bracket AGAIN."),
        ("13", "Pythagoras", "a&sup2; + b&sup2; = c&sup2;. Hypotenuse &rarr; ADD. Shorter side &rarr; SUBTRACT. Then &radic;.")])
 + note("Show every step &mdash; method marks are real marks. Good luck tomorrow!", "tip"),
 "That is everything. Say the four checks out loud one more time. Common factor. Two terms, difference of squares. Three terms, trinomial. Four terms, group in pairs. And for Pythagoras. Hypotenuse, add. Shorter side, subtract. Then square root. Show every step, because method marks are real marks. You have got this. Good luck tomorrow."),
]
