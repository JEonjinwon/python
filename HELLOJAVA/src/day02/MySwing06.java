package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 154, 241);
		contentPane.add(ta);
		
		tf = new JTextField();
		tf.setText("2");
		tf.setBounds(174, 11, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("구구단 출력");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
			
			int a = Integer.parseInt(tf.getText());
			ta.setText(a+"단\r\n"+
					a+"X 1 = "+a+"\r\n"+
					a+"X 2 = "+a*2+"\r\n"+
					a+"X 3 = "+a*3+"\r\n"+
					a+"X 4 = "+a*4+"\r\n"+
					a+"X 5 = "+a*5+"\r\n"+
					a+"X 6 = "+a*6+"\r\n"+
					a+"X 7 = "+a*7+"\r\n"+
					a+"X 8 = "+a*8+"\r\n"+
					a+"X 9 = "+a*9	);
			
			
			
			
			
			
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(172, 45, 97, 23);
		contentPane.add(btn);
	}

}
