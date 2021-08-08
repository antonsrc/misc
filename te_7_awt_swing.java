// te_7_awt_swing

import java.awt.Graphics;
import javax.swing.JComponent;
import javax.swing.JFrame;

class MyCanvas extends JComponent {
	public void paint(Graphics g) {
		char[] ar;
		int N = 12;
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
	        //System.out.println("n = "+i+", "+text);
        }
		
		int step_size = 5, LR;
		int x0 = 860, y0 = 440, xn = 860+step_size, yn = 440;
		g.drawLine(x0,y0,xn,yn);
		ar = text.toCharArray();
		for (int i=0; i < text.length(); i++) {
			if (ar[i] == 'R') LR = -1;
			else LR = 1;
			
			if (ar[i] != 'F'){
				if (yn-y0 == 0) {
					if (x0-xn > 0) {
						x0 = xn;
						y0 = yn;
						yn = yn-step_size*LR;
					}
					else {
						x0 = xn;
						y0 = yn;
						yn = yn+step_size*LR;						
					}
				}
				else {
					if (y0-yn < 0) {
						x0 = xn;
						y0 = yn;
						xn = xn-step_size*LR;
					}
					else {
						x0 = xn;
						y0 = yn;
						xn = xn+step_size*LR;						
					}
				}
				g.drawLine(x0,y0,xn,yn);
			}
		}
	}
}

public class te_7_awt_swing {
    public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setBounds(100, 100, 1720, 880);
		window.getContentPane().add(new MyCanvas());
		window.setVisible(true);
    }
}
