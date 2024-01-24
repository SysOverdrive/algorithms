"""
Cats are jumping into a crate ! The capacity of the crate is 5 cats, so if a cat jumps in when there are already 5 cats inside then the fattest cat gets pushed outside
At any given time we need to know the top 5 breeds and count for each breed of cat.
Your solution should work well for large create capacities as well
Implement two methods:

//Called when a cat jumps into the crate
add(breed: str, weight: int)
//Called frequently aat any time prints the top 5 occurences of the type of cat with the count, sorted by count descenting
Example

>> add(”Siamese”, 4)
>>
>>top()
Siamise 1 
>> add(”British Shorthair”, 5)
>>top 
Siamese 1

British Shorthair 1
"""
## Solution I see: 2 approaches one with hashmap of a list the other with a linked list.

class Cat:
    def __init__(self, breed, weight):
        self.breed = breed
        self.weight = weight

class Crate:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cats = []  # List to act as a min-heap
        self.breed_count = {}  # Dictionary for breed count

    def push_heap(self, cat):
        
        i = len(self.cats)
        self.cats.append(cat)
        
        while i > 0 :
            if self.cats[i].weight < self.cats[(i - 1) // 2].weight:
                self.cats[i], self.cats[(i - 1) // 2] = self.cats[(i - 1) // 2], self.cats[i]
                i = (i - 1) // 2

    def pop_heap(self):
        if not self.cats:
            return None
        removed_cat = self.cats[0]
        self.cats[0] = self.cats[-1]
        self.cats.pop()
        i = 0
        while 2 * i + 1 < len(self.cats):
            min_child = 2 * i + 1
            if min_child + 1 < len(self.cats) and self.cats[min_child + 1].weight < self.cats[min_child].weight:
                min_child += 1
            if self.cats[i].weight <= self.cats[min_child].weight:
                break
            self.cats[i], self.cats[min_child] = self.cats[min_child], self.cats[i]
            i = min_child
        return removed_cat

    def add(self, breed, weight):
        cat = Cat(breed, weight)
        self.push_heap(cat)
        self.breed_count[breed] = self.breed_count.get(breed, 0) + 1
        if len(self.cats) > self.capacity:
            removed_cat = self.pop_heap()
            self.breed_count[removed_cat.breed] -= 1

    def top(self):
        sorted_breeds = sorted(self.breed_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_breeds[:5]

if __name__ == "__main__":
        # Example Usage
    crate = Crate(5)
    crate.add("Siamese", 4)
    print(crate.top())  # [("Siamese", 1)]
    crate.add("British Shorthair", 5)
    print(crate.top())  # [("Siamese", 1), ("British Shorthair", 1)]
    #Scenario 1: Add more cats of different breeds
    crate.add("Persian", 6)
    crate.add("Maine Coon", 7)
    crate.add("Ragdoll", 5)
    print(crate.top())  # Top 5 breeds after adding these cats

    # Scenario 2: Crate reaches capacity and starts removing the fattest cat
    crate.add("Bengal", 8)  # This should push out the fattest cat
    print("Adding a fatter cat")
    print(crate.top())  # Top 5 breeds after capacity reached

    # Scenario 3: Adding multiple cats of the same breed
    print("Add 3 lightweight Sphinx")
    for _ in range(3):
        crate.add("Sphynx", 4)
    print(crate.top())  # Top 5 breeds after adding multiple Sphynx cats

    # Scenario 4: Adding a very light cat when the crate is full
    crate.add("Russian Blue", 3)
    print(crate.top())  # Top 5 breeds after adding a light Russian Blue cat

    # Scenario 5: Adding a mix of breeds
    crate.add("Scottish Fold", 4)
    crate.add("Siamese", 4)
    print(crate.top())  # Top 5 breeds after adding a mix of breeds