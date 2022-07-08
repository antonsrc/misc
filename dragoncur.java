public class te_7 {
    public static void main(String[] args) {
	    char[] ar;
	    int N = 3;
	    String text = "F", text_inv;

	    for (int i=0; i <= N; i++){
	        ar = text.toCharArray();
	        text_inv = "";
	        for (int j = ar.length-1; j >= 0; j--){
	            if (ar[j] == 'L') ar[j] = 'R';
	            else if (ar[j] == 'R') ar[j] = 'L';
	            text_inv = text_inv + ar[j];
            }
	        if (i != 0) text = text + 'L' + text_inv;
	        System.out.println("n = "+i+", "+text);
        }
    }
}
