//Smallest sub array with given sum
/* Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
*/
//CODE IS WRITTEN IN C#
//This is the brute force approach
//I have rewritten this program using SlidingWindow Pattern ( File name : SmallestSubArraySW )

using System;

namespace slidingwindowpattern
{
    class Program
    {
        static void Main(string[] args)
        {
          int[] arr = new int[] {1, 3, 2, 6, -1, 4, 1, 8, 2};
          int k = 5;
          //below method is a brute force approach.
          //this has a complexity of O( n * k)
          Console.WriteLine("Brute force method ");
          AvgOfSubArray(arr, k);
        }
    }
    public static void AvgOfSubArray(int[] array, int k)
        {
            int n = array.Length;
            
            for(int i = 0; i < n-k+1; i++)
            {
                float sum = 0.0f;
                float avg = 0.0f;
                for(int j= i;  j < i + k;j++)
                {
                    sum = sum + array[j];
                }
                avg = sum / k;
                
                Console.Write(avg + " ");
            }
        }
}
