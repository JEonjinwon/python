package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 28, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(151, 31, 57, 15);
		contentPane.add(lbl1);
		
		tf2 = new JTextField();
		tf2.setBounds(220, 28, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setBounds(345, 31, 57, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int a = Integer.parseInt(tf1.getText());
				int b = Integer.parseInt(tf2.getText());
				int result =0;
				if(a<=b) {
					for(int i=a ;i<=b;i++) {
						result += i;
					}
					tf3.setText(result+"");
				}else {
					tf3.setText("앞의 글자가 더 큽니다.");
				}
			}
		});
		btn.setBounds(26, 117, 97, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(135, 118, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JLabel lbl3 = new JLabel("입니다.");
		lbl3.setBounds(297, 121, 57, 15);
		contentPane.add(lbl3);
	}
}
