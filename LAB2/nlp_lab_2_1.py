

import string
from automathon import DFA
from graphviz import Digraph

input_symbols = set(string.ascii_lowercase + "_")

excluded = set(string.printable) - input_symbols

def is_safe_for_graphviz(c):
    return c not in {'"', '\\', '\n', '\t', '\r', '\x0b', '\x0c'}

excluded = {c for c in excluded if is_safe_for_graphviz(c)}

symbols = input_symbols.union(excluded)



q0_q1_dict={}
for char in input_symbols:
  q0_q1_dict.update({char:'q1'})
print(q0_q1_dict)

q0_dead_dict={}
for char in excluded:
  q0_dead_dict.update({char:'q2'})

q0_dict=q0_q1_dict.copy()
q0_dict.update(q0_dead_dict)

q1_dead_dict={}
for char in excluded:
  q1_dead_dict.update({char:'q2'})

q1_q1_dict={}
for char in input_symbols:
  q1_q1_dict.update({char:'q1'})

q1_dict=q1_q1_dict.copy()
q1_dict.update(q1_dead_dict)

q2_dead_dict={}
for char in excluded:
  q2_dead_dict.update({char:'q2'})

print(q1_dict)


q = {'q0', 'q1', 'q2'}
sigma = symbols
delta = { 'q0' : q0_dict,
          'q1' : q1_dict,
          'q2' : q2_dead_dict
        }
initial_state = 'q0'
f = {'q0','q1'}

automata = DFA(q, sigma, delta, initial_state, f)

automata.is_valid()

result=[]
with open('brown_nouns.txt','r') as f:
  for word in f:
    word = word.strip()
    if(automata.accept(word)):
      result.append("Accepted")
    else:
      result.append("Not Accepted")

with open('results.txt','w+') as f:
  for res in result:
    f.write(res + '\n')






q0_q1 = sorted(input_symbols)
q0_q2 = sorted(excluded)

q1_q1 = q0_q1
q1_q2 = q0_q2

q2_q2 = q0_q2
dot = Digraph(name="DFA", format='png')
dot.attr(rankdir='LR', size='10,5', fontsize='20')


dot.attr('node', shape='circle')
dot.node('q0')
dot.node('q1', shape='doublecircle')
dot.node('q2')


dot.node('', shape='plaintext', label='')
dot.edge('', 'q0')


def fmt(symbols):
    return ', '.join(sorted(symbols))


dot.edge('q0', 'q1', label=fmt(q0_q1))
dot.edge('q0', 'q2', label=fmt(q0_q2))

dot.edge('q1', 'q1', label=fmt(q1_q1))
dot.edge('q1', 'q2', label=fmt(q1_q2))

dot.edge('q2', 'q2', label=fmt(q2_q2))


dot.render('clean_dfa', view=True)

