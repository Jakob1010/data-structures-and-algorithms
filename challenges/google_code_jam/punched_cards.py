import sys


def solve():
    case_txt = "Case #"
    output = ""
    cell_top_single = "+-"
    cell_border_single = "|."

    for i, line in enumerate(sys.stdin):
        # skip first line (number of test cases)
        if i != 0:
            r, c = line.split()
            # print test case number
            output += case_txt+str(i)+":\n"

            # construct first row
            cell_top = ""
            cell_border = ""
            for column in range(int(c)):
                cell_top += cell_top_single
                cell_border += cell_border_single
            cell_top += "+\n"
            cell_border += "|\n"

            # print cells row by row
            for row in range(int(r)):
                if row == 0:
                    output += ".." + cell_top[2:]
                    output += ".." + cell_border[2:]
                else:
                    output += cell_top
                    output += cell_border
            output += cell_top

    #output_file = open("res/punched_cards"+"/output.txt","w")
    #output_file.write(output)
    #output_file.close()
    print(output)


if __name__ == '__main__':
    solve()
