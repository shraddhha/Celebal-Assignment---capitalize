# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    s = ''
    for i in l:
        s = s+ i.capitalize()+' '
        
    return s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
