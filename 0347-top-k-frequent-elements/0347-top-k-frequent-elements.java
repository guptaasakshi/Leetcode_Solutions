class Solution 
{
    public int[] topKFrequent(int[] nums, int k) 
    {
        // Create a HashMap to store the frequency of each element
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) 
  {
           if (frequencyMap.containsKey(num))
           {
              frequencyMap.put(num, frequencyMap.getOrDefault(num,0)+1);//if it contains we will add deafultly 1
           }
           else
           {
              frequencyMap.put(num,1);//else 1
           }
        }
        // Create a PriorityQueue to sort elements based on their frequencies
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> frequencyMap.get(b) - frequencyMap.get(a));
        // Add elements to the PriorityQueue
        pq.addAll(frequencyMap.keySet());//by using keyset we can add all elements without for loop
        // Create a list to store the top k frequent elements
        int[] topKFrequentElements = new int[k];
        int m=0;
        while (k > 0) 
  {
            topKFrequentElements[m++]=pq.poll();
            k--;
        }
        return topKFrequentElements;
    }
}