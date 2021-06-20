# Coding-Practice
Exercise programs

Solution for no more than k distinct substring 
This problem follows the Sliding Window pattern and we can use a similar dynamic sliding window strategy as discussed in Smallest Subarray with a given sum. We can use a HashMap to remember the frequency of each character we have processed. Here is how we will solve this problem:

First, we will insert characters from the beginning of the string until we have ‘K’ distinct characters in the HashMap.
These characters will constitute our sliding window. We are asked to find the longest such window having no more than ‘K’ distinct characters. We will remember the length of this window as the longest window so far.
After this, we will keep adding one character in the sliding window (i.e. slide the window ahead), in a stepwise fashion.
In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than ‘K’. We will shrink the window until we have no more than ‘K’ distinct characters in the HashMap. This is needed as we intend to find the longest window.
While shrinking, we’ll decrement the frequency of the character going out of the window and remove it from the HashMap if its frequency becomes zero.
At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.
Here is the visual representation of this algorithm for the Example-1:


![image](https://user-images.githubusercontent.com/32676744/122677214-083ccc80-d1ff-11eb-961d-a7153cc94413.png)
![image](https://user-images.githubusercontent.com/32676744/122677301-6a95cd00-d1ff-11eb-8ace-453606fefd14.png)


