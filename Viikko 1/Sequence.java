public class Sequence {
    public String generate(int n) {
        String  result = "1";
        String  newresult = "";
        int     count = 0;
        char     number = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < result.length(); j++) {
                number = result.charAt(j);
                count++;
                if (j + 1 == result.length()) {
                    newresult += count;
                    newresult += number;
                    count = 0;
                    break ;
                }
                else if (result.charAt(j+1) != number) {
                    newresult += count;
                    newresult += number;
                    count = 0;
                }
            }
            result = newresult;
            newresult = "";
        }

        return result;
    }

    public static void main(String[] args) {
        Sequence s = new Sequence();
        System.out.println(s.generate(1)); // 1
        System.out.println(s.generate(2)); // 11
        System.out.println(s.generate(3)); // 21
        System.out.println(s.generate(4)); // 1211
        System.out.println(s.generate(5)); // 111221
    }
}
