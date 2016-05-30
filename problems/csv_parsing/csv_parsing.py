#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_csv(string):
    """
    Iterate over the string and store the characters 1 by 1

    Runtime:
        Time  -> O(n): Iterate the string 1 time
        Space -> O(n): Create the list of size n

    """
    result = []
    tmp = []
    opened_quote = False
    for ch in string:
        # Edge case for quotes
        if ch == '"':
            if opened_quote is False:
                opened_quote = True
            else:
                # Found matching quote
                opened_quote = False
        elif ch == ',' and opened_quote is False:
            # skip this char and append to list now
            result.append(''.join(tmp))
            tmp = []
            continue

        tmp.append(ch)
    # append the last value
    result.append(''.join(tmp))
    return result



if __name__ == "__main__":
    print parse_csv('2,6,3,2,5') # [ 2, 6, 3, 2, 5 ]
    print parse_csv('"pears","apples","walnuts","grapes","cheese,cake"') # [ "pears", "apples", "walnuts", "grapes", "cheese,cake" ]
    print parse_csv('1,"Que?","Kay?",2,"Si.","Sea? Kay, sea?","No, no, no. Que... ‘what’.",234,"Kay Watt?","Si, que ‘what’.","C.K. Watt?",3,"Yes!","comma,comma, comma , :)"') # [ 1, "Que?", "Kay?", 2, "Si.", "Sea? Kay, sea?", "No, no, no. Que... ‘what’." 234, "Kay Watt?", "Si, que ‘what’.", "C.K. Watt?", 3, "Yes!", "comma,comma, comma , :)" ]

