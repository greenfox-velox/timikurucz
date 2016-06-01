# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_counter(file_name):
    try:
        output = 0
        f = open(file_name)
        text_list = f.readlines()
        f.close()
        for i in range(len(text_list)):
            output += 1
        return output
    except FileNotFoundError:
        return 0


print(line_counter('C:/Users/timi.kurucz/Greenfox/timikurucz/week-04/day-1/1-pip-io-modules/01_io/test.txt'))
print(line_counter('C:/Users/timi.kurucz/Greenfox/timikurucz/week-04/day-1/1-pip-io-modules/01_io/uj.txt'))
