class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer>set = new HashSet<>();
        for(int n : nums){
            if(set.add(n)!=true){
                return true;
            }
            set.add(n);
        }
    return false;
    }
}