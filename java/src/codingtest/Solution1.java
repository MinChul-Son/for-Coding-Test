package codingtest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class Solution1 {

    public static void main(String[] args) {
        TreeMap<Integer, Integer> tree = new TreeMap<Integer, Integer>();
        tree.put(1, 1);
        List<Integer> collect = tree.values().stream().sorted().collect(Collectors.toList());
//        Object[] objects = tree.keySet().toArray();
//        Integer[] integers = Arrays.copyOf(objects, objects.length, Integer[].class);
//        tree.put(integers[0], integers[0] + 1);
//        List<Integer> list = new ArrayList<>();
        int[] arr = {1,2,3,4};

    }
}
