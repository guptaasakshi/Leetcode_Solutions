import java.util.*;

class Solution {
    public double[] internalAngles(int[] sides) {
        int a = sides[0], b = sides[1], c = sides[2];

        // Step 1: Check triangle validity
        if (a + b <= c || a + c <= b || b + c <= a) {
            return new double[0];
        }

        // Step 2: Apply cosine rule
        double A = Math.toDegrees(Math.acos((b*b + c*c - a*a) / (2.0 * b * c)));
        double B = Math.toDegrees(Math.acos((a*a + c*c - b*b) / (2.0 * a * c)));
        double C = Math.toDegrees(Math.acos((a*a + b*b - c*c) / (2.0 * a * b)));

        double[] ans = {A, B, C};

        // Step 3: Sort in non-decreasing order
        Arrays.sort(ans);

        return ans;
    }
}