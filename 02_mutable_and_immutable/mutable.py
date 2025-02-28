# Mutable data types:
# Lists
my_list = [1, 2, 3]
my_list.append(4)
print("List:", my_list)  # Output: List: [1, 2, 3, 4]

# Dictionaries
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print("Dictionary:", my_dict)  # Output: Dictionary: {'a': 1, 'b': 2, 'c': 3}

# Sets
my_set = {1, 2, 3}
my_set.add(4)
print("Set:", my_set)  # Output: Set: {1, 2, 3, 4}

# Byte arrays
my_bytearray = bytearray(b'hello')
my_bytearray[0] = ord('j')
print("Byte array:", my_bytearray)  # Output: Byte array: bytearray(b'jello')


# Immutable data types:
# Integers
my_int = 5
my_int = 6  # Reassignment
print("Integer:", my_int)  # Output: Integer: 6

# Floats
my_float = 3.14
my_float = 2.71
print("Float:", my_float)  # Output: Float: 2.71

# Strings
my_string = "hello"
my_string = "jello"  # Reassignment
print("String:", my_string)  # Output: String: jello

# Tuples
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This would raise an error
my_tuple = (4, 5, 6) # reassigning the tuple to a new value
print("Tuple:", my_tuple)  # Output: Tuple: (4, 5, 6)

# Booleans
my_bool = True
my_bool = False
print("Boolean:", my_bool)  # Output: Boolean: False

# Frozen sets
my_frozenset = frozenset({1, 2, 3})
# my_frozenset.add(4)  # This would raise an error
print("Frozen set:", my_frozenset)  # Output: Frozen set: frozenset({1, 2, 3})

# Bytes
my_bytes = b'hello'
# my_bytes[0] = ord('j')  # This would raise an error
print("Bytes:", my_bytes) # Output: Bytes: b'hello'

# None
my_none = None
print("None:", my_none) # Output: None: None