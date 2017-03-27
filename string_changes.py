from collections import deque
from itertools import chain
init_word = input("initial word: ").strip()
goal_word = input("target word: ").strip()

def expand(word):
        new_nodes = []
        #char_replace
        new_nodes.append((word[:i]+goal_word[i]+word[i+1:] for i in range(min(len(word),len(goal_word))) if goal_word[i] != word[i]))
        #char_delete
        new_nodes.append((word[:i]+word[i+1:] for i in range(len(word))))
        if len(word) < len(goal_word):
            #char_insert
            size = len(word)
            new_nodes.append((word[:i]+goal_word[i]+word[i:] for i in range(size) if word[i] != goal_word[i]))
            new_nodes.append([word[:size]+goal_word[size]+word[size:]])
        return chain.from_iterable(new_nodes)

def search():
    search_queue = deque([init_word])
    count = 0
    changes_count = 0
    size_of_this_layer = 1
    size_of_next_layer = 0
    while search_queue:
        word = search_queue.popleft()
        if word == goal_word:
            return changes_count
        else:
            expantion_size = -len(search_queue)
            search_queue.extend(expand(word))
            expantion_size += len(search_queue)
            if count == size_of_this_layer:
                count = 0
                changes_count += 1
                size_of_this_layer = size_of_next_layer
                size_of_next_layer = 0
            size_of_next_layer += expantion_size
            
        count += 1
print(search())
