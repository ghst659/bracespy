class BraceParser:
    def __init__(self):
        pass
    def parse(self, pattern):
        "Parses PATTERN into a top-level BPSeq"
        result = list()
        if len(pattern) > 0:
            stack = Stack()
            cur_seq = result
            cur_alt = None
            for ch in pattern:
                if ch == "{":
                    stack.push((cur_seq, cur_alt))
                    cur_alt = BPAlt()
                    cur_seq.append(cur_alt)
                    cur_seq = list()
                    cur_alt.choice.append(cur_seq)
                elif ch == "}":
                    if stack.size() > 0:
                        cur_seq, cur_alt = stack.pop()
                    else:
                        raise Exception("invalid close-brace")
                elif ch == ",":
                    if cur_alt is None:
                        self.append_char(cur_seq, ch)
                    else:
                        cur_seq = list()
                        cur_alt.choice.append(cur_seq)
                else:
                    self.append_char(cur_seq, ch)
        return result

    def append_char(self, cur_seq, ch):
        if len(cur_seq) == 0:
            cur_seq.append(ch)
        elif isinstance(cur_seq[-1], str):
            cur_seq[-1] = cur_seq[-1] + ch
        else:
            cur_seq.append(ch)

    def iter_variations_list(self, seq_elem):
        "Returns list of variations of seq_elem"
        result = []
        if isinstance(seq_elem, BPAlt):
            for choice in seq_elem.choice:
                result.extend(self.expand_util(choice, ""))
        else:
            result.append(seq_elem)
        return result

    def iter_variations(self, seq_elem):
        "Yields variations of seq_elem"
        if isinstance(seq_elem, BPAlt):
            for choice in seq_elem.choice:
                yield from self.expand_util(choice, "")
        else:
            yield seq_elem

    def expand_util(self, seq, accum):
        result = []
        if len(seq) == 0:
            result.append(accum)
        else:
            for variation in self.iter_variations(seq[0]):
                next_accum = accum + variation
                result.extend(self.expand_util(seq[1:], next_accum))
        return result

    def expand(self, pattern):
        "Expands PATTERN string into set of strings"
        root_seq = self.parse(pattern)
        result = self.expand_util(root_seq, "")
        return result

class Stack:
    def __init__(self):
        self.stk = list()
    def push(self, item):
        self.stk.append(item)
    def pop(self):
        return self.stk.pop()
    def size(self):
        return len(self.stk)

class BPAlt:
    "Class representing a choice of elements"
    def __init__(self):
        self.choice = []
##############################################################################
# Local Variables:
# mode: python
# End:
