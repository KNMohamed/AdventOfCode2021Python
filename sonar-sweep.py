from argumentparsing import parseArguments

def increasingDepthCount(input):
  count = 0
  with open(input, 'r') as file:
    line = file.readline()
    before = after = int(line)
    while line:
      after = int(line)
      if after > before:
        count += 1
      before = after
      line = file.readline()
  return count

def slidingWindowIncreasingDepthCount(input, windowSize):
  count = 0
  with open(input, 'r') as file:
    lines = file.readlines()
    if(windowSize > len(lines)):
      print('nuber of lines must be greater than window size')
      return 0
    before = after = sum([int(x) for x in lines[:windowSize]])
    for idx, line in enumerate(lines[windowSize:]):
      after = after - int(lines[idx]) + int(line)
      if(after > before):
        count += 1
      before = after
    return count

def main():
  args = parseArguments()
  count = 0
  if(args.part == 1):
    count = increasingDepthCount(args.input)
  if(args.part == 2):
    count = slidingWindowIncreasingDepthCount(args.input, 3)
  print('The count is {count}'.format(count=count))


if __name__ == "__main__":
  main()