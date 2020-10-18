
def reverse_string(string):
    return string[::-1]


# using reversed() 
# Function to reverse a string 
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 

if __name__=="__main__":
    print(reverse_string("apple"))
