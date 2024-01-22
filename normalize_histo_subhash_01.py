"""
Author : Subhash Medipalli
File Name : normalize_histo_subhash_01.py
Purpose : Analyzing text using histogram technique and normalize the count using a constant value.
Revisions :
    00 : Importing string library and defining function for normalizing the repetitive characters by scaling them.
    01 : Announce, prompt, get user response and using necessary for and if loops to analyze
         the characters and inserting to list.
    02 : Calling plot_bars() with the parameters.

"""
### Step 1 : Importing string library and defining function for normalizing the repetition characters by scaling them.

# Importing string library
import string


def plot_bars(lis_num, ev_char, bar_length=20):
    """
    Description : plot_bars function is used to normalize the count according the peak value and to produce histogram
    plot.
    :param lis_num: character counts stored in a list
    :param ev_char: a string from A-Z
    :param bar_length: By default we are specified bar_length=20 if no value is specified by the user.
    :return: The histogram plot and all the characters with maximum frequency and all
    the percent of the sample that they represent.
    """
    max_ch = []
    word = ['character is', 'characters are']
    # If we have two or more characters with highest frequency we use word[1] else word[0].
    histogram = zip(lis_num, ev_char, normalize(counts))
    # Using zip() to combine three list into a single iterable.
    for p, q, r in histogram:
        # Iterating through the histogram.
        print(f'{q}[{p:02}]:' + '=' * round(r * bar_length))
    print("\n")
    for _ in lis_num:
        # For finding normalized area and appending to the list.
        a = _ / sum(lis_num)
        normalized_area.append(a)
    max_count = max(lis_num)
    max_area = max(normalized_area)
    histogram_1 = zip(lis_num, ev_char)
    for m, n in histogram_1:
        # Checking if we have two or more characters with the highest count.
        if m == max_count:
            max_ch += n
    max_ch = ','.join(max_ch)

    print(
        f'The highest frequency {word[1] if len(max_ch) > 1 else word[0]} {max_ch} and {"each" if len(max_ch)>1 else "it"} occurs {max(lis_num)} times.')
    print(
        f'The highest frequency {word[1] if len(max_ch) > 1 else word[0]} {max_ch} and {"each" if len(max_ch)>1 else "it"} accounts for {max_area * 100:.2f}%')


def normalize(lis_num, norm2peak=True):
    """
    Description: normalize function is used to normalize the peak or area according to the user.
    :param lis_num: character counts stored in a list
    :param norm2peak: By default we are specified norm2peak = True if no value is specified by the user.
    :return: the normalized_area list will be returned if norm2peak = True else normalized_peak list.
    """
    if not norm2peak:
        for _ in lis_num:
            c = _ / sum(lis_num)
            normalized_area.append(c)
        return normalized_area
    else:
        for _ in lis_num:
            d = _ / max(lis_num)
            normalized_peak.append(d)
    return normalized_peak


### Step 2 : Announce, prompt, get user response and using necessary for and if loops to analyze the characters and
# inserting to list.

# Announce
print("Text analysis using histogram technique and normalizing according to constant value \n")

alpha_li = string.ascii_uppercase
s_list = []
counts = []
normalized_area = []
normalized_peak = []
s = input('Enter text to analyze ... \n')
print('\n')
s = s.upper()
s = s.split()

for _ in s:
    # Iterating through user input and storing every character into list using concatenation.
    s_list += list(_)

for _ in alpha_li:
    # Counting frequency of the characters repeated in the user input and appending all the values to a list.
    count = 0
    for i in s_list:
        if _ == i:
            count += 1
    counts.append(count)

### Step 3 : Calling plot_bars() with the parameters.

plot_bars(counts, alpha_li)

