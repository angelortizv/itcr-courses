package ce.itcr.algorithms.sorting;

public class BubbleSort {
    public void sort(int a[],int n) {
        int temp;
        boolean swap;
        for(int i=0;i<n-1;i++) {
            swap=false;
            for(int j=0;j<n-1;j++) {
                if(a[j]>a[(j+1)])
                {
                    temp=a[j];
                    a[j]=a[(j+1)];
                    a[(j+1)]=temp;
                    swap=true;
                }
            }
            if(swap==false)
                break;
        }
        print(a,n);
    }

    public static void print(int a[],int n) {
        System.out.println();
        for(int i=0;i<n;i++)
            System.out.print(a[i]+"\t");
    }

}
