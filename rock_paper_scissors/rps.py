#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  output = []
  possible_moves = ['scissors', 'paper', 'rock']

  stack = []
  stack.append([])

  while len(stack) > 0:
    hand = stack.pop()

    if n == 0 or len(hand) == n:
      output.append(hand)
    else:
      for play in possible_moves:
        stack.append(hand + [play])

  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')