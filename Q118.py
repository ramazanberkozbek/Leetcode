"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""

# Pascal's triangle
def generate(numRows):
    pascal_triangle = [[1]*i for i in range(1,numRows+1)] #pascal üçgenini 1 lerle oluşturdum

    for i in range(numRows): 
        for j in range(1,i): #1 den başlayıp i ye kadar ilk ve son elemanları görmezden geliyor
            pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j] 
    return pascal_triangle

print(generate(5))