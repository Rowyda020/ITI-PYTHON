def long_substr(string):
    curr_string = ''
    longest_string = ''
    for i in (string):
        if curr_string == '' or i > curr_string[::-1]:
            curr_string+=i
        else:
            curr_string = i
        longest_string = max(curr_string,longest_string, key=len)
    return longest_string
string = input()
print(long_substr(string))