# Here you create the method of the node object that will return the generator
  # Here is the code that will be called each time you use the generator object:
  # If there is still a child of the node object on its left AND if distance is ok, return the next child
  # If there is still a child of the node object on its right AND if distance is ok, return the next child
  # If the function arrives here, the generator will be considered empty. there is no more than two values: the left and the right children

def node._get_child_candidates(self, distance, min_dist, max_dist):

  if self._leftchild and distance - max_dist < self._median:
                yield self._leftchild

  if self._rightchild and distance + max_dist >= self._median:
                yield self._rightchild

caller
# Create an empty list and a list with the current object reference
# Loop on candidates (they contain only one element at the beginning)
# Get the last candidate and remove it from the list
    # Get the distance between obj and the candidate
    # If distance is ok, then you can fill the result
    # Add the children of the candidate in the candidates list so the loop will keep running until
    #it will have looked at all the children of the children of the children, etc. of the candidate

result, candidates = list(), [self]

while candidates:

    node = candidates.pop()
    distance = node._get_dist(obj)

    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
    return result
