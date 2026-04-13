import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Set<Integer>> map = new HashMap<>();

        // store reserved seats per row
        for (int[] seat : reservedSeats) {
            map.computeIfAbsent(seat[0], k -> new HashSet<>()).add(seat[1]);
        }

        int result = 0;

        // rows with no reserved seats → 2 families
        result += (n - map.size()) * 2;

        for (Set<Integer> seats : map.values()) {
            boolean left = true, middle = true, right = true;

            // check left block (2–5)
            for (int i = 2; i <= 5; i++) {
                if (seats.contains(i)) {
                    left = false;
                    break;
                }
            }

            // check middle block (4–7)
            for (int i = 4; i <= 7; i++) {
                if (seats.contains(i)) {
                    middle = false;
                    break;
                }
            }

            // check right block (6–9)
            for (int i = 6; i <= 9; i++) {
                if (seats.contains(i)) {
                    right = false;
                    break;
                }
            }

            if (left && right) {
                result += 2;
            } else if (left || middle || right) {
                result += 1;
            }
        }

        return result;
    }
}