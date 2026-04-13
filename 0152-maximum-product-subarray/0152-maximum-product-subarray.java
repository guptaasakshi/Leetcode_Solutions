class Solution {
    public int maxProduct(int[] nums) {
        int max = nums[0];
        int min = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            // store previous max
            int temp = max;

            max = Math.max(num, Math.max(num * max, num * min));
            min = Math.min(num, Math.min(num * temp, num * min));

            result = Math.max(result, max);
        }

        return result;
    }
}