def check_username(username):
    # If the length is greater than or equal to 3 AND less than or equal to 10
    if len(username) >= 3 and len(username) <= 10:
        return True
    else:
        return False
    
# A standard Python list containing your edge cases
test_cases = ["usr", "ab", "toolongusername", "", "admin123"]

# The 'for' loop grabs one item from the list at a time and temporarily calls it 'case'
for case in test_cases:
    
    # Pass the current case into the function and save the answer (True or False)
    result = check_username(case)
    
    # Print the outcome to your terminal
    print(f"Testing '{case}': Result = {result}")