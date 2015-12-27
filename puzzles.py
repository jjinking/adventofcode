def d1_p1():
    floor = 0
    for c in open('in1.txt', 'rU').read().strip():
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            print('Error character: {}'.format(c))
    return floor


def d1_p2():
    floor = 0
    for i,c in enumerate(open('in1.txt', 'rU').read().strip()):
        floor += (1 if c == '(' else -1)
        if floor == -1:
            print(i + 1)
            break


def d2():
    total_wp = 0
    total_ribbon = 0
    with open('in2.txt', 'rU') as f:
        for line in f:
            l, w, h = line.strip().split('x')
            l, w, h = int(l), int(w), int(h)
            total_wp += 2*l*w + 2*w*h + 2*h*l + min(l * w, l * h, w * h)
            min_perimeter = min(2 * (l + w), 2 * (l + h), 2 * (w + h))
            total_ribbon += l * w * h + min_perimeter
    return total_wp, total_ribbon


def d3_p1():
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    with open('in3.txt', 'rU') as f:
        while True:
            d = f.read(1)
            if not d:
                break
            elif d == '^':
                x, y = (x, y - 1)
            elif d == '>':
                x, y = (x + 1, y)
            elif d == '<':
                x, y = (x - 1, y)
            elif d == 'v':
                x, y = (x, y + 1)
            visited.add((x, y))
    return len(visited)


def d3_p2():
    santa = {0: {'x': 0, 'y': 0}, 1: {'x': 0, 'y': 0}}
    visited = set()
    visited.add((0, 0))
    with open('in3.txt', 'rU') as f:
        robo_turn = False
        while True:
            x, y = santa[robo_turn]['x'], santa[robo_turn]['y']
            d = f.read(1)
            if not d:
                break
            elif d == '^':
                x, y = (x, y - 1)
            elif d == '>':
                x, y = (x + 1, y)
            elif d == '<':
                x, y = (x - 1, y)
            elif d == 'v':
                x, y = (x, y + 1)
            visited.add((x, y))
            santa[robo_turn]['x'], santa[robo_turn]['y'] = x, y
            robo_turn = not robo_turn
    return len(visited)


def d4_p1():
    import hashlib
    input = "iwrupvqb"
    n = 0
    while hashlib.new('md5',
                      (input + str(n)).encode()).hexdigest()[:5] != '00000':
        n += 1
    return n


def d4_p2():
    import hashlib
    input = "iwrupvqb"
    n = 0
    while hashlib.new('md5',
                      (input + str(n)).encode()).hexdigest()[:6] != '000000':
        n += 1
    return n

def d5_p1():
    n_nice = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    bad = {'ab', 'cd', 'pq', 'xy'}
    with open('in5.txt', 'rU') as f:
        for line in f:
            s = line.strip()
            n_vowels = 0
            twin_letter = False
            contains_bad = False
            for i, c in enumerate(s):
                if c in vowels:
                    n_vowels += 1
                if i > 0:
                    prev_c = s[i-1]
                    if prev_c == c:
                        twin_letter = True
                    if prev_c + c in bad:
                        contains_bad = True
                        break
            if not contains_bad and twin_letter and n_vowels > 2:
                n_nice += 1
    return n_nice


def d5_p2():
    n_nice = 0
    with open('in5.txt', 'rU') as f:
        for line in f:
            s = line.strip()
            len_s = len(s)
            double_pairs = False
            letter_repeats = False
            for i, c in enumerate(s):
                two = s[i:i+2]
                for j in range(i + 2, len(s) - 1):
                    if s[j:j+2] == two:
                        double_pairs = True
                if i < len_s - 2 and c == s[i + 2]:
                    letter_repeats = True
            if double_pairs and letter_repeats:
                n_nice += 1
    return n_nice


def d6_p1():
    from collections import defaultdict
    lights = defaultdict(bool)
    with open('in6.txt', 'rU') as f:
        for line in f:
            instr = line.strip().split()
            if instr[0] == 'turn':
                x_i, y_i = map(int, instr[2].split(','))
                x_f, y_f = map(int, instr[4].split(','))
                if instr[1] == 'off':
                    set_val = False
                else:
                    set_val = True
                for x in range(x_i, x_f + 1):
                    for y in range(y_i, y_f + 1):
                        lights[x, y] = set_val
            elif instr[0] == 'toggle':
                x_i, y_i = map(int, instr[1].split(','))
                x_f, y_f = map(int, instr[3].split(','))
                for x in range(x_i, x_f + 1):
                    for y in range(y_i, y_f + 1):
                        lights[x, y] = not lights[x, y]
            else:
                print("Instruction error {}".format(instr))
    total_lit = 0
    for x in range(1000):
        for y in range(1000):
            total_lit += lights[x, y]
    return total_lit


def d6_p2():
    from collections import defaultdict
    lights = defaultdict(int)
    with open('in6.txt', 'rU') as f:
        for line in f:
            instr = line.strip().split()
            if instr[0] == 'turn':
                x_i, y_i = map(int, instr[2].split(','))
                x_f, y_f = map(int, instr[4].split(','))
                for x in range(x_i, x_f + 1):
                    for y in range(y_i, y_f + 1):
                        if instr[1] == 'off':
                            lights[x, y] = max(lights[x, y] - 1, 0)
                        else:
                            lights[x, y] += 1
            elif instr[0] == 'toggle':
                x_i, y_i = map(int, instr[1].split(','))
                x_f, y_f = map(int, instr[3].split(','))
                for x in range(x_i, x_f + 1):
                    for y in range(y_i, y_f + 1):
                        lights[x, y] += 2
            else:
                print("Instruction error {}".format(instr))
    total_lit = 0
    for x in range(1000):
        for y in range(1000):
            total_lit += lights[x, y]
    return total_lit


def d7_p1():
    instructions = [instr.strip().split()
                    for instr in open('in7.txt', 'rU').readlines()]
    n_instructions = len(instructions)
    ns = {}
    executed = [False for _ in instructions]
    while sum(executed) < n_instructions:
        for i, instr in enumerate(instructions):
            if executed[i]:
                continue
            if instr[0] == 'NOT' and instr[1] in ns:
                ns[instr[3]] = (~ns[instr[1]]) & 65535
            elif instr[1] == 'OR':
                if instr[2] in ns:
                    try:
                        ns[instr[4]] = int(instr[0]) | ns[instr[2]]
                    except ValueError:
                        if instr[0] in ns:
                            ns[instr[4]] = ns[instr[0]] | ns[instr[2]]
                        else:
                            continue
                else:
                    continue
            elif instr[1] == 'AND':
                if instr[2] in ns:
                    try:
                        ns[instr[4]] = int(instr[0]) & ns[instr[2]]
                    except ValueError:
                        if instr[0] in ns:
                            ns[instr[4]] = ns[instr[0]] & ns[instr[2]]
                        else:
                            continue
                else:
                    continue
            elif instr[1] == 'RSHIFT' and instr[0] in ns:
                ns[instr[4]] = (ns[instr[0]] >> int(instr[2])) & 65535
            elif instr[1] == 'LSHIFT' and instr[0] in ns:
                ns[instr[4]] = (ns[instr[0]] << int(instr[2])) & 65535
            elif len(instr) == 3:
                try:
                    ns[instr[2]] = int(instr[0])
                except ValueError:
                    if instr[0] in ns:
                        ns[instr[2]] = ns[instr[0]]
                    else:
                        continue
            else:
                continue
            executed[i] = True
    return ns['a']


def d7_p2():
    instructions = [instr.strip().split()
                    for instr in open('in7.txt', 'rU').readlines()]
    n_instructions = len(instructions)
    ns = {'b': 3176}
    executed = [False for _ in instructions]
    while sum(executed) < n_instructions:
        for i, instr in enumerate(instructions):
            if executed[i]:
                continue
            if instr[0] == 'NOT' and instr[1] in ns:
                ns[instr[3]] = (~ns[instr[1]]) & 65535
            elif instr[1] == 'OR':
                if instr[2] in ns:
                    try:
                        ns[instr[4]] = int(instr[0]) | ns[instr[2]]
                    except ValueError:
                        if instr[0] in ns:
                            ns[instr[4]] = ns[instr[0]] | ns[instr[2]]
                        else:
                            continue
                else:
                    continue
            elif instr[1] == 'AND':
                if instr[2] in ns:
                    try:
                        ns[instr[4]] = int(instr[0]) & ns[instr[2]]
                    except ValueError:
                        if instr[0] in ns:
                            ns[instr[4]] = ns[instr[0]] & ns[instr[2]]
                        else:
                            continue
                else:
                    continue
            elif instr[1] == 'RSHIFT' and instr[0] in ns:
                ns[instr[4]] = (ns[instr[0]] >> int(instr[2])) & 65535
            elif instr[1] == 'LSHIFT' and instr[0] in ns:
                ns[instr[4]] = (ns[instr[0]] << int(instr[2])) & 65535
            elif len(instr) == 3:
                if instr[2] == 'b':
                    executed[i] = True
                    continue
                try:
                    ns[instr[2]] = int(instr[0])
                except ValueError:
                    if instr[0] in ns:
                        ns[instr[2]] = ns[instr[0]]
                    else:
                        continue
            else:
                continue
            executed[i] = True
    return ns['a']


def d8_p1():
    import string
    hexdigits = set(string.hexdigits)
    total = 0
    with open('in8.txt', 'rU') as f:
        for line in f:
            line = line.strip()
            n_line = len(line)
            n_line_minus_1 = n_line - 1
            n_line_minus_3 = n_line - 3
            n_strdata = 0
            i = 0
            while i < n_line:
                if i < n_line_minus_1 and line[i] == '\\':
                    if line[i+1] in {'\\', '\"'}:
                        i += 1
                    elif i < n_line_minus_3 and line[i+1] == 'x':
                        if line[i+2] in hexdigits and line[i+3] in hexdigits:
                            i += 3
                n_strdata += 1
                i += 1
            if line[0] == '\"':
                n_strdata -= 1
            if line[-1] == '\"':
                n_strdata -= 1
            total += (n_line - n_strdata)
    return total


def d8_p2():
    total = 0
    expand_chars = {'\\', '\"'}
    with open('in8.txt', 'rU') as f:
        for line in f:
            line = line.strip()
            front_end = {0, len(line) - 1}
            total += 4
            for i, c in enumerate(line):
                if i not in front_end and c in expand_chars:
                    total += 1
    return total


def d8(shortest=True):
    import itertools
    from collections import defaultdict
    dist = defaultdict(dict)
    with open('in9.txt', 'rU') as f:
        for line in f:
            row = line.strip().split()
            d = int(row[4])
            dist[row[0]][row[2]] = d
            dist[row[2]][row[0]] = d

    optimal_dist = None
    for cities in itertools.permutations(dist.keys()):
        order_total_dist = 0
        for i, city in enumerate(cities[:-1]):
            order_total_dist += dist[city][cities[i+1]]
        if shortest:
            if optimal_dist is None or order_total_dist < optimal_dist:
                optimal_dist = order_total_dist
        else:
            if optimal_dist is None or order_total_dist > optimal_dist:
                optimal_dist = order_total_dist
    return optimal_dist


def d23(a=0, b=0):
    register = {'a': a, 'b': b}
    instructions = tuple([tuple(line.strip().split())
                          for line in open('in23.txt', 'rU')])
    pc = 0
    while pc < len(instructions) and pc >= 0:
        instr = instructions[pc]
        if instr[0] == 'hlf':
            register[instr[1]] >>= 1
        elif instr[0] == 'tpl':
            register[instr[1]] *= 3
        elif instr[0] == 'inc':
            register[instr[1]] += 1
        elif instr[0] == 'jmp':
            pc += int(instr[1])
            continue
        elif instr[0] == 'jie' and register[instr[1][0]] % 2 == 0:
            pc += int(instr[2])
            continue
        elif instr[0] == 'jio' and register[instr[1][0]] == 1:
            pc += int(instr[2])
            continue
        pc += 1
    return register['b']
