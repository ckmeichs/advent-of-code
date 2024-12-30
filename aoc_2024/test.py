def can_form_design(design, towel_patterns):
    """
    Recursively checks if the design can be formed using the available towel patterns.
    """
    if not design:  # Base case: If the design is empty, it's successfully constructed.
        return True
    
    for pattern in towel_patterns:
        # Check if the design starts with the current pattern
        if design.startswith(pattern):
            # Recursively check the rest of the design
            if can_form_design(design[len(pattern):], towel_patterns):
                return True
    
    return False  # If no pattern matches, the design cannot be formed.

def count_possible_designs(towel_patterns, designs):
    """
    Counts how many designs can be formed using the given towel patterns.
    """
    possible_count = 0
    
    for design in designs:
        if can_form_design(design, towel_patterns):
            possible_count += 1
    
    return possible_count

# Example Input
towel_patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
designs = [
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb",
]

# Calculate the result
possible_count = count_possible_designs(towel_patterns, designs)

# Output the result
print(f"Number of possible designs: {possible_count}")