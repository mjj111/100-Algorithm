import java.util.*;
class Test{
    public static void main(String[] args) {
        ArrayList<Integer> arList = new ArrayList<Integer>();
        ArrayList<Integer> copyW = new ArrayList<Integer>();
        copyW.addAll(arList);
        arList.add(1);
        arList.add(3);
        arList.add(2);
        arList.add(1);
        arList.sort(null);
        arList.remove(0);
        System.out.println(arList.toString());
        
        Set<Integer> setList = new HashSet<Integer>();
        setList.add(2);

        int [] arr = {1,2,3,4,5};
        Arrays.sort(arr);
        int [] tmp = Arrays.copyOfRange(arr,1,3);
        
        String str = "12345";
        char[] charArray = str.toCharArray();
        System.out.println(charArray[0]);

        Map<String,Integer> hmap = new HashMap<>();
        hmap.put("h",1);
        hmap.get("h");
        hmap.getOrDefault("h",1);
        hmap.containsKey("h");
        System.out.println(hmap.get("not"));
        Map<String,ArrayList<Integer>> biMap = new HashMap<>();
        
        String satr = "hello";
        System.out.println(satr.toLowwerCase());
    }

}
