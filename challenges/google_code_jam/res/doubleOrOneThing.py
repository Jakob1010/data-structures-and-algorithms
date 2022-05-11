import sys


def solve():

    for i, line in enumerate(sys.stdin):
        # skip first line (number of test cases)
        if i != 0:
            word = line
            word_processed = ""
            l, r = 0, 1
            while word[l].isalpha() and l < len(word)-1:
                if r >= len(word):
                    word_processed += word[l]
                elif word[l] == word[r]:
                    r+=1
                    continue
                elif word[l] < word[r]:
                    word_processed += word[l] + word[l]
                else:
                    word_processed += word[l]

                if r-l == 1:
                    r+=1
                l+=1

            print('Case #' + str(i) + ': ' + word_processed)



if __name__ == '__main__':
    solve()