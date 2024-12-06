from collections import defaultdict
order_input, books = open("input.txt", "r").read().split('\n\n')
ordering = defaultdict(list)
for line in order_input.split('\n'):
    left, right = map(int, line.split('|'))
    ordering[left].append(right)
books = [[int(num) for num in line.split(',')] for line in books.split('\n')]
def is_ordered(pages):
    for ix, page1 in enumerate(pages[:-1]):
        for page2 in pages[ix:]:
            if page1 in ordering[page2]:
                return False
    return True

print(sum([pages[len(pages)//2] if is_ordered(pages) else 0 for pages in books]))