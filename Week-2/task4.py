n_val, m_val = map(int, input().split())
lecture_chars = input().strip()
unique_words = set()
for slide in range(n_val - m_val + 1):
    unique_words.add(lecture_chars[slide:slide+m_val])
print(len(unique_words))
