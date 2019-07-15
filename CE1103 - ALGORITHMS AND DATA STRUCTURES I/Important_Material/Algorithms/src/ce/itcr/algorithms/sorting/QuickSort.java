package ce.itcr.algorithms.sorting;

public class QuickSort {
    public static void qsort(int a[],int start,int end) {
        if(start<end) {
            int pIndex=QuickPartition(a,start,end);
            qsort(a,start,pIndex-1);
            qsort(a,pIndex+1,end);
        }
        else
            return;

    }

    public static int QuickPartition(int a[],int start,int end) {
        int temp;
        int pivot=a[end];
        int pIndex=start;
        for(int i=start;i<end;i++) {
            if(a[i]<=pivot)
            {
                //swap a[i],apindex
                temp=a[i];
                a[i]=a[pIndex];
                a[pIndex]=temp;
                pIndex++;
            }
        }
        temp=a[pIndex];
        a[pIndex]=a[end];
        a[end]=temp;
        return pIndex;
    }

    public static void print(int a[],int n) {
        System.out.println();
        for(int i=0;i<n;i++)
            System.out.print(a[i]+"\t");
    }
}
