# Cards are given in descending order. You need to find the position of the card in the deck if the card is in the deck.

# All kinds of testcases for the given problem
test_cases_for_cards = [
    {"ip": [5,4,3,2,1], "query_card": 3, "op":2},
    {"ip": [], "query_card": 3, "op":-1},
    {"ip": [5,4,3,2,1], "query_card": 5, "op":0},
    {"ip": [1], "query_card": 3, "op":-1},
    {"ip": [5,4,3,2,1], "query_card": 10, "op":-1}
    ]

# Tester function for testing against multiple testcases
def function_evaluator(function, testcases):
    passed = 0
    total =  len(testcases)
    tcno = 1
    for testcase in testcases:
        result = function(testcase['ip'], testcase['query_card'])
        print("================================================================")
        print("Deck of Cards: ", testcase['ip'])
        print("Query Cards: ", testcase['query_card'])
        print("Expected Output: ", testcase['op'])
        print("Your Output: ", result)

        if result == testcase['op']:
            print("Test Case {}: Passed Successfully".format(tcno))
            passed += 1
        else:
            print("Test Case {}: Failed!".format(tcno))
        
        print("================================================================")
        tcno += 1

    print("\nFinal Test Cases Status {}/{} Passed Successfully, {} Tests Failed".format(passed,total,total-passed))
    return None

def card_locator(cards, query_card):
    # If query_card is not in the range of cards
    if len(cards) == 0 or query_card == None:
        # print("No Deck of cards provided.")
        return -1

    if cards[0] < query_card or cards[-1] > query_card:
        # print("Card not Found in Deck")
        return -1

    start = 0
    end = len(cards)
    
    while  start < end:
        mid = (start + end)//2
        if cards[mid] == query_card:
            # print("Card Successfully Found at index ",mid )   
            return mid
        elif cards[mid] < query_card:
            end = mid - 1
        else:
            start = mid + 1

    # print("Card not Found in Deck")
    return -1

#Driver Code
if __name__ == '__main__':
    try:
        function_evaluator(card_locator,test_cases_for_cards)
    except Exception as e:
        print(e)
    