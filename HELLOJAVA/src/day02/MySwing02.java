package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing02 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02 frame = new MySwing02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	int i =1;
	/**
	 * Create the frame.
	 */
	public MySwing02() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl2 = new JLabel("1");
		lbl2.setBounds(48, 128, 74, 28);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("increase");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				i++;
				lbl2.setText(i+"");
			}
		});
		btn.setBounds(181, 96, 212, 92);
		contentPane.add(btn);
	}

}
