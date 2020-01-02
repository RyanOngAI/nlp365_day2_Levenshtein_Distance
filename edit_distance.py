import sys
# A Dynamic Programming based Python program for edit 
# distance problem 
def editDistDP(str1, str2):
    m = len(str1) 
    n = len(str2)
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 

            # If str1 is empty, need to insert all characters of str2
            if i == 0: 
                dp[i][j] = j    # Min. operations = j

            # If str2 is empty, need to remove all characters of str1
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum  
            # Levenshtein Distance (substitution cost is 2)
            else: 
                dp[i][j] = min(dp[i][j-1] + 1,        # Insert
                                   dp[i-1][j] + 1,        # Delete 
                                   dp[i-1][j-1] + 2)    # Substitution 
  
    return dp, dp[m][n]

def prettyPrint2dArray(array2d):
    s = [[str(e) for e in row] for row in dp_table]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)


if __name__ == "__main__":

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    print("Calculating the Levenshtein Distance between " + str1 + " and " + str2)

    dp_table, edit_distance = editDistDP(str1, str2)
    
    print("Levenshtein Distance: " + str(edit_distance))
    print("Edit distance table: ")
    prettyPrint2dArray(dp_table)