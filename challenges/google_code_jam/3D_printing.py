import sys


def solve():
    case_txt = "Case #"
    threshold = pow(10,6)
    line_counter = 0
    min_c1, min_c2, min_c3, min_c4 = float('inf'), float('inf'), float('inf'), float('inf')

    for i, line in enumerate(sys.stdin):
        # skip first line (number of test cases)
        if i != 0:
            line_counter += 1
            c1, c2, c3, c4 = map(int, line.split())
            min_c1, min_c2, min_c3, min_c4 = min(c1, min_c1), min(c2, min_c2), min(c3, min_c3), min(c4, min_c4)

            if line_counter == 3:
                color_sum = min_c1 + min_c2 + min_c3 + min_c4
                if color_sum < threshold:
                    print(case_txt + str(i//3) + ":" + " IMPOSSIBLE")
                else:
                    colors = [min_c1, min_c2, min_c3, min_c4]
                    ink_used = 0
                    output = ""
                    for c in colors:
                        if ink_used >= threshold:
                            output += " 0"
                        elif c >= threshold-ink_used:
                            output += " " + str(threshold-ink_used)
                            ink_used += c
                        else:
                            output += " " + str(c)
                            ink_used += c
                    print(case_txt + str(i//3) + ":" + output)
                min_c1, min_c2, min_c3, min_c4 = float('inf'), float('inf'), float('inf'), float('inf')
                line_counter = 0






if __name__ == '__main__':
    solve()
