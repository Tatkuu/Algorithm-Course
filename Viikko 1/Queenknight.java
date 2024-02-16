public class QueenKnight {
    public boolean checkKnight(int[] knight, int[] queen) {
        int x;
        int y;

        x = Math.abs(knight[1] - queen[1]);
        y = Math.abs(knight[0] - queen[0]);

        if ((x == 2 && y == 1) || (x == 1 && y == 2)) {
            return true;
        } else {
           return false;
        }
    }

    public boolean checkQueen(int[] queen, int[] knight) {
        int x;
        int y;

        x = Math.abs(queen[1] - knight[1]);
        y = Math.abs(queen[0] - knight[0]);

        if (x == 0 || y == 0 || x == y) {
            return true;
        } else {
            return false;
        }
    }

    public int[] moveUnit(int[] unit, int x, int y, int length) {
        int unitx = unit[1];
        int unity = unit[0];

        if (unitx < length) {
            unitx += 1;
        } else if (unitx == length) {
            if (unity < length) {
                unitx = 0;
                unity += 1;
            } else if (unity == length) {
                unitx = x;
                unity = y;
            }
        }
        unit[0] = unity;
        unit[1] = unitx;
        return unit;
    }

    public int count(int n) {
        int[] knight = new int[2];
        int[] queen = new int[2];
        int result = 0;
        int length = n -1;
        knight[0] = 0;
        knight[1] = 1;
        queen[0] = 0;
        queen[1] = 0;
        while (true) {
            if (!checkQueen(queen, knight) && !checkKnight(knight, queen)) {
                result += 1;
            }
            queen = moveUnit(queen, 0, 0, length);
            if (queen[0] == 0 && queen[1] == 0) {
                knight = moveUnit(knight, 0, 0, length);
                if (knight[0] == 0 && knight[1] == 1) {
                    break ;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        QueenKnight q = new QueenKnight();
        System.out.println(q.count(3)); // 0
        System.out.println(q.count(4)); // 40
        System.out.println(q.count(5)); // 184
    }
}
