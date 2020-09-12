import re
def solution(new_id):
    original = new_id
    text = original.lower()
    parse = re.sub('[][~!@#$%^&*()=+{}:?,<>]','',text)
    text = list(parse)
    idx_to_delete = []
    for idx in range(len(text)-1):
        if text[idx] == '.':
            if text[idx] == text[idx+1]:
                idx_to_delete.append(idx+1)
    for idx in reversed(idx_to_delete):
        text.pop(idx)

    idx_to_delete.clear()
    for idx in range(len(text)):
        if text[idx] == '.':
            if idx == 0 or idx == len(text)-1:
                idx_to_delete.append(idx)
    for idx in idx_to_delete:
        text.pop(idx)

    if not text:
        text.append('a')

    if len(text) >= 16:
        text = text[:15]
        if text[-1] == '.':
            text.pop(-1)

    if len(text) <= 2:
        while len(text) < 3:
            text = text + list(text[-1])

    answer = text
    return answer


a = solution("...!@BaT#*..y.abcdefghijklm")
print(''.join(a))