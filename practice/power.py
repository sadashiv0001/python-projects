class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def __init__ (self, A, B):
        self.A = A
        self.B = B

    def power(self):
        result = self.A ** self.B
        print(result)

if __name__ == "__main__":
    InputA = int(input("Enter the base: "))
    InputB = int(input("Enter the exponent: "))
    SolObj = Solution(InputA, InputB)
    SolObj.power()
                

