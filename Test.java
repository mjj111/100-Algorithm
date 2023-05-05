import java.util.*;
class Test{
    public static void main(String[] args) {
        String str = "hello";
        // for (char s : str.toCharArray()){
        //     System.out.println(s);
        // }
        int a = 212;
        System.out.print(String.valueOf(a));
        String as = "hi im mj";
        String[] splitedString = as.split(" ");
        for(String c : splitedString){
            System.out.println(c);
        }
        System.out.println(as.indexOf("m"));
        System.out.println(as.substring(0, 3));
        
        StringBuffer reverseString = new StringBuffer(str);
        System.out.print(reverseString.reverse().toString());
        char aplhabet = 's';
        System.out.println((int)aplhabet);
        int aaa = Integer.valueOf(aplhabet);
        System.out.println(aaa);
        int num = 77;
        String binum = Integer.toBinaryString(num);
        System.out.println(binum);
        int exA= 2;
        int exB= 3;
        System.out.println(Math.max(exA,exB));
        HashMap<Integer,Integer> hmap = new HashMap<>();
        hmap.put(1,2);
        System.out.println(hmap.get(1));
        
    }
}
