import java.util.*;
public class Singleoccurence {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums=new int[n];        
        for(int i=0;i<n;i++)
            nums[i] = sc.nextInt();        
        for(int i = 0;i < n;i++) {
            boolean isSingle=true;
            for (int j = 0;j<n;j++){
                if (i!=j && nums[i]==nums[j]){
                    isSingle=false;
                    break;
                }
            }
            if (isSingle) {
                System.out.println(nums[i]);
                return;
            }
        }
    }
}
