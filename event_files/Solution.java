import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] arr = Arrays.stream(br.readLine().trim().split("\\s+"))
                          .mapToInt(Integer::parseInt)
                          .toArray();
        System.out.println(findSingleNumber(arr));
    }

    private static int findSingleNumber(int[] arr) {
        int result = 0;
        for (int num : arr) {
            result ^= num;
        }
        return result;
    }
}
