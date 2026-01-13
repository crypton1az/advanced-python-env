word_count = {}
line_total = 0
word_total = 0

with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_total += 1
        clean_line = ""

        for ch in line.lower():
            if ch.isalpha() or ch == " ":
                clean_line += ch

        words = clean_line.split()

        for w in words:
            word_total += 1
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1

with open("analysis.txt", "w", encoding="utf-8") as result:
    result.write("Lines: " + str(line_total) + "\n")
    result.write("Words: " + str(word_total) + "\n")
    result.write("Word frequency:\n")

    for key in word_count:
        result.write(key + ": " + str(word_count[key]) + "\n")
