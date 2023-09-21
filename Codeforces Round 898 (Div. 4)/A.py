def is_possible(cards):
    swaps = [("a", "b"), ("b", "c"), ("a", "c")]

    for swap in swaps:
        modified_cards = list(cards)
        for i in range(2):
            modified_cards[modified_cards.index(swap[i])] = swap[1 - i]
        
        if "".join(modified_cards) == "abc":
            return "YES"
    
    return "NO"

t = int(input())

for _ in range(t):
    cards = input()  
    
   
    print(is_possible(cards))
