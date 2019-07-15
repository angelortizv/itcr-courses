package ce.itcr.algorithms.searching;

public class LinearSearch {
    public boolean linearSearch(int[] list, int key) {

        for(int i = 0; i < list.length; i++) {
            if(list[i] == key){
                return true;
            }

        }
        return false;
    }

}
