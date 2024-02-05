"""
------- The Problems from Optimzly Soluation ----


This is a fun problem I always enjoy walking through with people. It's influenced by a problem I had to solve in my career which may not need super advanced coding skills or knowledge of data structures, but needs some good old fashioned thinking and problem solving. Submit your solution and I'll reach out to you if I find it interesting!

Here's the problem:

Imagine you're working at T-shirt factory and you manage orders by packing a bulk amount of shirts into a certain amount of bags. Meaning, for every order you have a specification of how many bags you have to fill, and a fixed number of shirts to fill them with.

The requirement is to be able to distribute the shirts in the bag as evenly as possible. For example, if there are 100 shirts, and 10 bags, then each bag will get 10 shirts. However, sometimes the shirt factory will have production errors, and it might produce the wrong number of shirts. It's not going to be 200 shirts instead of 100, but it will have some minor deviation from the original number.

Just to clarify, for every order there is a fixed number of shirts and fixed number of bags, you will just have to distribute the shirts across the bags as evenly as possible.

Write a function to solve this problem. Define the function name, input parameters and output type as you wish.

Constraints:
- The number of shirts and number of bags will always be known
- The size of the bag does not matter
- You have to use all the bags, and cannot add or remove any bags
- The goal is to minimise the deviation of number of shirts in each bag, i.e. as even as possible
- You should come up with your own test cases

Some things in this problem are purposefully left vague to see how you think about this problem. Think of what you would do if you physically had the shirts and bags in front of you, and what would the most efficient way to do this would be.
"""


def distribute_shirts(num_shirts, num_bags):
    # Calculate the base number of shirts per bag
    base_shirts_per_bag = num_shirts // num_bags
    # Calculate the number of bags that will have one extra shirt
    extra_shirts = num_shirts % num_bags
    
    # Initialize a list to store the number of shirts in each bag
    bags = [base_shirts_per_bag] * num_bags
    
    # Distribute the extra shirts among the bags with one extra shirt each
    for i in range(extra_shirts):
        bags[i] += 1
    
    return bags

# # Test cases - 01
# print(distribute_shirts(100, 10))  # Example test case
# print(distribute_shirts(101, 10))  # Test case with one extra shirt
# print(distribute_shirts(99, 10))   # Test case with one shirt less
# print(distribute_shirts(50, 5))    # Test case with fewer bags
# print(distribute_shirts(1000, 7))  # Test case with more bags
# print(distribute_shirts(75, 10))  # Test case with more bags

# Test cases - 02


"""
Here's how it works:

When a generator function is called, it returns a generator object without actually executing the function's code.
Each time the yield statement is encountered in the generator function, the function's execution is paused, and the value specified by yield is returned to the caller.
The state of the generator function is preserved, allowing it to resume execution right after the yield statement the next time it's called.
The caller can iterate over the generator object using a loop or by explicitly calling the next() function, retrieving values one at a time.
In the distribute_shirts function:

We calculate the number of shirts for each bag based on the total number of shirts and bags.
Instead of returning a list of all bags at once, we use yield to produce each bag's shirt count one at a time.
This allows us to lazily generate the shirt counts as needed, reducing memory usage, especially for large numbers of shirts and bags.
The caller can iterate over the generator object returned by distribute_shirts, getting each bag's shirt count sequentially without needing to store all shirt counts in memory simultaneously.


------  Explanation -------

This way, we avoid creating and storing the entire list of bags, which can be unnecessary if the number of shirts and bags is very large. Instead, we can yield the number of shirts for each bag dynamically.

"""


def distribute_shirts(shirts, bags):
      avr_shirts_per_bags = shirts // bags
      
      extra_shirts = shirts % bags
      
      
      for i in range(bags):
            yield avr_shirts_per_bags + ( 1 if i < extra_shirts else 0)


# Test cases - 02
print(list(distribute_shirts(100, 10)))  # Example test case
print(list(distribute_shirts(101, 10)))  # Test case with one extra shirt
print(list(distribute_shirts(99, 10)))   # Test case with one shirt less
print(list(distribute_shirts(50, 5)))    # Test case with fewer bags
print(list(distribute_shirts(1000, 7)))  # Test case with more bags