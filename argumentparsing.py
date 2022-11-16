import argparse

def parseArguments():
  parser = argparse.ArgumentParser(
  prog = 'Sonar sweep program',
  description = 'This program calculates increasing depth count, given an input file of depths')
  parser.add_argument('-i', '--input', required=True) # input filename
  parser.add_argument('-p','--part',  type=int, choices=range(1, 3), default=2)
  args = parser.parse_args()
  return args