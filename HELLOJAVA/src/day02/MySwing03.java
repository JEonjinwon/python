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

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField TFA;
	private JTextField TFB;
	private JTextField TFC;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		TFA = new JTextField();
		TFA.setBounds(12, 30, 116, 21);
		contentPane.add(TFA);
		TFA.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(151, 33, 57, 15);
		contentPane.add(lbl);
		
		TFB = new JTextField();
		TFB.setBounds(220, 30, 116, 21);
		contentPane.add(TFB);
		TFB.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int A = Integer.parseInt(TFA.getText());
				int B = Integer.parseInt(TFB.getText());
				
				TFC.setText(A+B+"");
			}
		});
		btn.setBounds(48, 107, 97, 23);
		contentPane.add(btn);
		
		TFC = new JTextField();
		TFC.setBounds(193, 108, 116, 21);
		contentPane.add(TFC);
		TFC.setColumns(10);
	}
}
